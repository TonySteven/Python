#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 11/20/20 11:39
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : reverseWords.py

# 简单说明
# 输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student. "，则输出"student. a am I"。


class Solution:
    def reverseWords1(self, s: str) -> str:
        # 双指针方法
        s = s.strip()  # 删除首尾空格
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ': i -= 1  # 搜索首个空格
            res.append(s[i + 1: j + 1])  # 添加单词
            while s[i] == ' ': i -= 1  # 跳过单词间空格
            j = i  # j 指向下个单词的尾字符
        return ' '.join(res)  # 拼接并返回

    def reverseWords2(self, s: str) -> str:
        # 分割 + 倒序
        # 由于 split() 方法将单词间的 “多个空格看作一个空格” （参考自split()和split(' ')的区别 ），因此不会出现多余的 “空单词” 。
        # 因此，直接利用reverse()方法翻转单词列表strs ，拼接为字符串并返回即可。
        return ' '.join(s.strip().split()[::-1])


if __name__ == '__main__':
    str = 'the sky is blue'

    s = Solution()
    result = s.reverseWords1(s=str)
    print(result)
