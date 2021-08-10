import scrapy


class GuernicaInfoSpider(scrapy.Spider):
    name = 'guernica_info'
    allowed_domains = ['https://www.guernicamag.com/at-the-bend-of-the-road/']
    start_urls = ['https://www.guernicamag.com/at-the-bend-of-the-road//']

    def parse(self, response):
        
        title = response.xpath('//*[@id="content"]/article/header/h1/text()').extract()
        author = response.xpath('//*[@id="content"]/article/header/span[2]/a/text()').extract()
        date_altered = response.xpath('//*[@id="content"]/article/header/span[1]/text()').extract()
        content = response.xpath('//p/text()').getall()
        data = zip(title, author, date_altered, content)
        for item in data:
            info = {'title': item[0], 'author': item[1], 'date_altered': item[2], 'content': item[3]}
        yield info
        with open('content.txt', 'w') as cont:
            for i in response.xpath(f'//p/text()').getall():
                cont.write(str(i))