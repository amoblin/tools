#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: amoblin <amoblin@gmail.com>
# file name: track.py
# create date: 2013-11-29 11:48:27
# This file is created from ~/.marboo/source/media/file_init/default.init.py
# 本文件由 ~/.marboo/source/media/file_init/default.init.py 复制而来

import sys
from itunes import *
import datetime
import os

LIMIT = 500
APP_ID = 848880040
Bundle_ID = "com.Mofunsky.EnglishMofunShow"
NUM = 500

keywords = "演奏,钢琴,键盘,piano,keyboard,乐曲,傻瓜,傻瓜音乐家,伴奏,节奏大师,音乐"

app = Lookup(APP_ID).get()[0]
#print app.get_description()
#sys.exit(0)
print app.get_name()
print app.get_version()
print app.get_num_ratings()
print app.get_avg_rating()
print app.get_url()

print "中国区关键词排名一览"
for keyword in keywords.split(","):
    i = 0
    isNext = 0
    while not isNext:
        items = search_app(query=keyword, store="CN", offset=i, limit=NUM)
        if len(items) == 0:
            isNext = 1
            info = "关键词：%s 排名未找到" % ( keyword)
            print info
            os.system("say %s" % info)
            break
        for item in items:
            i = i + 1
            if item.get_id() == APP_ID:
                info = "关键词：%s 排名：%d" % ( keyword, i)
                print info
                os.system("say %s" % info)
                isNext = 1
                break
        if i >= LIMIT:
            info = "关键词：%s 排名在%d之外" % ( keyword, i)
            print info
            os.system("say %s" % info)
            isNext = 1
            break
print str(datetime.datetime.now())
