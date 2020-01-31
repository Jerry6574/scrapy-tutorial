# -*- coding: utf-8 -*-
import scrapy
import subprocess

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        title = response.css('title::text').extract()
        yield {"title": title}


path = r"C:\Users\wujun\OneDrive\Desktop\ScrapyTutorial\tutorial"
subprocess.run("cd {0}".format(path), shell=True)
subprocess.run("scrapy crawl quotes", shell=True)

