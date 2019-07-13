import scrapy
from pipelines_fybeca.items import ProductoFybeca
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
## 6_Deber

# 1) Generar las url 
# 2) Anadir el precio (clase, input,output)
# 3) Transfromar el precio a float
# 4) Exportar a csv
# 5) Anadir un pipeline para seleccionar los productos mayores al promedio


def obtener_urls():
    principal_url = 'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=238&s=changeThis&pp=25'
    return [principal_url.replace('changeThis',str(url)) for url in range(0,176,25) ]
    #Empieza por el cero hasta la 176 de 25 en 25
        
# 1) Generar las url 
class AraniaProductosFybeca(scrapy.Spider):
    name = 'arania_fybeca'

    def start_requests(self):
        urls = obtener_urls() 

        for url in urls:
            yield scrapy.Request(url=url)
            
    def parse(self, response):

        productos = response.css('div.product-tile-inner')
        for producto in productos:
            existe_producto = len( producto.css('div.detail'))
            if(existe_producto > 0):
                
                producto_loader = ItemLoader(
                    item = ProductoFybeca(),
                    selector = producto
                )
                
                producto_loader.default_output_processor = TakeFirst()

                producto_loader.add_css(
                    'titulo',
                    'a.name::text'
                    )
                
                producto_loader.add_xpath(
                    'imagen',
                    'div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src'
                )

                producto_loader.add_css(
                    'precio',
                    '.price::attr(data-bind)'
                )

                yield producto_loader.load_item()
