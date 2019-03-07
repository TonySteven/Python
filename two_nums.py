# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 16:30
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : two_nums.py

# 题目说明:给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

def twoSum(nums, target):

    l = len(nums)

    for m in (0, l - 1):

        for i in (m + 1, l):

            print(m)
            print(i)
            if nums[m] + nums[i] == target:
                return [m, i]
        else:
            continue


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    result = twoSum(nums, target)
    print(result)
