# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy import FormRequest

class ExampleSpider(scrapy.Spider):
    name = 'githublogin'
    #allowed_domains = ['example.com']
    start_urls = ['https://github.com/login']
    login = "https://github.com/login"
    session = "https://github.com/session"
    def start_requests(self):
        yield Request(self.login,callback=self.parse)
    def parse(self, response):
        """
        commit:Sign in
        utf8:✓
        authenticity_token:5+c2UFL5NGqizHuzxKqEJw7AW/NgVfnK5sINaxJtojjlm8ElITTPwIgAclGYajHWzg/JJu42LnqxiXFgDlaFAw==
        login:bianc2018
        password:q1051576073
        """
        form = {'commit':None,'utf8':None,'authenticity_token':None}
        for key in form.keys():
            form[key] = response.xpath(f"//input[@name='{key}']/@value").extract()[0]
        form.update({'login':'bianc2018','password':'q1051576073'})
        #print("form:", form)
        yield FormRequest(self.session,formdata=form,callback=self.after)
        pass
    def after(self,response):
        print(response.xpath("//meta[@name = 'user-login']/@content").extract())
        pass