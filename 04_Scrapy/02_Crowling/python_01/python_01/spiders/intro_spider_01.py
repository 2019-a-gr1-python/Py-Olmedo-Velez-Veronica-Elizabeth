import scrapy
import os

class IntroSpyder(scrapy.Spider):
    name = 'introduccion_spider'

    def start_requests (self):
        urls= [
            'http://books.toscrape.com/catalogue/category/books_1/page-1.html'
        ]

        for url in urls:
            yield scrapy.Request(url=url)

    def parse(self, response):
        etiqueta_contenedora= response.css('article.product_pod')
        titulos = etiqueta_contenedora.css('h3 > a::attr(title)').extract()
        stocks = etiqueta_contenedora.css('div.product_price > p.instock.availability::text').extract()
        precios = etiqueta_contenedora.css('div.product_price > p.price_color::text').extract()

        print(titulos)
        print(stocks)
        print(precios)
    
        
        print(os.getcwd())
        with open("titulos.txt","w") as file:
            for text in titulos:
                file.write(text)
            file.close()

        with open("precios.txt","w") as file:
            for text in precios:
                file.write(text)
            file.close()

        with open("stocks.txt","w") as file:
            for text in stocks:
                file.write(text)
            file.close()











