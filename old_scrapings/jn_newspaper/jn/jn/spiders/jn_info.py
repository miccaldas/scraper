import scrapy


class JnInfoSpider(scrapy.Spider):
    name = 'jn_info'
    allowed_domains = ['https://www.jn.pt/mundo/descoberto-barco-romano-carregado-de-anforas-portuguesas-no-mar-da-sicilia-14019544.html']
    start_urls = ['https://www.jn.pt/mundo/descoberto-barco-romano-carregado-de-anforas-portuguesas-no-mar-da-sicilia-14019544.html/']

    def parse(self, response):
        
        title = response.xpath('/html/body/main/article/header/h1/text()').extract()
        author = response.xpath('/html/body/main/article/div/div/aside/div/div[1]/div/span/text()').extract()
        date_altered = response.xpath('/html/body/main/article/div/div/aside/div/div[1]/time/attribute::datetime').extract()
        content = response.xpath('/html/body/main/article/div/div/p/text()').getall()
        data = zip(title, author, date_altered, content)
        for item in data:
            info = {'title': item[0], 'author': item[1], 'date_altered': item[2], 'content': item[3]}
        yield info
        with open('content.txt', 'w') as cont:
            for i in response.xpath(f'/html/body/main/article/div/div/p/text()').getall():
                cont.write(str(i))