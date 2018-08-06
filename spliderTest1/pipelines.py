# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

class Splidertest1Pipeline(object):
    def __init__(self,fpath):
        self.fpath = fpath
        print(self.fpath)
    def open_spider(self,spider):
        print("call open_spider")
        self.save = open(self.fpath,"w",encoding='utf-8')
    def close_spider(self,spider):
        print("call close_spider")
        self.save.close()
    def process_item(self, item, spider):
        print("call process_item")
        self.save.writelines(item['mName'])
        self.save.write('\n')
        return item
    @classmethod
    def from_crawler(cls,crawler):
        print("call from_crawler")
        return cls(fpath = crawler.settings.get('TXTPATH'))

class doubanPipeline(object):
    def __init__(self,fpath):
        self.fpath = fpath
        print(self.fpath)
    def open_spider(self,spider):
        print("call open_spider")
        self.save = open(self.fpath,"w",encoding='utf-8')
    def close_spider(self,spider):
        print("call close_spider")
        self.save.close()
    def process_item(self, item, spider):
        print("call process_item")
        self.save.writelines(item['name']+" "+item['score']+" "+item['about'])
        self.save.write('\n')
        return item
    @classmethod
    def from_crawler(cls,crawler):
        print("call from_crawler")
        return cls(fpath = crawler.settings.get('DOUBAN'))

    """
        title = scrapy.Field()
        author = scrapy.Field()
        size = scrapy.Field()
        update = scrapy.Field()
        introduction = scrapy.Field()
        url = scrapy.Field()
    """
    #create table book(title char(128),author char(20),size char(10),updatetime char(30),introduction char(128),url char(50));
insert ="insert into book(title,author,size,updatetime,introduction,url) values('%s','%s','%s','%s','%s','%s')"
import pymysql as sql
class bookPipeline(object):
    def open_spider(self,spider):
        print("call open_spider")
        self.db = sql.connect(host="localhost",user="root",password="44532f",db="xqishu")
        self.cur = self.db.cursor()
        self.save = open("./xqishu","w",encoding='utf-8')
    def close_spider(self,spider):
        print("call close_spider")
        self.db.commit()
        self.db.close()
        self.save.close()
    def process_item(self, item, spider):
        print("call process_item")
        print("insert"+insert%(item['title'],item['author'],item['size'],item['update'],item['introduction'],item['url']))
        self.save.writelines(item['title']+" "+item['author']+" "+item['size']+" "+item['update']+" "+item['introduction']+" "+item['url'])
        self.cur.execute(insert%(item['title'],item['author'],item['size'],item['update'],item['introduction'],item['url']))
        self.save.write('\n')
        return item



class ProxyPipeline(object):
    def open_spider(self,spider):
        print("call open_spider")
        self.save = open('./proxy.txt',"w",encoding='utf-8')
        self.proxys = []
    def close_spider(self,spider):
        print("call close_spider")
        self.save.writelines(str(self.proxys))
        self.save.close()
    def process_item(self, item, spider):
        url = item['url']
        print(url)
        self.proxys.append(url)
        self.save.writelines(url)
        self.save.write('\n')
        return item

from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
class BaiDuImage(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        #print("path"+request.meta['path'])
        return request.meta.get('path', '')

    def get_media_requests(self, item, info):
        img_url = item['IMG_URL'][0]
        meta = {'path': item['IMG_PATH']}
        yield Request(url=img_url, meta=meta)
