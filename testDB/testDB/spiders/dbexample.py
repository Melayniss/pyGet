# -*- coding: utf-8 -*-
import scrapy


class DbexampleSpider(scrapy.Spider):
    name = 'dbexample'
    allowed_domains = ['douban.com']
    start_urls = ['http://douban.com/']

    def parse(self, response):
        pass
