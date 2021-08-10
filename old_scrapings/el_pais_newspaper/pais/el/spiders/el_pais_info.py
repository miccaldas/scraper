import scrapy


class ElPaisInfoSpider(scrapy.Spider):
    name = "el_pais_info"
    allowed_domains = ["elpais.com"]
    start_urls = ["https://tinyurl.com/yganfm57/"]

    def parse(self, response):

        title = response.xpath("//*[@id='article_header']/h1/text()").extract()
        author = response.xpath("//*[@id='fusion-app']/article/header/div[4]/div[1]/span/text()").extract()
        date_altered = response.xpath("//*[@id='article_date']/text()").extract()
        content = response.xpath("//*[@id='ctn_article_body']/p/text()").getall()
        data = zip(title, author, date_altered, content)
        for item in data:
            info = {"title": item[0], "author": item[1], "date_altered": item[2], "content": item[3]}
        yield info
