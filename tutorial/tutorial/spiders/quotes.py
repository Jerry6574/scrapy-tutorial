# -*- coding: utf-8 -*-
import scrapy
from ..items import TutorialItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # title = response.css('title::text').extract_first()
        # next_page = response.css("li.next a").xpath("@href").extract_first()  # can combine css and xpath selectors

        items = TutorialItem()

        all_div_quotes = response.css('div.quote')
        for quote in all_div_quotes:
            title = quote.css('span.text::text').extract()
            author = quote.css('.author::text').extract()
            tag = quote.css(".tag::text").extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            yield items

# scrapy crawl quotes -o items.json
# scrapy crawl quotes -o items.csv
# scrapy crawl quotes -o items.xml