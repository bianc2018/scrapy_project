# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy import FormRequest
from ..items import Image
import json
import re
dicts = {'w':'a','k':'b','v':'c','1':'d','j':'e','u':'f','2':'g','i':'h','t':'i','3':'j','h':'k','s':'l','4':'m','g':'n',\
         '5':'o','r':'p','q':'q','6':'r','f':'s','p':'t','7':'u','e':'v','o':'w','8':'1','d':'2','n':'3','9':'4','c':'5',\
         'm':'6','0':'7','b':'8','l':'9','a':'0','_z2C$q':':','_z&e3B':'.','AzdH3F':'/'}
class ExampleSpider(scrapy.Spider):
    name = 'BaiduImage'
    #allowed_domains = ['example.com']
    #start_urls = ['https://github.com/login']
    imagejson = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&queryWord=%s&word=%s&pn=%d'
    imagenum = 30
    maxnum = 30000
    keywordlist = ['佐天泪子','御坂美琴','美女','动漫美女','魔法禁书目录',"元气","少女","伪恋","亚丝娜"]
    keyword = "佐天泪子"
    request_num = 30
    its = 0
    q = 0
    def start_requests(self):
        for self.keyword in self.keywordlist:
            self.request_num = 30
            self.q = 0
            while True:
                url = self.imagejson%(self.keyword,self.keyword,self.request_num)
                yield Request(url,callback=self.parse,dont_filter=True)
                self.request_num+=self.imagenum
                if self.request_num>=self.maxnum or self.q==1:
                    break

    def parse(self, response):
        images = json.loads(response.text,strict=False)['data']

        if len(images)==1:
            self.q = 1

        for image in images:
            try:
                if len(image)==0:
                    break
                objitem = Image()
                middleitem = Image()
                hoveritem = Image()

                objurl = self.convertObjURL(image['objURL'])
                objpath = self.keyword+'/'+str(self.its)+'/'+'obj'+'/'+str(self.its)+"obj.jpg"
                if objurl != "":
                    print("objURL",objpath,objurl)
                    objitem['IMG_URL'] = [objurl]
                    objitem['IMG_PATH'] = objpath
                    yield objitem

                middleurl = image['middleURL']
                middlepath = self.keyword + '/' + str(self.its) + '/' +'middle'+'/'+ str(self.its) + "middle.jpg"
                if middleurl != "":
                    print("middleURL", objpath, objurl)
                    middleitem['IMG_URL'] = [middleurl]
                    middleitem['IMG_PATH'] = middlepath
                    yield middleitem

                hoverurl = image['hoverURL']
                hoverpath = self.keyword + '/' + str(self.its) + '/' +'hover'+'/'+str(self.its) + "hover.jpg"
                if hoverurl!="":
                    print("hoverURL", objpath, objurl)
                    hoveritem['IMG_URL'] = [hoverurl]
                    hoveritem['IMG_PATH'] = hoverpath
                    yield hoveritem

                self.its += 1
                print("获得item数量：", self.its, self.request_num)
            except Exception as e:
                print("发生错误：",str(e))

    def convertObjURL(self,objURL):
        url = ""
        size = len(objURL)
        i=0
        while i<size:
            ch = objURL[i]
            if ch =='_' or ch=='A':
                ch = objURL[i:i+6]
                #print(ch)
                i+=6
            else:
                i+=1
            if ch not in dicts.keys():
                url+=ch
            else:
                url += dicts[ch]
        return url
