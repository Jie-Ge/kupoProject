# -*- coding: utf-8 -*-

import pandas as pd
from datetime import date, datetime, timedelta
from extract_telegram_info import ExtractTelegraminfo
from utils import insert_db_history
import json

item = {}
# 获取发言者信息

def en_decode(str01):
    return str(str01).replace('\'', '').replace('\001', '').replace('\002', '') \
        .replace(r'\0xa0', '').replace('\n', ' ').replace('\r', ' ') \
        .encode("utf-8", 'ignore').decode("utf-8", "ignore")

item['username'] = ""
item['first_name'] = en_decode("一起赚钱'")
item['last_name'] = '点我头像'


item['link'] = 'BDSCommunity'

date1 = (date.today()).strftime('%Y-%m-%d %H:%M:%S')  # xxxx-xx-xx 00:00:00, type: str
date2 = datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')





item['date_time'] = date2
# item['text_info'] = ''
item['text_info'] = en_decode("[\u200b](https://telegra.ph/file/25ba6bc9c4d31b566c81f.jpg)**TON 生态系统更新**\n\nTON 基金会一直在努力为生态系统参与者创造一个公平的去中心化生态。合作伙伴应在早期阶段获得募资、技术咨询以及营销等支持。 TON 基金会是一个非营利组织，因此能够提供捐款及技术咨询。我们非常重视所有参与者想要努力的方向，当前的众筹启动板和独立合作社都已正常运行。\n\n同时，TON 基金会综合开发人员和社群人员提出建议后，决定为孵化计划设立一些门槛：\n\n——该项目的团队在区块链行业中建立了良好的基础，内部开发人员积极推进技术的进步，偶尔也会与著名核心团队接触。\n\n在这种情况下，团队足够有经验，并希望孵化自己的项目，也有确定的目标。因此，加入一个合作社或将其想法提交给另一个团队管理的启动平台无法为生态系统做出更大的贡献。因此，Ton基金会必须激励这些团队实现他们的潜力，例如引进战略合作伙伴——头部交易所的风险投资公司，通过给团队配备合适的资源，帮助他们更进一步，如官方头衔。\n\n——该团队在孵化人才库方面拥有专业知识和经验，而不是构建项目，并希望通过举办黑客竞赛、开发培训项目和增加开发人员阵容，与经过正式审查的孵化合作伙伴合作。\n\n在这种情况下，团队需要确定生态系统中的孵化合作伙伴，并与之合作。由于他们不寻求构建独立的产品，因此不需要集中启动平台。此外，不筛选孵化合作伙伴的资质，可能会导致效率低下的结果。\n\n因此，Ton基金会将正式成立一个新的频道（详细说明）作为孵化合作伙伴和生态系统基金。新的频道将拥有独立网站，该网站将有开发者论坛、博客等。\n\n**名称是什么？**\n\n-孵化合作伙伴：建立团队，通过建立和孵化项目、引入战略合作伙伴或开展教育项目，帮助TON生态系统发展壮大。\n\n-生态系统基金：由一个或多个孵化伙伴组成的基金，用于孵化和投资新兴项目。基金将受到激励，并优先考虑生态系统增长相关基金，因为它们将以孵化目的持有 Toncoin 。\n\nTON 基金会将向生态系统基金提供赞助，以及孵化工作所产生的项目级募资。 此外，还可以提供技术咨询和制定即将出台的标准的机会。 在接下来的几天里，我们将跟进团队如何申请竞争计划以及官方频道和网站。 对于独立开发人员或较小的团队，通过 ton.org 或生态系统基金特定网页提交项目将提供连接到正确团队的机会（基于产品团队匹配度）。\n\n**生态系统基金启动**\n\n第一个 TON 生态系统基金将于 4 月 11 日在巴黎的 Terrasse de l'Alcazar 举行的发布会上宣布。 对于该地区的人，可以在 [此处](https://www.eventbrite.com/e/toncoinfund-launch-party-tickets-307167856327?aff=eemailordconf&utm_campaign=order_confirm&utm_medium=email&ref=eemailordconf&utm_source=eventbrite&utm_term=viewevent) 获得启动派对的门票。\n\n请继续关注更多激动人心的消息！")

result_info = {"telegram_group": "", "twitter_group": "", "urls": ["https://telegra.ph/file/25ba6bc9c4d31b566c81f.jpg)**TON", "https://www.eventbrite.com/e/toncoinfund-launch-party-tickets-307167856327?aff=eemailordconf&utm_campaign=order_confirm&utm_medium=email&ref=eemailordconf&utm_source=eventbrite&utm_term=viewevent"], "email": "", "telegram_person": "", "mobiles_in_china": "", "wechat": "", "token_address": "", "publish_time": "", "block_chain": "", "qq_number": "", "project_name": ["party", "org", "utm_source", "Ton", "file", "launch", "jpg", "TON", "Alcazar", "eemailordconf", "toncoinfund", "order_confirm", "tickets", "viewevent", "utm_medium", "utm_campaign", "Toncoin", "ton", "Terrasse de l", "ref", "telegra", "utm_term", "email", "eventbrite", "aff"], "project_type": ""}
result_info = json.dumps(result_info, ensure_ascii=False)
item['result'] = result_info

print(item)

# table_name = 'telegram_msg_01'
# # table_name = get_table_name()
# if table_name:
#     insert_db_history(item, table_name)

