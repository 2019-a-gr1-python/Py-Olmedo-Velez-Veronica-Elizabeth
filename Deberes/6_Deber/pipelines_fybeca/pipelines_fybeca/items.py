import scrapy
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst
import re 

def transformar_url_imagen(texto): 
    url = 'https://www.fybeca.com' 
    cadena_a_reemplazar = '../..'   
    return texto.replace(cadena_a_reemplazar,url)

def obtener_precio_item(precio):
    # Crea un objeto 'expresión regular' para encontrar texto de acuerdo a un patron
    regex = r"(\d+\.\d{1,})"
    # 3) Transfromar el precio a float
    return float(re.search(regex,precio).group(0))
        


class ProductoFybeca(scrapy.Item):
    imagen = scrapy.Field(
        input_processor = MapCompose(
            transformar_url_imagen
            ),
        output_processor = TakeFirst()
    )
    titulo = scrapy.Field()

    # 2) Anadir el precio (clase, input,output)
    precio = scrapy.Field(
        input_processor= MapCompose(
            obtener_precio_item
        ),
        output_processor = TakeFirst() 
    ) 