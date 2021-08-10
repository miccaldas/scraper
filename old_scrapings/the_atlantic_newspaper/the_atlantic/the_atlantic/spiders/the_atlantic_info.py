import scrapy
from scrapy.shell import inspect_response


class TheAtlanticInfoSpider(scrapy.Spider):
    name = "the_atlantic_info"
    allowed_domains = ["theatlantic.com"]
    start_urls = ["https://www.theatlantic.com/magazine/archive/2021/09/twenty-years-gone-911-bobby-mcilvaine/619490//"]

    def parse(self, response):

        title = response.xpath('//*[@id="main-content"]/article/header/div[2]/h1/text()').extract()
        author = response.xpath('//*[@id="byline"]/a').extract()
        date_altered = response.xpath(
            '//*[@id="main-content"]/article/header/div[3]/time/attribute::datetime'
        ).extract()
        content = response.xpath('//*[@id="main-content"]/article/section/p/text()').getall()
        data = zip(title, author, date_altered, content)
        for item in data:
            info = {"title": item[0], "author": item[1], "date_altered": item[2], "content": item[3]}
        yield info
        for i in response.xpath("//p[contains(@class, 'ArticleParagraph_root__2QM08')]/text()"):
            print(i.get().lstrip())
