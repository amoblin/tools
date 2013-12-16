#!/usr/bin/env python
# -*- coding:utf8 -*-
# author: amoblin <amoblin@gmail.com>
# file name: track.py
# create date: 2013-11-29 11:48:27
# This file is created from ~/.marboo/source/media/file_init/default.init.py
# 本文件由 ~/.marboo/source/media/file_init/default.init.py 复制而来

import sys
from itunes import *
import datetime

APP_ID = 123456789
NUM = 500
keywords = "电影"

app = Lookup(APP_ID).get()[0]
#print app.get_description()
print app.get_name()
print app.get_version()
print app.get_num_ratings()
print app.get_avg_rating()
print app.get_url()

print "关键词排名一览"
for keyword in keywords.split(","):
    i = 0
    isNext = 0
    while not isNext:
        for item in search_app(query=keyword, store="CN", offset=i, limit=NUM):
            i = i + 1
            if item.get_id() == APP_ID:
                print "关键词：%s 排名：%d" % ( keyword, i)
                isNext = 1
                break
print str(datetime.datetime.now())
