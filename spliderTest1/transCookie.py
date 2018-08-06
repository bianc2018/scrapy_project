# -*- coding: utf-8 -*-
class transCookie:
    def __init__(self, cookie):
        self.cookie = cookie

    def stringToDict(self):
        '''
        将从浏览器上Copy来的cookie字符串转化为Scrapy能使用的Dict
        :return:
        '''
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict

if __name__ == "__main__":
    cookie = 'iewed="5916655"; bid=sxoYd31rfH8; _vwo_uuid_v2=DA38E9D9B0C11C3EEA5C5A973C17A83F4|dc9f8263ec3b4944f8bd97af2ed04885; gr_user_id=26eb5adc-d6b4-4f2a-97f4-c82725df3f29; __yadk_uid=mu6tlLc5zSHv0ogJothlqwZ6YTKYSJ8v; ll="118281"; __utmz=30149280.1533095431.4.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=223695111.1533095431.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=30149280.1184233981.1521450513.1533133666.1533140040.6; __utma=223695111.2112733825.1533095431.1533133669.1533140040.3; ps=y; dbcl2="182166527:sEnCAQfLcBQ"; ck=b6qq; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1533185465%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DPQiSofMCHC-Pj236PVJVrCEcpSX03DNgp59OpISM1vie10m0uPQr3pJRzNWFbp_s%26wd%3D%26eqid%3Ddb174b8900029121000000065b628ecc%22%5D; _pk_ses.100001.4cf6=*; push_noty_num=0; push_doumail_num=0; _pk_id.100001.4cf6=bc8fc8331afca7d0.1533047656.6.1533187062.1533140039.'
    trans = transCookie(cookie)
    print(trans.stringToDict())