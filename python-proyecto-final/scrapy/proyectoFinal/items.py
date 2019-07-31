# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from datetime import datetime
from scrapy.loader.processors import MapCompose

def socialblade_link(link):
    short_link = 'https://socialblade.com' + link
    return  short_link

def rank_to_int(rank):
    rank = rank.replace('st','')
    rank = rank.replace('nd','')
    rank = rank.replace('rd','')
    rank = rank.replace('th','')
    rank = int(rank)
    return rank

def count_to_int(rank):
    rank = rank.replace(',','')
    if (rank == '--'):
        rank = '0'
    rank = int(rank)
    return  rank
def months(x):
    return {
        'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
    }[x]
def str_to_date(d):
    d = d.replace(',','')
    d = d.replace('st', '')
    d = d.replace('nd', '')
    d = d.replace('rd', '')
    d = d.replace('th', '')
    parts = d.split(' ')
    try:
        m = parts[0]
        d = parts[1]
        y = parts[2]
        # return f'{d}-{m}-{y}'
        return f'{m} {d} {y}'
    except:
        return d

def clean_earn(e):
    e = e.replace('\n','')
    e = e.replace('\xa0-\xa0','')
    parts = e.split('  ')
    try:
        for idx, i in enumerate(parts):
            k = parts[idx].count('K')
            m = parts[idx].count('M')
            parts[idx] = parts[idx].replace('K', '')
            parts[idx] = parts[idx].replace('M', '')
            parts[idx] = parts[idx].replace('$', '')
            parts[idx] = float(parts[idx])
            if (k == 1): parts[idx]= parts[idx] * 1000
            if (m == 1): parts[idx] = parts[idx] * 1000000
        return f'{parts[0]}'
    except:
        return e


class ProyectofinalItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class InfoPlataforma(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    value = scrapy.Field()
    pass

class YouTubeItem(scrapy.Item):
    # define the fields for your item here like:
    rank = scrapy.Field(input_processor=MapCompose(rank_to_int))
    grade = scrapy.Field()
    username = scrapy.Field()
    uri = scrapy.Field(input_processor=MapCompose(socialblade_link))
    uploads = scrapy.Field(input_processor=MapCompose(count_to_int))
    subs = scrapy.Field(input_processor=MapCompose(count_to_int))
    views = scrapy.Field(input_processor=MapCompose(count_to_int))
    pass

class TwitchItem(scrapy.Item):
    # define the fields for your item here like:
    rank = scrapy.Field(input_processor=MapCompose(rank_to_int))
    grade = scrapy.Field()
    username = scrapy.Field()
    uri = scrapy.Field(input_processor=MapCompose(socialblade_link))
    subs = scrapy.Field(input_processor=MapCompose(count_to_int))
    views = scrapy.Field(input_processor=MapCompose(count_to_int))
    pass

class TwitterItem(scrapy.Item):
    # define the fields for your item here like:
    rank = scrapy.Field(input_processor=MapCompose(rank_to_int))
    grade = scrapy.Field()
    username = scrapy.Field()
    uri = scrapy.Field(input_processor=MapCompose(socialblade_link))
    uploads = scrapy.Field(input_processor=MapCompose(count_to_int))
    subs = scrapy.Field(input_processor=MapCompose(count_to_int))
    follow = scrapy.Field(input_processor=MapCompose(count_to_int))
    pass

class InstagramItem(scrapy.Item):
    # define the fields for your item here like:
    rank = scrapy.Field(input_processor=MapCompose(rank_to_int))
    grade = scrapy.Field()
    username = scrapy.Field()
    uri = scrapy.Field(input_processor=MapCompose(socialblade_link))
    uploads = scrapy.Field(input_processor=MapCompose(count_to_int))
    subs = scrapy.Field(input_processor=MapCompose(count_to_int))
    follow = scrapy.Field(input_processor=MapCompose(count_to_int))
    pass

class AccountItem(scrapy.Item):
    # define the fields for your item here like:
    username = scrapy.Field()
    country = scrapy.Field()
    category = scrapy.Field()
    subscribers_daily = scrapy.Field(input_processor=MapCompose(count_to_int))
    subscribers_monthly = scrapy.Field(input_processor=MapCompose(count_to_int))
    views_daily = scrapy.Field(input_processor=MapCompose(count_to_int))
    views_monthly = scrapy.Field(input_processor=MapCompose(count_to_int))
    earnings_daily = scrapy.Field(input_processor=MapCompose(clean_earn))
    earnings_monthly = scrapy.Field(input_processor=MapCompose(clean_earn))
    start_date = scrapy.Field(input_processor=MapCompose(str_to_date))
    twitter = scrapy.Field()
    pass
