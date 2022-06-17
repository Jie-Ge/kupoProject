import redis
import os
from os import path
import pandas as pd

r = redis.Redis('192.168.224.72', port=6379, db=3, password='123456')

def ocr(image_list):
    global urls, contents
    '''
    收款人、收款户名、对方户名、收款人名称、收款方、收款人姓名

    收款账号、对方账户、对方账户名称、收款卡号、收款账户
    '6217 米米/米米米 8242'、6230521190061458671、6235**********5183、'对方账户:  余忠甫6228****2978'、
    '余忠甫 6228***2978'、6230 *****x  8671、6230**4170

    收款银行、开户行、收款银行开户、收款行、对方账户行别、收款开户行、收款行名
    中国农业银行、黑龙江农村信用社、'收款银行开户 中国农业银行'、中国邮政储蓄银行
    :return:
    '''
    aa = ['https://legacy-pics.meiqiausercontent.com/images/347754/Ytpu/olsFKapvUgDqa4KwNZ3a.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/L6Jd/3LLxIjPTDkKbhYjrFMuu.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/tHr4/IPWKfrU0zv6DbIvdkfSn.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/Pr29/MrL5BWjK1Jn5Z1D7GGq8.png',
          'https://legacy-pics.meiqiausercontent.com/images/347754/dS24/8o0KSrUffkHBWbIBxbXY.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/s25u/NucnrV5rcOVc7oSW1mDv.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/2VYL/VRQ6FN2OBSBI94OFYD2L.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/SOUl/P41NWyQrjYShlryFyqDK.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/ZIx0/nmMXNhXSoWtbWgX56n6z.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/R6jt/3ROENXGHGUgLN962l06j.png',
          'https://legacy-pics.meiqiausercontent.com/images/347754/Om1n/qWwKmZcn1cXfU2Huo5Wa.png',
          'https://legacy-pics.meiqiausercontent.com/images/347754/PUky/erxmwyE38V2Bu4naeq3e.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/dbxO/ptJvPDOj9OzDfEYu2xQT.png',
          'https://legacy-pics.meiqiausercontent.com/images/347754/C6TT/DevR5rFhsR5qwm5ymka4.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/3ema/v9yvoyj3ZccoAoH0qCpx.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/hhAu/pDaxFYOMicrM9oEig0ex.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/coT2/o1qmvgW6HS1RGVTEmVdv.png',
          'https://legacy-pics.meiqiausercontent.com/images/347754/rTD3/gXbVYo71VgeFFJFa72S1.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/n0Qq/nMX5rPKEXRMZZfXjr5GZ.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/QPKP/h3yKZHN1J2KXOEssyfIZ.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/MSBg/kFeMTfkZpm31kbWdnmAU.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/CHAq/ShVlSAgrvvfApW3f3W24.png',
          'https://legacy-pics.meiqiausercontent.com/images/347754/rVAO/ecH2pgMH5Cy6ZHY7oG2F.png',
          'https://legacy-pics.meiqiausercontent.com/images/347754/cJKo/E61fxvXDILuDvaUYvlSp.png',
          'https://legacy-pics.meiqiausercontent.com/images/347754/1Yiw/yQFSDGpLyTdNGWGhegaA.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/egu1/7BmcTHuerbJoNOnCVImn.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/ENWh/QwuxowAwPxe2gSRdmhnl.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/UGSu/Y0Vlr2AEy7XtPkW0Uuvq.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/o5D3/eZcKjrdEAV4XkV5u1GE0.png',
          'https://legacy-pics.meiqiausercontent.com/images/347754/xBRX/c10rjJQ7CnA1zOlCMfjU.png',
          'https://legacy-pics.meiqiausercontent.com/images/347754/S3nb/gNePsl0GoLo5KwJNv6Ii.png',
          'https://legacy-pics.meiqiausercontent.com/images/347754/gdHx/0UwsYLK7YxYJQAA98qwo.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/pWdT/wweZalZQZ02Sw4qcdyzK.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/yk2Q/UjfXij62EaqbwObEAQmO.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/ukTA/zETRN8uzOXMUHSQg5nqi.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/VZi1/JCaEzDEP7N8UxwEhImWB.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/2dlO/YYLWpjGk8m7rqE4Kr9zr.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/irvG/Gv16aCCYJoM0MhVGegah.png',
          'https://legacy-pics.meiqiausercontent.com/images/347754/U7C8/ZGQx00pXQEuDFCw2nsSe.png',
          'https://legacy-pics.meiqiausercontent.com/images/347754/rsaz/LJoZvQCtOacKbLo8yR1N.png',
          'https://legacy-pics.meiqiausercontent.com/images/347754/1DEy/yJea9287cJHqXLN0gVts.png',
          'https://legacy-pics.meiqiausercontent.com/images/347754/Dfkj/YARUDstuR45xnLozb67X.png',
          'https://legacy-pics.meiqiausercontent.com/images/347754/EAZE/YxD5nrY0Slt3sQ7utk50.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/mOJj/mnDYjXmRD1bTw3GBcHtD.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/Gil9/spNxqrvzrOVHfZhkEEzE.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/h5j5/ZOG11rwExsjEoODT4dub.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/MHEU/D5YnjyzGTTKT7u6iNzKT.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/hoe9/QTEvmKYCB5YRpOp9Og8z.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/03Sx/KPxqkYo1L9YZ3faWUdiQ.png',
          'https://legacy-pics.meiqiausercontent.com/images/347754/qajw/vknJ7CUVTMSsM1k5VWKV.png',
          'https://legacy-pics.meiqiausercontent.com/images/347754/n3TV/7ySTiK2Wz4SPUhaswewO.png',
          'https://legacy-pics.meiqiausercontent.com/images/347754/8ZAo/iu5JlZ3olrtdnBus7mRf.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/eZVT/vwikTzdbMExMVsrxXgbc.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/YfOS/18FKaZmv24bnQ8uWbHbT.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/swXe/VpExcqXcA47g7jmLvuWN.png',
          'https://legacy-pics.meiqiausercontent.com/images/347754/g4UJ/tiZ5meJFyhxQuoM6YDmM.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/ohe3/6gnfF0UHIASC4w1X6krk.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/ID6V/KOK7tEK4353PVPKAWlK7.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/kSmH/CAk0P4dyuG5ye60sKX1l.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/zp5j/oXJVONJgVG9zOXhyfPTC.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/5AGQ/ylYL4bEFS3H9ODZ7o1mU.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/Soij/8EIxpH3JEne7kNxdMgvZ.png',
          'https://legacy-pics.meiqiausercontent.com/images/347754/QL7f/dUMjTW9GTE1HxT9scEpA.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/LYoj/iSvkzzgN8YWnD9KprPLe.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/r9lO/S7EnHaS7K8a4du7Usntz.png',
          'https://legacy-pics.meiqiausercontent.com/images/347754/NdXr/a1AYLhcihAqRfJcZhB8b.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/pyVI/qLQntm7QxCWuf6Jsrfbq.png',
          'https://legacy-pics.meiqiausercontent.com/images/347754/NHHJ/8bOwMT8NpNULHIm7Io1g.png',
          'https://legacy-pics.meiqiausercontent.com/images/347754/AfbF/2hTgH6tFas7GhcVDZKJE.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/2Ujp/zBMMbkYS8gAVuuGdKEwx.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/8WGD/neT4QkgRgnBMuzNsHx7E.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/TOYH/fXeGxSfDJ0eirjvTtiva.png',
          'https://legacy-pics.meiqiausercontent.com/images/347754/io0F/O350WV6BZmvcc6rYQMFt.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/0eM6/jnQMid6dwivEHQ4BY3Yn.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/5otf/1TPntJui5McAF7GxQuNN.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/7HkF/YIXWCmdkVK1fGoN6R14t.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/6KZ6/DnMJ1dggeDiJUAEzvyMt.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/boq0/2pg4gTU0Xsxe4QcwoKQF.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/cXNb/KxlJPvdor4mIeRRHXqT5.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/Odrj/cGce1wgpb5qkKCnB4MaR.png',
          'https://legacy-pics.meiqiausercontent.com/images/347754/Rw0c/ZsMtoBAfOAm1FuDhwBbJ.png',
          'https://legacy-pics.meiqiausercontent.com/images/347754/cLtV/9f5xbfRJ6eD8903sH0od.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/vS4x/Ujj3TRdzQmW4EnMs6AV0.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/b7Wp/njVKR3Pjwxbt7GfG0zAM.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/ACNQ/h22Ft4AQ5xIWwKF0xgRh.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/KPqJ/2rZ1LRNQtLaJZgY1XeO7.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/4Pf2/fcUDAJJMXlGqaILqqq1h.png',
          'https://legacy-pics.meiqiausercontent.com/images/347754/mxA7/xQUjTRgp0ZpzhpCNdbFt.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/c72y/kdN8qbpujDUaDU7rZayo.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/HSOW/bfBfavSqzLSie3O6221w.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/0hhG/1R9Icugf2xsTuwYMujKy.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/WbsX/lkz2ufC6KV4TLhVyTfqM.png',
          'https://legacy-pics.meiqiausercontent.com/images/347754/ptOP/28QSGMRkXU33oTofB1Ze.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/j7Lx/30DnRPC4uk5OdVK1StN7.png',
          'https://legacy-pics.meiqiausercontent.com/images/347754/HRDX/uEG6E6YXXRGFZMMQ9bOT.png',
          'https://legacy-pics.meiqiausercontent.com/images/347754/qrt1/DYaaUic8sJP6IapNH1ey.png',
          'https://legacy-pics.meiqiausercontent.com/images/347754/hsg1/wwseHVoDchTwh8HzK8RF.png',
          'https://legacy-pics.meiqiausercontent.com/images/347754/3pmX/Fzn0uYUNg7U3ZoWz9pt8.jpg',
          'https://legacy-pics.meiqiausercontent.com/images/347754/AOKF/uCsQguObzaLKnsnBqQFe.png',
          'https://legacy-pics.meiqiausercontent.com/images/347754/fiML/ferZbqsfRPsvdCwrO6QG.jpg']
    # url = 'https://legacy-pics.meiqiausercontent.com/images/347754/krnw/cnOcoHOkNT8jSQIW6dPx.jpg'
    # url = 'https://legacy-pics.meiqiausercontent.com/images/347754/85w5/aN9yz4eTVmj5r269p4eC.jpg'
    # url = 'https://legacy-pics.meiqiausercontent.com/images/347754/JnfU/knO6dBLZYhaaRGf4qZOw.jpg'
    for url in image_list:
        if url in aa:
            continue
        print('url: ', url)
        r.sadd('image_url', url)

