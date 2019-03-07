#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 17:16
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : solution217.py

#说明:给定一个整数数组，判断是否存在重复元素。

# 如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

def twoSum(nums):
    set1 = set(nums)
    if len(set1) == len(nums):
        return False
    else:
        return True


if __name__ == '__main__':
    nums = [2, 2, 11, 15]
    result = twoSum(nums)
    print(result)