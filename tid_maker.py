#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019-12-10 15:33
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : tid_maker.py
import datetime
import random


def tid_maker():
    return '{0:%Y%m%d%H%M%S%f}'.format(datetime.datetime.now()) + ''.join(
        [str(random.randint(1, 10)) for i in range(5)])

print(tid_maker());