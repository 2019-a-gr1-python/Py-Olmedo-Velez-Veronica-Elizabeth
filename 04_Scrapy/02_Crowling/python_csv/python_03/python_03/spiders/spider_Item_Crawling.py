import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor 

class AraniaCrawling(CrawlSpider):
    name='crawl_productos' #Heredado conservar nombre de atributo
    allowed_domains = [     #Heredado conservar nombre de atributo
        'fybeca.com'
        ]
    start_urls=[    #Heredado conservar nombre de atributo
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=238&s=0&pp=25'
        ]
    url_segmentos_permitidos=(
        'cat=238'
       
        )
    rules=(
        Rule(
            LinkExtractor(
                allow_domains=allowed_domains,
                allow=url_segmentos_permitidos
                ),callback='parse_page'),
        )