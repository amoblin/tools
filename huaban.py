#!/usr/bin/env python
# -*- coding: utf8 -*-
# author: amoblin <amoblin@163.com>

import sys, re, urllib2, os, urllib
import json

## flickr

flickr_url = "http://www.flickr.com/explore/interesting/7days/?"
flickr_re = '<img src="(.+?)" width'

flickr_api_url = "http://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=045379bc5368502f749af23d95a17c83&tags=beauty&per_page=1&format=json&nojsoncallback=1"


## huaban

beauty_url = "http://huaban.com/favorite/beauty/"
beauty_url_api = "http://api.huaban.com/favorite/beauty/?max=9259498&limit=20"
#beauty_url = "http://huaban.com/"
pin_re = '<a href="/pins/(.+?)/"'

def get_img_url(pin):
    pin_url = "http://huaban.com/pins/%s/" % pin
    print "pin_url: %s" % pin_url
    img_url_re = '<img alt=".+?" src="(.+?)"'
    pg = urllib2.urlopen(pin_url)
    content = pg.read()
    pg.close()
    try:
        img_url = re.findall(img_url_re, content)[0]
    except:
        print re.findall(img_url_re, content)
        sys.exit(1)
    print img_url
    return img_url

def get_index_html():
    os.system("curl -s %s -o /tmp/huaban.html" % beauty_url)
    content = open("/tmp/huaban.html").read()

    pins = re.findall(pin_re, content)[1:]
    for pin in pins:
        img_url = get_img_url(pin)
        print "saving pin: %s" % pin
        urllib.urlretrieve(img_url, "%s/%s.jpeg" % (local_path, pin))

def get_api_json():
    json_str = urllib.urlopen(beauty_url_api)
    huaban = json.load(json_str)
    print len(huaban["pins"])
    for pin in huaban["pins"]:
        print pin["pin_id"], pin["file"]["key"]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        local_path = "./huaban"
    else:
        local_path = sys.argv[1]

    if not os.path.exists(local_path):
        try:
            os.makedirs(local_path)
        except e:
            print e
            sys.exit(1)

    print "pin images will saved to: %s" % local_path
    get_api_json()

