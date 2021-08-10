import scrapy


class TheConversationInfoSpider(scrapy.Spider):
    name = "the_conversation_info"
    allowed_domains = ["theconversation.com"]
    start_urls = [
        "https://theconversation.com/vaccinating-teenagers-is-beneficial-even-if-their-vulnerability-to-covid-19-is-low-165690/"
    ]

    def parse(self, response):

        title = response.xpath('//*[@id="article"]/figure/div[3]/div/header/div/div/h1/strong/text()[1]').extract()
        author = response.xpath('//*[@id="author-403130"]/a/span').extract()
        date_altered = response.xpath('//*[@id="article"]/figure/div[3]/div/header/time/attribute::content').extract()
        content = response.xpath('//*[@id="article"]/div[1]/div[2]/div[2]/p/text()').getall()
        data = zip(title, author, date_altered, content)
        for item in data:
            info = {"title": item[0], "author": item[1], "date_altered": item[2], "content": item[3]}
            yield info
