#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-21 10:41
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : 520.py
import time, os, math

[([(time.sleep(a), print("\033[91m" + i, end="", flush=True)) for i in ('\n'.join([''.join([(' I love U'[
                                                                                                 (x - y) % 9] if ((
                                                                                                                          x * 0.05) ** 2 + (
                                                                                                                          y * 0.1) ** 2 - 1) ** 3 - (
                                                                                                                         x * 0.05) ** 2 * (
                                                                                                                         y * 0.1) ** 3 <= 0 else ' ')
                                                                                            for x in range(-30, 30)])
                                                                                   for y in range(15, -15, -1)]))],
  time.sleep(1 / math.log(ai + 3)), os.system('clear')) for (ai, a) in enumerate([0.001, *[0.00001] * 99])]
