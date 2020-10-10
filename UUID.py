#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/27 10:40
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : UUID.py

import uuid

def getuuid():
    return "".join(str(uuid.uuid4()).split("-")).upper()

uuid = getuuid()
print(uuid)