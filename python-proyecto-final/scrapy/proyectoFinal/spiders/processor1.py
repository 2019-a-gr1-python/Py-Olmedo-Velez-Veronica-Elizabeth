import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst
from proyectoFinal.items import InfoPlataforma

def truncar_text(texto):
    if (any(char.isdigit() for char in texto)):
        k = texto.count('K')
        m = texto.count('M')
        texto = texto.replace('K','')
        texto = texto.replace('M','')
        texto = float(texto)
        if (k == 1): texto = texto * 1000
        if (m == 1): texto = texto * 1000000
    return texto

class DetalleItem(scrapy.Spider):
    name = 'p1'
    start_urls = [
        'file:///C:/Users/rprado/AppData/Local/Temp/tmp88x7x84x.html'
    ]
    def parse(self, response):
        resultados_busqueda = response.xpath('body/div[10]/div/div')
        for producto in resultados_busqueda:
            producto_loader = ItemLoader(item=InfoPlataforma(), selector=producto)

            producto_loader.default_input_processor = MapCompose(truncar_text)
            producto_loader.default_output_processor = TakeFirst()

            name = producto_loader.add_xpath('name', 'p[2]/text()')
            value = producto_loader.add_xpath('value', 'p[1]/text()')
            yield producto_loader.load_item()

