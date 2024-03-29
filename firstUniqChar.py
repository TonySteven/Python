#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 11/12/20 11:14
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : firstUniqChar.py
import string


class Solution:
    def firstUniqChar(self, s: string) -> string:
        dic = {}
        for c in s:
            dic[c] = not c in dic
        for c in s:
            if dic[c]: return c
        return ' '


if __name__ == '__main__':
    str = 'abaccdeff'

    s = Solution()
    result = s.firstUniqChar(s=str)
    print(result)
