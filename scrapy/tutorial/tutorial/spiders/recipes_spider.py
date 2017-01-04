import scrapy
# This is for exercise

class QuotesSpider(scrapy.Spider):
    name = "recipes"

    def start_requests(self):
        urls = [
            'http://allrecipes.com/recipe/13116/cabbage-fat-burning-soup'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for ingred in response.xpath('//span[@class="recipe-ingred_txt added"]/text()' ).extract():
            print (ingred)
