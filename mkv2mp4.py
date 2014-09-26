#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: amoblin <amoblin@gmail.com>
# file name: mkv2mp4.py
# create date: 2014-04-26 08:09:11
# This file is created from ~/.marboo/source/media/file_init/default.init.py
# 本文件由 ~/.marboo/source/media/file_init/default.init.py 复制而来

import datetime

import os
import sys

SectionDuration = 20 * 60

def getDurationSeconds(name):
    return int(float(os.popen("mkvinfo \"%s\"|grep \"Duration\"" % name).readlines()[0].split(" ")[-2].strip()[:-1]))

c1 = "ffmpeg -y -threads 1 -i \"%s\" -map 0:a:0 -map 0:v:0 -map 0:s:0 -c:v copy -c:a copy -ss 02:00:00 -t 300 %s.mkv"
c1 = "ffmpeg -y -threads 1 -i \"%s\" -map 0:a:0 -map 0:v:0 -map 0:s:0 -r 29.97 -g 2.997 -c:v libx264 -c:a copy %s.mkv"

#c1 = "ffmpeg -y -threads 1 -i \"%s\" -map 0:a:0 -map 0:v:0 -map 0:s:0 -r 29.97 -g 2.997 -c:v libx264 -c:a libfaac -ss %s -t %d %s.mkv"
#c2 = "ffmpeg -y -i %s.mkv -map 0:a:0 -map 0:v:0 -c:v copy -c:a copy %s.mp4"
#c3 = "ffmpeg -y -i %s.mkv -map 0:s:0 %s.ass"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "missing argument"
    name = sys.argv[1]

    position = 0
    end = getDurationSeconds(name)
    sectionCount = end / SectionDuration + 1
    print end, sectionCount

    print(c1 %  (name, "II"))
    os.system(c1 %  (name, "29.97"))
    sys.exit(0)
    for i in range(sectionCount):
        outName = "%s_%d-%d" % ("指环王I", sectionCount, i+1)
        if not os.path.exists(outName + ".mkv"):
            print "generate mkv: %s" % outName
            print(c1 %  (name, str(datetime.timedelta(seconds=position)), SectionDuration, outName))
            os.system(c1 %  (name, str(datetime.timedelta(seconds=position)), SectionDuration, outName))
        if os.path.exists(outName + ".mkv") and not os.path.exists(outName + ".mp4"):
            print "generate mp4: %s" % outName
            os.system(c2 %  (outName, outName))
            os.system(c3 %  (outName, outName))
        position += SectionDuration
