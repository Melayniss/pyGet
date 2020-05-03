# -*- coding: utf-8 -*-
import scrapy


class DbdemoSpider(scrapy.Spider):
    name = 'dbdemo'
    # allowed_domains = ['douban.com']
    start_urls = ['http://douban.com/']

    def parse(self, response):
        fname = response.url.split('/')[-1]
        with open(fname, 'dbt') as f:
            f.write(response.body)
        self.log('Saved file %s.' % fname)
