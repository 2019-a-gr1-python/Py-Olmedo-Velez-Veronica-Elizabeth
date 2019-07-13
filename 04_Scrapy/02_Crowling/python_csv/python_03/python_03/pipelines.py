       
from scrapy.exceptions import DropItem

class FiltrarSoloTabletas(object):

    def process_item(self, item, spider):
        titulo = item['titulo']
        print(titulo)
        if('capsula' not in titulo):
            raise DropItem('No tiene capsula en el titulo')
        else:
            return item

class TransformarTituloAMinusculas(object):
    
    def process_item(self, item, spider):
        print(item['titulo'])
        item['titulo'] = item['titulo'].lower()
        return item