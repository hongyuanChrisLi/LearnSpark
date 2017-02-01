from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from crawler.core.spiders import blog_spider
import pref.setting as pref
import json


class PageRank:

    def __init__(self):
        data_dir = pref.get_env_variable('SPARK_DATA')
        self.file_dir = data_dir + '/blog_links.json'
        self.settings = get_project_settings()
        self.settings.set('FEED_FORMAT', 'json')
        self.settings.set('FEED_URI', self.file_dir)
        self.settings.set('LOG_LEVEL', 'INFO')
        self.json_data = []

    def __craw_blog(self):
        process = CrawlerProcess(self.settings)
        process.crawl(blog_spider.BlogSpider)
        process.start()

    def __read_json(self):
        for line in open(self.file_dir, 'r'):
            # remove '[', ']' and extra ','
            # JSON file contains multiple lists
            if not(line.startswith(('[', ']'))):
                self.json_data.append(json.loads(line.rstrip('\n,')))
        print(self.json_data)

    def get_report(self):
        self.__craw_blog()
        self.__read_json()

# Main
PageRank().get_report()
