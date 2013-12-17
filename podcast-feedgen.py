#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: amoblin <amoblin@gmail.com>
# file name: podcast-feedgen.py
# create date: 2013-12-16 23:25:26
# This file is created from ~/.marboo/source/media/file_init/default.init.py
# 本文件由 ~/.marboo/source/media/file_init/default.init.py 复制而来

# require: pip install feedgen
# require: python Orgnode

HTTP_PREFIX="https://dl.dropboxusercontent.com/u/28458830/Podcast"

import os
import sys
import Orgnode
from feedgen.feed import FeedGenerator

fg = FeedGenerator()
fg.load_extension('podcast')
fg.podcast.itunes_category('Technology', 'Podcasting')

fg.id('http://lernfunk.de/media/654321')
fg.title(u'遇见未知的自己')
fg.author( {'name':'whoomin','email':'whoomin@gmail.com'} )
fg.link( href='http://whoomin.marboo.biz', rel='alternate' )
fg.logo('http://ex.com/logo.jpg')
fg.subtitle('sub title')
fg.link( href='http://larskiesow.de/test.atom', rel='self' )
fg.language('en')

nodelist = Orgnode.makelist(sys.argv[1])
for n in nodelist:
    mp3_length = "1024"
    fe = fg.add_entry()

    title = n.Heading()
    category = {"term": n.Tag(), "scheme":"", "label":""}
    link = "http://whoomin.marboo.biz/podcast/1"
    link_dic = {"href":"", "length":mp3_length, "type": "audio/MPEG-3"}

    properties = n.Properties()
    for item in properties:
        if item == "link":
            mp3_url = os.path.join(HTTP_PREFIX, properties[item])
            fe.enclosure(mp3_url, mp3_length, "audio/MPEG-3")
        elif item == "description":
            description = "<![CDATA[ %s ]]>" % properties[item]
            fe.description(description, isSummary=1)
        elif item == "summary":
            summary = properties[item]
            fe.summary(summary)
        else:
            print item

    fe.title(title)
    fe.author({"name":"whoomin", "email":"whoomin@gmail.com"})
    fe.guid(link)
    fe.link(link_dic)
    fe.category(category)
    #fe.pubdate()
    #fe.duration(mp3_length)

print fg.rss_str(pretty=True)
