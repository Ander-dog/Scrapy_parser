import re

import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        pep_tags = response.css('#numerical-index').css('tbody > tr')
        for pep in pep_tags:
            link = pep.css('a::attr(href)').get()
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        page_title = response.css('h1.page-title::text').get()
        pattern = r'^PEP (?P<number>\d+) – (?P<title>.*)$'
        text_match = re.search(pattern, page_title)
        number, name = text_match.groups()
        dt_tags = response.css('dl > dt')
        for dt in dt_tags:
            if dt.css('dt::text').get() == 'Status':
                status = dt.css('dt + dd abbr::text').get()
                break
        data = {
            'number': number,
            'name': name,
            'status': status,
        }
        yield PepParseItem(data)
