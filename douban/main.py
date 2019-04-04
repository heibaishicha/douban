#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/4 0:10
# @Author  : LuoJie
# @Email   : 2715053558@qq.com
# @File    : main.py
# @Software: PyCharm

from scrapy import cmdline
cmdline.execute('scrapy crawl douban_spider'.split( ))