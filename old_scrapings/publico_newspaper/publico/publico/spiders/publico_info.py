import scrapy


class PublicoInfoSpider(scrapy.Spider):
    name = "publico_info"
    allowed_domains = ["https://tinyurl.com/yzbkuzq7"]
    start_urls = ["https://tinyurl.com/yzbkuzq7/"]

    def parse(self, response):

        title = response.xpath('//*[@id="story-header"]/div/h1/text()').extract()
        author = response.xpath('//*[@id="story-header"]/div/div[3]/div[1]/div/address[1]/a/span').extract()
        date_altered = response.xpath('//*[@id="story-header"]/div/div[3]/div[1]/time/attribute::datetime').extract()
        content = response.xpath('//*[@id="story-body"]/p').getall()
        data = zip(title, author, date_altered, content)
        for item in data:
            info = {"title": item[0], "author": item[1], "date_altered": item[2], "content": item[3]}
            yield info
