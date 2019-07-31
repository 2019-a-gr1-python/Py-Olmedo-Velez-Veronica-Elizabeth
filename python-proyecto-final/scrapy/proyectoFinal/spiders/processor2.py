import scrapy
import math
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from proyectoFinal.items import YouTubeItem
from proyectoFinal.items import TwitchItem
from proyectoFinal.items import TwitterItem
from proyectoFinal.items import InstagramItem

class DetalleYouTubeItem(scrapy.Spider):
    name = 'p2'
    start_urls = [
        'file:///C:/Users/rprado/AppData/Local/Temp/tmppv4p43xt.html'
    ]
    def parse(self, response):
        resultados_busqueda = response.xpath('/html/body/div[9]/div[2]/div[position()>4]')
        for producto in resultados_busqueda:
            producto_loader = ItemLoader(item=YouTubeItem(), selector=producto)
            producto_loader.default_output_processor = TakeFirst()

            rank = producto_loader.add_xpath('rank', 'div[1]/text()')
            grade = producto_loader.add_xpath('grade', 'div[2]/span/text()')
            username = producto_loader.add_xpath('username', 'div[3]/a/text()')
            uri = producto_loader.add_xpath('uri', 'div[3]/a/@href')
            uploads = producto_loader.add_xpath('uploads', 'div[4]/span/text()')
            subs = producto_loader.add_xpath('subs', 'div[5]/span/text()')
            views = producto_loader.add_xpath('views', 'div[6]/span/text()')
            yield producto_loader.load_item()

class DetalleTwitchItem(scrapy.Spider):
    name = 'p3'
    start_urls = [
        'file:///C:/Users/rprado/AppData/Local/Temp/tmpswix9pv8.html'
    ]
    def parse(self, response):
        resultados_busqueda = response.css('div.content-module-wide > div.table-cell')
        producto_loader_final = {'rank': None, 'grade': None, 'username': None, 'uri': None, 'subs': None, 'views': None}
        for idx, producto in enumerate(resultados_busqueda):
            producto_loader = ItemLoader(item=TwitchItem(), selector=producto)
            producto_loader.default_output_processor = TakeFirst()
            m = math.floor(idx / 5)
            indice_actual = idx - (m * 5)
            if (indice_actual == 0):
                producto_loader_final = {'rank': None, 'grade': None, 'username': None, 'uri': None, 'subs': None,
                                         'views': None}
                producto_loader.add_xpath('rank', 'text()')
                producto_loader_final['rank'] = producto_loader.load_item()['rank']

            if (indice_actual == 1):
                producto_loader.add_xpath('grade', 'span/text()')
                producto_loader_final['grade'] = producto_loader.load_item()['grade']

            if (indice_actual == 2):
                producto_loader.add_xpath('username', 'a/text()')
                producto_loader_final['username'] = producto_loader.load_item()['username']
                producto_loader.add_xpath('uri', 'a/@href')
                producto_loader_final['uri'] = producto_loader.load_item()['uri']

            if (indice_actual == 3):
                producto_loader.add_xpath('subs', 'text()')
                producto_loader_final['subs'] = producto_loader.load_item()['subs']

            if (indice_actual == 4):
                producto_loader.add_xpath('views', 'text()')
                producto_loader_final['views'] = producto_loader.load_item()['views']
                yield producto_loader_final

class DetalleTwitterItem(scrapy.Spider):
    name = 'p4'
    start_urls = [
        'file:///C:/Users/rprado/AppData/Local/Temp/tmpbptvin5a.html'
    ]
    def parse(self, response):
        resultados_busqueda = response.css('div.content-module-wide > div.table-cell')
        producto_loader_final = {'rank': None, 'grade': None, 'username': None, 'uri': None, 'uploads': None, 'subs': None, 'follow': None}
        for idx, producto in enumerate(resultados_busqueda):
            producto_loader = ItemLoader(item=TwitterItem(), selector=producto)
            producto_loader.default_output_processor = TakeFirst()
            m = math.floor(idx / 6)
            indice_actual = idx - (m * 6)
            if (indice_actual == 0):
                producto_loader_final = {'rank': None, 'grade': None, 'username': None, 'uri': None, 'uploads': None, 'subs': None, 'follow': None}
                producto_loader.add_xpath('rank', 'text()')
                producto_loader_final['rank'] = producto_loader.load_item()['rank']

            if (indice_actual == 1):
                producto_loader.add_xpath('grade', 'span/text()')
                producto_loader_final['grade'] = producto_loader.load_item()['grade']

            if (indice_actual == 2):
                producto_loader.add_xpath('username', 'a/text()')
                producto_loader_final['username'] = producto_loader.load_item()['username']
                producto_loader.add_xpath('uri', 'a/@href')
                producto_loader_final['uri'] = producto_loader.load_item()['uri']

            if (indice_actual == 3):
                producto_loader.add_xpath('uploads', 'text()')
                producto_loader_final['uploads'] = producto_loader.load_item()['uploads']

            if (indice_actual == 4):
                producto_loader.add_xpath('subs', 'text()')
                producto_loader_final['subs'] = producto_loader.load_item()['subs']

            if (indice_actual == 5):
                producto_loader.add_xpath('follow', 'text()')
                producto_loader_final['follow'] = producto_loader.load_item()['follow']
                yield producto_loader_final

class DetalleInstagramItem(scrapy.Spider):
    name = 'p6'
    start_urls = [
        'file:///C:/Users/rprado/AppData/Local/Temp/tmpgzkcrorz.html'
    ]
    def parse(self, response):
        resultados_busqueda = response.xpath('/html/body/div[9]/div[2]/div[position()>4]')
        for producto in resultados_busqueda:
            producto_loader = ItemLoader(item=InstagramItem(), selector=producto)
            producto_loader.default_output_processor = TakeFirst()

            rank = producto_loader.add_xpath('rank', 'div[1]/text()')
            grade = producto_loader.add_xpath('grade', 'div[2]/span/text()')
            username = producto_loader.add_xpath('username', 'div[3]/a/text()')
            uri = producto_loader.add_xpath('uri', 'div[3]/a/@href')
            uploads = producto_loader.add_xpath('uploads', 'div[4]/span/text()')
            subs = producto_loader.add_xpath('subs', 'div[5]/span/text()')
            views = producto_loader.add_xpath('follow', 'div[6]/span/text()')
            yield producto_loader.load_item()

