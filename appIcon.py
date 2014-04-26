#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: amoblin <amoblin@gmail.com>
# file name: appIcon.py
# create date: 2014-03-18 21:04:54
# This file is created from ~/.marboo/source/media/file_init/default.init.py
# 本文件由 ~/.marboo/source/media/file_init/default.init.py 复制而来

import os
import sys

origin_name = sys.argv[1]
core_name = os.path.splitext(origin_name)[0]
extension = os.path.splitext(origin_name)[1]

print origin_name
print core_name
print extension

size = [29, 40, 50, 57, 72, 76]
size_2 = [29, 40, 50, 57, 60, 72, 76]

for i in size:
    filename = "%s-%d%s" % (core_name, i, extension)
    os.system("cp %s %s" % (origin_name, filename))
    os.system("sips -Z %s %s" % (i, filename))

for i in size_2:
    filename = "%s-%d@2x%s" % (core_name, i, extension)
    os.system("cp %s %s" % (origin_name, filename))
    os.system("sips -Z %s %s" % (i*2, filename))
