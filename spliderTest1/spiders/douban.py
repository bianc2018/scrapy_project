# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from ..items import MovieItem
from scrapy.loader import ItemLoader
#https://movie.douban.com/top250
#{'iewed': '"5916655"', 'bid': 'sxoYd31rfH8', '_vwo_uuid_v2': 'DA38E9D9B0C11C3EEA5C5A973C17A83F4|dc9f8263ec3b4944f8bd97af2ed04885', 'gr_user_id': '26eb5adc-d6b4-4f2a-97f4-c82725df3f29', '__yadk_uid': 'mu6tlLc5zSHv0ogJothlqwZ6YTKYSJ8v', 'll': '"118281"', '__utmz': '223695111.1533095431.1.1.utmcsr', '__utma': '223695111.2112733825.1533095431.1533133669.1533140040.3', 'ps': 'y', 'dbcl2': '"182166527:sEnCAQfLcBQ"', 'ck': 'b6qq', '_pk_ref.100001.4cf6': '%5B%22%22%2C%22%22%2C1533185465%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DPQiSofMCHC-Pj236PVJVrCEcpSX03DNgp59OpISM1vie10m0uPQr3pJRzNWFbp_s%26wd%3D%26eqid%3Ddb174b8900029121000000065b628ecc%22%5D', '_pk_ses.100001.4cf6': '*', 'push_noty_num': '0', 'push_doumail_num': '0', '_pk_id.100001.4cf6': 'bc8fc8331afca7d0.1533047656.6.1533187062.1533140039.'}
class ExampleSpider(scrapy.Spider):
    name = 'douban'
    #allowed_domains = ['example.com']
    start_urls = ['https://movie.douban.com/top250']
    cookie = {'iewed': '"5916655"', 'bid': 'sxoYd31rfH8', '_vwo_uuid_v2': 'DA38E9D9B0C11C3EEA5C5A973C17A83F4|dc9f8263ec3b4944f8bd97af2ed04885', 'gr_user_id': '26eb5adc-d6b4-4f2a-97f4-c82725df3f29', '__yadk_uid': 'mu6tlLc5zSHv0ogJothlqwZ6YTKYSJ8v', 'll': '"118281"', '__utmz': '223695111.1533095431.1.1.utmcsr', '__utma': '223695111.2112733825.1533095431.1533133669.1533140040.3', 'ps': 'y', 'dbcl2': '"182166527:sEnCAQfLcBQ"', 'ck': 'b6qq', '_pk_ref.100001.4cf6': '%5B%22%22%2C%22%22%2C1533185465%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DPQiSofMCHC-Pj236PVJVrCEcpSX03DNgp59OpISM1vie10m0uPQr3pJRzNWFbp_s%26wd%3D%26eqid%3Ddb174b8900029121000000065b628ecc%22%5D', '_pk_ses.100001.4cf6': '*', 'push_noty_num': '0', 'push_doumail_num': '0', '_pk_id.100001.4cf6': 'bc8fc8331afca7d0.1533047656.6.1533187062.1533140039'}
    headers = \
    {
        'Connection': 'keep - alive',  # 保持链接状态
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
    }
    # 对请求的返回进行处理的配置
    meta = \
    {
        'dont_redirect': True,  # 禁止网页重定向
        'handle_httpstatus_list': [301, 302]  # 对哪些异常返回进行处理
    }

    def parse(self, response):
        lista = response.xpath("//div[@class='hd']/a")
        baseurl = 'https://movie.douban.com/top250'
        for a in lista:
            print(a.xpath("span[1]/text()").extract(),a.xpath("@href").extract())
            abouturl = a.xpath("@href").extract()[0]
            print(abouturl)
            yield Request(abouturl,callback=self.about_parse,cookies=self.cookie,headers=self.headers,meta=self.meta)

        next = response.xpath("//span[@class='next']/a/@href").extract()
        if next:
            nexturl = baseurl+next[0]
            print("nexturl:",nexturl)
            yield Request(nexturl,callback=self.parse,cookies=self.cookie,headers=self.headers,meta=self.meta)
        pass
    def about_parse(self, response):
        # //*[@id="content"]/h1/span[1]
        name = response.xpath("//*[@id='content']/h1/span[1]/text()").extract()
        # //*[@id="interest_sectl"]/div[1]/div[2]/strong
        score = response.xpath("//*[@id='interest_sectl']/div[1]/div[2]/strong/text()").extract()
        # //*[@id="link-report"]/span[1]/span/text()[1]
        about = response.xpath("//*[@id='link-report']/span[1]/span/text()[1]").extract()

        print(name,score,about)
        item = MovieItem()
        item['name'] = self.gs(name)
        item['score'] = self.gs(score)
        item['about'] = self.gs(about)
        yield item

    def gs(self,i):
        if i==None or len(i)==0:
            return ""
        return i[0]
    #http://m.xqishu.com/newbook/