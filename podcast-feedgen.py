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
import time, pytz
import Orgnode
from feedgen.feed import FeedGenerator

fg = FeedGenerator()
fg.load_extension('podcast')

nodelist = Orgnode.makelist(sys.argv[1])

info = nodelist[0]
properties = info.Properties()
fg.podcast.itunes_category('Technology', 'Podcasting')

fg.title(info.Heading())
fg.author( {'name':properties['author'],'email':properties['email']} )
fg.id(properties["id"])
fg.link( href='http://whoomin.marboo.biz', rel='alternate' )
fg.logo(properties["logo"])
fg.subtitle(properties["subtitle"])
fg.link(href=properties["link"], rel='self' )
fg.language(properties["language"])
fg.image(properties["image"], height="140", width="140")
fg.rights(properties["copyright"])
fg.podcast.itunes_author(properties["author"])
fg.podcast.itunes_subtitle(properties["subtitle"])
fg.podcast.itunes_summary(properties["summary"])
#fg.podcast.itunes_keywords(properties["keywords"])
#fg.ttl(1440)

for i in range(1, len(nodelist)):
    node = nodelist[i]
    if node.Todo() == "DRAFT":
        continue
    mp3_length = "1024"
    fe = fg.add_entry()

    title = node.Heading()
    category = {"term": node.Tag(), "scheme":"", "label":""}
    #link = "http://whoomin.marboo.biz/podcast/1"
    link_dic = {"href":"", "length":mp3_length, "type": "audio/MPEG"}

    properties = node.Properties()
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
            print properties[item]

    fe.pubdate(node.Closed().replace(tzinfo=pytz.timezone('Asia/Shanghai')))

    fe.title(title)
    fe.author({"name":"whoomin", "email":"whoomin@gmail.com"})
    #fe.guid(link)
    fe.link(link_dic)
    fe.category(category)
    #fe.duration(mp3_length)

print fg.rss_str(pretty=True)
