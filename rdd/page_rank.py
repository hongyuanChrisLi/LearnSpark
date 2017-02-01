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
        self.links_dict = {}
        self.link_cnt_dict = {}

    def __craw_blog(self):
        process = CrawlerProcess(self.settings)
        process.crawl(blog_spider.BlogSpider)
        process.start()

    def __read_json(self):
        for line in open(self.file_dir, 'r'):
            # remove '[', ']' and extra ','
            # JSON file contains multiple lists
            if not(line.startswith(('[', ']'))):
                # self.json_data.append(json.loads(line.rstrip('\n,')))
                self.__parse_json(json.loads(line.rstrip('\n,')))
        print(self.link_cnt_dict)
        # print(self.json_data)

    def __parse_json(self, entry):
        if 'to_link' in entry:
            to_links = entry['to_link']
            from_link = entry['from_link'][0]
            print(from_link)
            for link in to_links:
                if link in self.links_dict:
                    self.links_dict[link].add(from_link)
                else:
                    from_list = [from_link]
                    self.links_dict[link] = set(from_list)

            self.link_cnt_dict[from_link] = entry['count'][0]

    def get_report(self):
        self.__craw_blog()
        self.__read_json()

# Main
PageRank().get_report()
