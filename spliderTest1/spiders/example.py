# -*- coding: utf-8 -*-
import scrapy

#https://movie.douban.com/top250
class ExampleSpider(scrapy.Spider):
    name = 'example'
    #allowed_domains = ['example.com']
    start_urls = ['https://httpbin.org/ip']

    def parse(self, response):
        print("执行：")
        print(response.text)
        pass
