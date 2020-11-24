#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 11/24/20 23:41
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : isStraight.py
from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        joker = 0
        nums.sort()  # 数组排序
        for i in range(4):
            if nums[i] == 0:
                joker += 1  # 统计大小王数量
            elif nums[i] == nums[i + 1]:
                return False  # 若有重复，提前返回 false
        return nums[4] - nums[joker] < 5  # 最大牌 - 最小牌 < 5 则可构成顺子


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    s = Solution()
    result = s.isStraight(nums=nums)
    print(result)
