#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 11/22/20 01:03
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : reverseLeftWords.py


class Solution:
    def reverseLeftWords1(self, s: str, n: int) -> str:
        # 切片方法
        return s[n:] + s[:n]

    def reverseLeftWords2(self, s: str, n: int) -> str:
        # 列表遍历拼接
        res = []
        for i in range(n, n + len(s)):
            res.append(s[i % len(s)])
        return ''.join(res)


if __name__ == '__main__':
    str = 'abcdefg'
    n = 2
    s = Solution()
    result = s.reverseLeftWords1(s=str, n=n)
    print(result)
