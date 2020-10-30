#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/10/20 16:33
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : check-permutation-lcci.py

# 给定两个字符串 s1 和 s2，请编写一个程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。
#
# 示例 1：
#
# 输入: s1 = "abc", s2 = "bca"
# 输出: true
# 示例 2：
#
# 输入: s1 = "abc", s2 = "bad"
# 输出: false
# 说明：
#
# 0 <= len(s1) <= 100
# 0 <= len(s2) <= 100

def CheckPermutation(astr: str) -> bool:
    return len(set(astr)) == len(astr)


if __name__ == '__main__':
    rusult = CheckPermutation(astr='leetcode')
    print(rusult)
