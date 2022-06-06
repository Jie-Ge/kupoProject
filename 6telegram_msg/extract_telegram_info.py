# -*- coding: utf-8 -*-

"""
Created On Mon 23 May 2022
@author john
"""

import re
import json
import pandas as pd
import psycopg2

high_frequency_words = ['app', 'KYC', 'HPT', 'TikTok', 'ins', 'com',
                        'bsc', 'eth', 'tron', 'Metaverse', 'network',
                        'pancake', 'https', 'unicrypt', 'NFT', 'DFC',
                        'NFTs', 'DEX', 'Dapp', 'DeFi', 'USDT', 'swap',
                        'Token', 'Erc20', 'soul', 'ZFB', 'user', 'http',
                        'bnb', 'BBC', 'Twitter', 'Youtube', 'Telegram',
                        'PancakeSwap', 'www', 'dextools', 'finance',
                        'pair', 'VPN', 'explorer', 'eat', 'bscscan',
                        'logo', 'TikTok', 'CPA', 'github', 'CPU', 'yes']
other_words = ['PancakeSwap', 'WhatsAPP']


class ExtractTelegraminfo(object):
    """
    抽取telegram文本信息
    get_full_result：历史数据抽取解析入库
    get_increase_result：增量数据解析，返回解析结果：json格式
    """
    def __init__(self, host='192.168.224.80', port='5432', password='1qaz2wsx', user='mxadmin', database='yuqing'):
        self.host = host
        self.port = port
        self.password = password
        self.user = user
        self.database = database

    def get_full_result(self):
        data = self.get_postgres_data()
        data['result'] = data['text_info'].map(lambda x: self.info_extract(x))
        self.write_postgres_data(data)

    def get_increase_result(self, info):
        result = self.info_extract(info)
        return result

    def get_postgres_data(self):
        """ 获取历史数据 """
        try:
            conn = psycopg2.connect(database=self.database,
                                    user=self.user,
                                    password=self.password,
                                    host=self.host,
                                    port=self.port)
            print(conn)
            cur = conn.cursor()
            print(cur)
            sql = "select * from telegram01.telegram_msg_01"
            cur.execute(sql)
            data01 = cur.fetchall()
            data01 = pd.DataFrame(data01, columns=['link', 'date_time', 'text_info', 'result'])
            return data01
        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL", error)
            return None

    def write_postgres_data(self, data01):
        data_cols = list(data01.columns)
        # convert 'nan' and np.nan to None
        data01 = data01.reindex(columns=data_cols).mask(data01.isna() | (data01 == 'nan'), None)
        data_temp = data01[data_cols].to_dict('records')
        try:
            conn = psycopg2.connect(database=self.database,
                                    user=self.user,
                                    password=self.password,
                                    host=self.host,
                                    port=self.port)

            cur = conn.cursor()
            sql = "drop table if exists telegram01.telegram_msg_02;|" \
                  "create table telegram01.telegram_msg_02(" \
                  "link varchar(255) not null," \
                  "date_time timestamp(6)," \
                  "text_info text," \
                  "result   jsonb);|" \
                  "insert into telegram01.telegram_msg_02 values(%(link)s,%(date_time)s,%(text_info)s,%(result)s)"
            sql = sql.split('|')
            cur.execute(sql[0])
            cur.execute(sql[1])
            print('writing table ...')
            cur.executemany(sql[2], data_temp)
            conn.commit()
            conn.close()
            print('finished')
        except (Exception, psycopg2.Error) as error:
            print("Error while writing data from PostgreSQL", error)
            return None

    def info_extract(self, info):
        result_info = {}
        if self.isNone(info):
            return json.dumps(result_info, ensure_ascii=False)
        else:
            # 1. 网页信息，电报群信息，推特信息
            urls_telegram, urls_twitter, urls_website = self.extract_url(info)
            # 2. 邮箱账号
            emails = re.findall(r"[A-Za-z0-9\.\-+_]+@[a-z0-9A-Z\.\-+_]+\.[a-z]+", info)
            emails = list(set(emails))
            # 3. telegram联系人账号
            telegram_persons = self.extract_telegram_person(info)
            # 4. 涉及国内手机号码
            mobiles_in_china = re.findall(r"1\d{10}", info)
            mobiles_in_china = list(set(mobiles_in_china))
            # 5. 微信号
            wechat_number = self.extract_wechat(info)
            # 6. token地址识别
            token_address = self.extract_token(info)
            # 7. 疑似代币发行时间
            publish_time = self.extract_time(info)
            # 8. 代币所在链识别
            block_chain = self.extract_chain(info)
            # 9. qq群号识别
            qq_number = self.extract_qq_number(info)
            # 10. 可能项目名称识别
            project_name = self.extract_project_name(info)
            # 11. 可能代币类别
            project_type = self.extract_project_type(info)

            result_key_list = ['telegram_group', 'twitter_group', 'urls',
                               'email', 'telegram_person', 'mobiles_in_china',
                               'wechat', 'token_address', 'publish_time',
                               'block_chain', 'qq_number', 'project_name',
                               'project_type']
            result_info_list = [urls_telegram, urls_twitter, urls_website,
                                emails, telegram_persons, mobiles_in_china,
                                wechat_number, token_address, publish_time,
                                block_chain, qq_number, project_name,
                                project_type]
            key_record = 0
            for i in range(len(result_key_list)):
                if len(result_info_list[i]) > 0:
                    key_record += 1
                    result_info[result_key_list[i]] = result_info_list[i]
                else:
                    result_info[result_key_list[i]] = ''
            result_info = json.dumps(result_info, ensure_ascii=False)
            # 如果全部没有value，则返回空值
            if key_record == 0:
                result_info = None
                result_info = json.dumps(result_info, ensure_ascii=False)
            return result_info

    def extract_url(self, info):
        """
         消息文本中提取网页信息，电报群信息，推特信息
        """
        urls = re.findall(
            r"(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*,]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)|([0-9a-zA-Z]+.\w+\.+[a-zA-Z0-9\/_]+)",
            info)
        urls = list(sum(urls, ()))
        urls = [re.split('[,， ]', x) for x in urls if x != '']
        urls_ = []
        for _ in urls:
            urls_ += _
        # 1.1 将网页中的电报群信息单独提取出来
        urls_telegram = []
        urls_website = []
        urls_twitter = []
        for _ in urls_:
            _ = _.strip('()[]')
            if '/t.me' in _:
                urls_telegram.append(_)
            elif 'twitter' in _:
                urls_twitter.append(_)
            elif len(re.findall(r'http|www|com', _)) >= 1 and '@' not in _:
                urls_website.append(_)
            else:
                pass

        # 结果信息去重
        urls_telegram = list(set(urls_telegram))
        urls_twitter = list(set(urls_twitter))
        if '' in urls_website:
            urls_website.remove('')
        urls_website = list(set(urls_website))
        return urls_telegram, urls_twitter, urls_website

    def extract_wechat(self, info):
        """ 微信号提取 """
        wechat = re.findall(r"[V|v|微信|威|微][A-Za-z0-9💕❤\.\_\-@\s\:\：\】\咨询\号\,\，\;\；\]\"]+", info)
        wechat_list = []
        for wechat_number in wechat:
            wechat_list += re.split("[,，】]", wechat_number)
        # 去掉中文
        wechat_list = [re.sub('[\u4e00-\u9fa5]', '', _) for _ in wechat_list]
        # 按照长度干掉，&去掉日期数据,去掉特殊标点
        wechat_list01 = [_.strip('()[] ') for _ in wechat_list if
                         6 <= len(_.strip('()[] ')) <= 20 and not _.startswith('202')]
        wechat_list02 = []
        for _ in wechat_list01:
            wechat_list02 += re.split("[\"/,，：；;:']", _)
        wechat_list03 = [_.strip() for _ in wechat_list02 if
                         6 <= len(_) <= 20 and len(re.findall(r' |\|\\', _.strip())) == 0
                         and '.com' not in _]
        wechat_list03 = list(set(wechat_list03))

        # 去掉高频词汇
        high_frequency_words_lower = [_.lower() for _ in high_frequency_words]
        high_frequency_words_upper = [_.upper() for _ in high_frequency_words]
        high_frequency_words_title = [_.title() for _ in high_frequency_words]

        high_frequency_words_all = high_frequency_words_lower + high_frequency_words_upper + \
                                   high_frequency_words_title + other_words
        wechat_list03 = list(set(wechat_list03) - set(high_frequency_words_all))
        # 微信号不能是url里面 and telegram_person 的内容
        urls_telegram, urls_twitter, urls_website = self.extract_url(info)
        telegram_person = self.extract_telegram_person(info)
        urls = list(set(urls_telegram + urls_twitter + urls_website + telegram_person))
        remove_list = []
        for name in wechat_list03:
            # print(name)
            for url in urls:
                if name in url:
                    # print(url)
                    remove_list.append(name)
                    break
        wechat_list03 = list(set(wechat_list03) - set(remove_list))
        # 去掉可能重复的微信号
        for _ in wechat_list03:
            if _.startswith('v') or _.startswith('V'):
                if _.strip('v|V') in wechat_list03:
                    wechat_list03.remove(_)
            if len(re.findall(r"[0-9]+[Kk]-[0-9]+[Kk]", _)) >= 1:  # 去掉招聘信息里里面解析出的微信号
                wechat_list03.remove(_)
        return wechat_list03

    def extract_telegram_person(self, info):
        """ 抽取电报联系人信息 """
        telegram_persons = re.findall(r"@[A-Za-z0-9\.\_\-]+", info)
        telegram_persons = list(set(telegram_persons))
        telegram_persons_result = []
        # 如果是邮箱的后半段以及字符串太长的数据需要排除掉
        for _ in telegram_persons:
            if _.endswith('com') or len(_) >= 30:
                continue
            else:
                telegram_persons_result.append(_)
        return telegram_persons_result

    def extract_token(self, info):
        """ 提取地址信息 代币不涉及btc地址，这里规则不包含btc地址提取规则 """
        # eth or bsc上都是以0x开头
        token_address01 = re.findall(r"0x[A-Fa-f0-9\.]+", info)
        token_address01 = [_ for _ in token_address01 if len(_) == 42 or '..' in _]
        # tron 上面地址都是以T开头
        token_address02 = re.findall(r"T[A-Fa-f0-9\.]+", info)
        token_address02 = [_ for _ in token_address02 if len(_) == 34 or '..' in _]

        token_address012 = token_address01 + token_address02
        token_address012 = list(set(token_address012))
        return token_address012

    def extract_time(self, info):
        """ 抽取文本涉及时间信息：默认以年开头的数据有效 """
        """ 抽取文本涉及时间信息：默认以年开头的数据有效 """
        time_list0 = re.findall(r"[0-9\-\.\/\年\月]+202+", info)
        time_list1 = re.findall(r"202[0-9\-\.\/\年\月]+", info)
        time_list2 = re.findall(r"[0-9\-\.\/\年\月]+", info)
        time_list = time_list0 + time_list1 + time_list2

        time_list = [re.sub('[./\年\月\日]', '-', _) for _ in time_list]
        time_list = [_.strip('-,') for _ in time_list]
        time_list_result = []
        for date in time_list:
            try:
                date_split = date.split('-')
                if len(date_split) == 3:  # 2022-11-5
                    if len(date_split[0]) >= 3:
                        date_split[1] = date_split[1] if len(date_split[1]) >= 2 else '0' + date_split[1]
                        date_split[2] = date_split[2] if len(date_split[2]) >= 2 else '0' + date_split[2]
                        time_list_result.append('-'.join(date_split))
                    else:  # 11-5-2022
                        date_split[0] = date_split[0] if len(date_split[0]) >= 2 else '0' + date_split[0]
                        date_split[1] = date_split[1] if len(date_split[1]) >= 2 else '0' + date_split[1]
                        date_split_new = [date_split[2], date_split[0], date_split[1]]
                        time_list_result.append('-'.join(date_split_new))
                if len(date_split) == 2:  # 5-7
                    if int(date_split[0]) <= 12:
                        date_split[0] = '0' + date_split[0] if len(date_split[0]) == 1 else date_split[0]
                        date_split[1] = '0' + date_split[1] if len(date_split[1]) == 1 else date_split[1]
                        date_split_new = [date_split[0], date_split[1]]
                        time_list_result.append('-'.join(date_split_new))
                    else:
                        continue
            except:
                time_list_result.append(date)
        time_list_result = list(set(time_list_result))
        # 去掉重复的年份数据
        if len(time_list_result) >= 2:
            try:
                if '2022-' in time_list_result:
                    time_list_result.remove('2022-')
                elif '2022' in time_list_result:
                    time_list_result.remove('2022')
            except:
                pass
        try:
            time_list_result.remove('-')
        except:
            pass
        return time_list_result


    def extract_chain(self, info):
        """ 识别文本涉及的货币链 """
        bsc_words = '|'.join(['BSC', 'bsc', '币安', 'bnb', 'BNB', 'pancake'])
        eth_words = '|'.join(['ETH', 'eth', '以太'])
        tron_words = '|'.join(['TRON', 'tron', '波场'])
        block_chain_result = []
        if len(re.findall(bsc_words, info)) >= 1:
            block_chain_result.append('bsc')
        if len(re.findall(eth_words, info)) >= 1:
            block_chain_result.append('eth')
        if len(re.findall(tron_words, info)) >= 1:
            block_chain_result.append('tron')
        return block_chain_result

    def extract_qq_number(self, info):
        qq_words = '|'.join(['QQ', 'qq', '扣扣'])
        qq_number = []
        if len(re.findall(qq_words, info)) >= 1:
            qq_number = re.findall(r'[0-9]+\d{8}', info)
        else:
            pass
        qq_number = [_ for _ in qq_number if len(_) in [9, 10]]
        return qq_number

    def extract_project_name(self, info):
        """ 项目名称抽取 """
        high_frequency_words_lower = [_.lower() for _ in high_frequency_words]
        high_frequency_words_upper = [_.upper() for _ in high_frequency_words]
        high_frequency_words_title = [_.title() for _ in high_frequency_words]

        high_frequency_words_all = high_frequency_words_lower + high_frequency_words_upper + \
                                   high_frequency_words_title + other_words
        may_project_name = re.findall(r"[a-zA-Z][a-zA-Z\d\_\ ]+", info)  # +表示多匹配，不限制长度
        project_name = [name.strip('()[]\ ') for name in may_project_name if
                        3 <= len(name.strip('()[]\ ')) <= 20 and len(re.findall(r'[0-9]', name)) == 0]
        project_name_result = list(set(project_name) - set(high_frequency_words_all))  # 去掉高频词
        project_name_result01 = []
        # 项目名称不能是telegram_person
        telegram_persons_result = self.extract_telegram_person(info)
        for name in project_name_result:
            if '@' + name not in telegram_persons_result:
                project_name_result01.append(name)

        return project_name_result01

    def extract_project_type(self, info):
        """ 项目类别抽取"""
        wallet_words = '|'.join(['钱包', 'wallet', 'IMtoken'])
        kongtou_words = '|'.join(['空投', 'Airdrop', 'airdrop'])
        token_words = '|'.join(['代币', 'token'])
        project_type_list = []
        if len(re.findall(wallet_words, info)) >= 1:
            project_type_list.append('钱包')
        if len(re.findall(kongtou_words, info)) >= 1:
            project_type_list.append('空投')
        if len(re.findall(token_words, info)) >= 1:
            project_type_list.append('代币')
        return project_type_list

    def isNone(self, d):
        try:
            if (str(d) == '\n' or str(d) == 'NULL' or str(d) == 'None' or
                    str(d) == 'null' or str(d) == 'nan'):
                return True
        except:
            if not d:
                return True
        if isinstance(d, str):
            if d == 'None' or d == '?' or d == '' or d == 'NaN':
                return True
            elif len(d) > 0:
                return False
        elif isinstance(d, list) or isinstance(d, tuple) or isinstance(d, dict):
            if d.__len__() < 1:
                return True
        elif isinstance(d, int):
            return False
        elif d:
            return False
        else:
            return True

if __name__ == "__main__":
    print('跑历史全量数据...')
    ExtractTelegraminfo().get_full_result()
    # print('单条增量数据解析...')
    print(ExtractTelegraminfo().get_increase_result('text_info'))
