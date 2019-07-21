# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 序号
    serial_number = scrapy.Field()
    # 电影名称
    movie_name = scrapy.Field()
    # 电影介绍
    introduce = scrapy.Field()
    # 星级
    star = scrapy.Field()
    # 电影评论数
    evaluate = scrapy.Field()
    # 电影描述
    describe = scrapy.Field()


class JingDongItem(scrapy.Item):
    """
    @desc 京东商城爬取目录
    """
    # 一级目录
    first_directory = scrapy.Field()
    # 二级目录
    secondary_directory = scrapy.Field()
    # 三级目录
    third_directory = scrapy.Field()
    # 商品名称
    good_name = scrapy.Field()
    # 商品价格
    good_price = scrapy.Field()
    # 优惠券
    coupon = scrapy.Field()
    # 促销内容
    promotion_content = scrapy.Field()
    # 增值业务
    value_added = scrapy.Field()
    # 重量
    weight = scrapy.Field()
    # 服务支持
    server_support = scrapy.Field()
    # 尺寸
    size = scrapy.Field()
    # 增值保障业务
    value_added_security = scrapy.Field()
    # 白条分期
    white_strip = scrapy.Field()




