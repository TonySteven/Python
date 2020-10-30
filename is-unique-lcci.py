#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/10/20 16:02
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : is-unique-lcci.py

# 实现一个算法，确定一个字符串 s 的所有字符是否全都不同。
#
# 示例 1：
#
# 输入: s = "leetcode"
# 输出: false
# 示例 2：
#
# 输入: s = "abc"
# 输出: true
# 限制：
#
# 0 <= len(s) <= 100
# 如果你不使用额外的数据结构，会很加分。

class Solution:
    # 方法一 利用set不重复原理
    @staticmethod
    def isUnique1(astr: str) -> bool:
        return len(set(astr)) == len(astr)

    # 方法二 位运算原理
    @staticmethod
    def isUnique(s: str) -> bool:
        # 相当于 set
        seen = 0
        for c in s:
            # 相当于判断 c 是否在 set 中
            if seen & 1 << ord(c) - ord('a') != 0: return False
            # 相当于将 c 加入到 set
            seen |= 1 << ord(c) - ord('a')
        return True


if __name__ == '__main__':
    rusult = Solution.isUnique1(astr='leetcode')
    print(rusult)
