import scrapy
import re


class BlogSpider(scrapy.Spider):
    name = "blog"
    link_dict = {}

    def start_requests(self):
        url = 'https://speedy-elephant.blogspot.com/'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        link_set = self.get_link_set(response)

        for href in link_set:
            yield scrapy.Request(url = href, callback=self.build_hash)

    def build_hash(self, response):

        my_link = response.url
        links = self.get_link_set(response)
        link_count = len(links)

        for href in links:
            if href != my_link:
                self.link_dict[(href, my_link)] = link_count
        # print (my_link + " : " + str(len(links)))
        # for k, v in link_dict.items():
        #     print ("From: " + k[0])
        #     print ("To: " + k[1])
        #     print ("Total: " + str(v))

    def get_link_set(self, response):
        links = response.xpath('//a/@href').extract()
        regex = re.compile(r'speedy-elephant')
        sel_links = filter(regex.search, links)
        cln_links = [i.split('#', 1)[0] for i in sel_links]

        return cln_links

    def get_link_dict(self):
        return self.link_dict
