#!/bin/sh
# author: amoblin <amoblin@gmail.com>
# file name: mkv2mp4.sh
# create date: 2014-04-20 07:32:51
# This file is created from ~/.marboo/source/media/file_init/default.init.sh
# 本文件由 ~/.marboo/source/media/file_init/default.init.sh　复制而来

file="$1"

# 提取出来放到mkv里

ffmpeg -y -i $file -map 0:a:0 -map 0:v:0 -map 0:s:0 -r 29.97 -g 2.997 -c:v libx264 -c:a libfaac -ss 00:00:00 -t 1200 1-1.mkv
ffmpeg -y -i 1-1.mkv -map 0:a:0 -map 0:v:0 -c:v copy -c:a copy 1-1.mp4
ffmpeg -y -i 1-1.mkv -map 0:s:0 1-1.ass

# 等分
#ffmpeg -i $file.mp4 -c:v copy -c:a copy -ss 03:40:00 -to 04:00:00 12.mp4
