import scrapy
import os


class RecipesFinderSpider (scrapy.Spider):

    name = "recipes_finder"
    f = open(os.path.join(os.path.expanduser('~'), 'Data/LearnSpark/recipes.dat'), 'wb')

    def start_requests(self):
        url = 'http://allrecipes.com/recipes'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        recipe_hrefs = response.xpath('//section/article/a/@href').extract();

        for href in recipe_hrefs:
            yield scrapy.Request (response.urljoin(href), callback=self.parse_recipe)
        # self.f.close()

    def parse_recipe(self, response):

        title = response.xpath('//title/text()').extract_first()
        self.f.write(title + ' :\n')

        for ingred in response.xpath('//span[@class="recipe-ingred_txt added"]/text()').extract():
            self.f.write(ingred + '\n')
        self.f.write('\n')
