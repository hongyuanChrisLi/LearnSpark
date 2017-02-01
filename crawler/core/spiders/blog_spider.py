import re
import scrapy
from scrapy.loader import ItemLoader
from ..items import LinkCnx


class BlogSpider(scrapy.Spider):
    name = "blog"

    def start_requests(self):
        url = 'https://speedy-elephant.blogspot.com/'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        link_set = self.get_link_set(response)

        for href in link_set:
            yield scrapy.Request(url=href, callback=self.parse_each)

    def parse_each(self, response):
        l = ItemLoader(item=LinkCnx(), response=response)
        l.add_value('from_link', response.url)
        links = self.get_link_set(response)
        l.add_value('count', len(links) - 1)

        for href in links:
            if href != response.url:
                l.add_value('to_link', href)
        return l.load_item()

    def get_link_set(self, response):
        links = response.xpath('//a/@href').extract()
        regex = re.compile(r'speedy-elephant')
        sel_links = filter(regex.search, links)
        cln_links = [i.split('#', 1)[0] for i in sel_links]

        return cln_links
