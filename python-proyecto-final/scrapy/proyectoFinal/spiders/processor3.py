import scrapy
import math
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from proyectoFinal.items import AccountItem

import sqlite3
import pandas as pd

class DetalleAccountItem(scrapy.Spider):
    # Create your connection.
    conexion = sqlite3.connect('C:/Users/rprado/python-proyecto-final/socialblade.db')
    # df_read = pd.read_sql_query("SELECT * FROM accounts where origin = 'Instagram'", conexion)
    df_read = pd.read_sql_query("SELECT * FROM accounts", conexion)
    uris = df_read['uri'].values
    name = 'p3'
    start_urls = [
        'file:///C:/Users/rprado/AppData/Local/Temp/tmpfd884h7x.html'
    ]
    start_urls = uris
    def parse(self, response):
        current_url = response.request.url
        print(current_url)
        account = self.df_read[self.df_read['uri'].str.contains(current_url, case=False, regex=False)]
        username = account['username'].values[0]
        origin = account['origin'].values[0]
        resultados_busqueda = response.xpath('/html/body')
        for producto in resultados_busqueda:
            producto_loader = ItemLoader(item=AccountItem(), selector=producto)
            producto_loader.default_output_processor = TakeFirst()

            if(origin == 'YouTube'):
                producto_loader.add_xpath('twitter', '//a/i[@class="fa fa-twitter"]/parent::a/@href')
                producto_loader.add_value('username', username)
                producto_loader.add_css('country', '#youtube-user-page-country::text')
                producto_loader.add_css('category', '#youtube-user-page-channeltype::text')
                producto_loader.add_xpath('start_date', '//div[@class="YouTubeUserTopInfo"][span = "User Created"]/span[2]/text()')
                producto_loader.add_xpath('subscribers_daily', '//div[contains(text(),"Daily Averages")]/following-sibling::div[1]/span/text()')
                producto_loader.add_xpath('views_daily', '//div[contains(text(),"Daily Averages")]/following-sibling::div[2]/span/text()')
                producto_loader.add_xpath('earnings_daily', '//div[contains(text(),"Daily Averages")]/following-sibling::div[3]/text()')
                producto_loader.add_xpath('subscribers_monthly', '//div[contains(text(),"Last 30 Days")]/following-sibling::div[1]/span/text()')
                producto_loader.add_xpath('views_monthly', '//div[contains(text(),"Last 30 Days")]/following-sibling::div[2]/span/text()')
                producto_loader.add_xpath('earnings_monthly', '//div[contains(text(),"Last 30 Days")]/following-sibling::div[3]/text()')

            if(origin == 'Twitch'):
                producto_loader.add_value('username', username)
                producto_loader.add_xpath('subscribers_daily', '//div[contains(text(),"Daily Averages")]/following-sibling::div[1]/span/text()')
                producto_loader.add_xpath('views_daily', '//div[contains(text(),"Daily Averages")]/following-sibling::div[2]/span/text()')
                producto_loader.add_xpath('subscribers_monthly', '//div[contains(text(),"Monthly Averages")]/following-sibling::div[1]/span/text()')
                producto_loader.add_xpath('views_monthly', '//div[contains(text(),"Monthly Averages")]/following-sibling::div[2]/span/text()')

            if (origin == 'Twitter'):
                producto_loader.add_xpath('twitter', '//a[contains(text(),"Twitter Profile")]/@href')
                producto_loader.add_value('username', username)
                producto_loader.add_xpath('start_date', '//div[@class="YouTubeUserTopInfo"][span = "User Created"]/span[2]/text()')
                producto_loader.add_xpath('subscribers_daily',
                                          '//div[contains(text(),"Daily Averages")]/following-sibling::div[1]/span/text()')
                producto_loader.add_xpath('views_daily',
                                          '//div[contains(text(),"Daily Averages")]/following-sibling::div[3]/span/text()')
                producto_loader.add_xpath('subscribers_monthly',
                                          '//div[contains(text(),"Last 30 Days")]/following-sibling::div[1]/span/text()')
                producto_loader.add_xpath('views_monthly',
                                          '//div[contains(text(),"Last 30 Days")]/following-sibling::div[3]/span/text()')

            if (origin == 'Instagram'):
                producto_loader.add_value('username', username)
                producto_loader.add_xpath('subscribers_daily',
                                          '//div[contains(text(),"Daily Averages")]/following-sibling::div[1]/span/text()')
                producto_loader.add_xpath('subscribers_monthly',
                                          '//div[contains(text(),"Monthly Averages")]/following-sibling::div[1]/span/text()')
                producto_loader.add_xpath('views_daily',
                                          '//div[contains(text(),"Daily Averages")]/following-sibling::div[3]/span/text()')
                producto_loader.add_xpath('views_monthly',
                                          '//div[contains(text(),"Monthly Averages")]/following-sibling::div[3]/span/text()')
            yield producto_loader.load_item()