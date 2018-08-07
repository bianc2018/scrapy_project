# -*- coding: utf-8 -*-
import scrapy
from ..items import urlItem
from scrapy import Request
#https://movie.douban.com/top250
import re
class ExampleSpider(scrapy.Spider):
    name = 'getProxy'
    #allowed_domains = ['example.com']
    start_urls = ['http://www.66ip.cn/mo.php?sxb=&tqsl=50&port=&export=&ktip=&sxa=&submit=%CC%E1++%C8%A1&textarea=']

    def parse(self, response):
        test = "https://httpbin.org/ip"
        proxys = re.findall(r'(\d+\.\d+\.\d+\.\d+:\d+)<br />',response.text)
        print(f'proxys:{len(proxys)}')
        for proxy in proxys:
            #print("get"+proxy)
            yield Request(test,callback=self.test,meta={'proxy':f'http://{proxy}'},dont_filter = True,)
    def test(self,response):
        proxy = re.findall(r'(\d+\.\d+\.\d+\.\d+)', response.meta['proxy'])[0]
        rproxy = re.findall(r'"(\d+\.\d+\.\d+\.\d+)"', response.text)[0]
        print(f'proxy:{proxy}\nrproxy:{rproxy}')
        if proxy == rproxy:
            item = urlItem()
            item['url'] = response.meta['proxy']
            yield item
        pass