# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from ..items import BookItem
from scrapy.loader import ItemLoader
"""
    title = scrapy.Field()
    author = scrapy.Field()
    size = scrapy.Field()
    update = scrapy.Field()
    size = scrapy.Field()
    introduction = scrapy.Field()
    url = scrapy.Field()
"""
class ExampleSpider(scrapy.Spider):
    name = 'xqishu'
    #allowed_domains = ['example.com']
    start_urls = ['http://m.xqishu.com/newbook/']

    def parse(self, response):
        baseurl = 'http://m.xqishu.com'

        lista = response.xpath("//ul[@class='book_list']/li")
        for a in lista:
            book = BookItem()
            title = a.xpath(".//p[@class='book_title']/text()").extract()[0]
            author = a.xpath(".//a/p[2]/text()").extract()[0].replace("作者：","")
            size = a.xpath(".//a/p[3]/text()").extract()[0].replace("大小：","")
            update = a.xpath(".//a/p[4]/text()").extract()[0].replace("更新：","")
            introduction = a.xpath(".//a/p[5]/text()").extract()[0].replace("简介：","")
            url = baseurl+a.xpath(".//a/@href").extract()[0]
            print("book",title,author,size,update,introduction,url)
            book['title'] = title
            book['author'] = author
            book['size'] = size
            book['update'] = update
            book['introduction'] = introduction
            book['url'] = url
            yield book

        next = response.xpath("//a[@id='pt_next']/@href").extract()
        if next:
            nexturl = baseurl+next[0]
            print("next url:",nexturl)
            yield Request(nexturl,callback=self.parse)
        pass