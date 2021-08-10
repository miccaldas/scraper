import scrapy


class EcoInfoSpider(scrapy.Spider):
    name = 'eco_info'
    allowed_domains = ['https://eco.sapo.pt/2021/08/10/chineses-obrigam-loja-da-xiaomi-em-portugal-a-desistir-de-pagamentos-com-criptomoedas/']
    start_urls = ['https://eco.sapo.pt/2021/08/10/chineses-obrigam-loja-da-xiaomi-em-portugal-a-desistir-de-pagamentos-com-criptomoedas//']

    def parse(self, response):
        
        title = response.xpath('//*[@id="post-878113"]/div/div[1]/header/h1/text()').extract()
        author = response.xpath('//*[@id="post-878113"]/div/div[1]/header/div[2]/div/div[1]/ul/li[1]/a/text()').extract()
        date_altered = response.xpath('//*[@id="post-878113"]/div/div[1]/header/div[2]/div/div[1]/ul/li[2]').extract()
        content = response.xpath('//*[@id="post-878113"]/div/div[1]/div[1]/p/text()').getall()
        data = zip(title, author, date_altered, content)
        for item in data:
            info = {'title': item[0], 'author': item[1], 'date_altered': item[2], 'content': item[3]}
        yield info
        with open('content.txt', 'w') as cont:
            for i in response.xpath('//*[@id="post-878113"]/div/div[1]/div[1]/p/text()').getall():
                cont.write(str(i))