def get_image_url(abs_path, folder_name):
    global urls, contents
    urls = []
    contents = []

    df = pd.read_excel(abs_path)
    image_df = df[df['消息内容'].str.startswith('http') & df['消息内容'].str.match('.*\\.(jpg|png)')]
    image_list = image_df['消息内容'].tolist()

    ocr(image_list)

def scaner_file(url, folder_name):
    '''
    遍历文件夹中的文件
    '''
    file = os.listdir(url)
    for f in file:
        real_url = path.join(url, f)
        if path.isfile(real_url):
            # 如果是文件，则以绝度路径的方式输出
            abs_path = path.abspath(real_url)
            # if 'support-sys-历史对话_347754_2022-03-20_2022-04-01' in abs_path and
            print('abs_path: ', abs_path)
            get_image_url(abs_path, folder_name)
        elif path.isdir(real_url):
            # 如果是目录，则是递归调用自定义函数 scaner_file (url)进行多次
            scaner_file(real_url, folder_name)
        else:
            print("其他情况")
            pass


def main():
    ll = [
        # 'C:/Users/Administrator/Desktop/情报数据《金沙彩票》',
          'C:/Users/Administrator/Desktop/情报数据《84棋牌》',
          'C:/Users/Administrator/Desktop/情报数据《668娱乐》'
    ]
    for p in ll:
        scaner_file(p, p.split('/')[-1])



if __name__ == '__main__':
    main()
