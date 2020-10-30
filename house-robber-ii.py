#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/30/20 22:40
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : house-robber-ii.py
from typing import List


class Solution:
    # 方法一 利用set不重复原理
    @staticmethod
    def rob(nums: List[int]) -> int:
        def robmax(nums):
            nums_len = len(nums)
            if not nums: return 0
            if nums_len == 1: return nums[0]

            opt = [0] * nums_len
            opt[0] = nums[0]
            opt[1] = max(nums[0], nums[1])

            for i in range(2, nums_len):
                opt[i] = max(opt[i - 1], opt[i - 2] + nums[i])
            return opt[nums_len - 1]

        if not nums: return 0
        if len(nums) == 1: return nums[0]

        nums1 = nums[1:]  # [1,n] 找到到最大值
        nums2 = nums[0:len(nums) - 1]  # [0,n-1] 找到到最大值
        return max(robmax(nums1), robmax(nums2))


if __name__ == '__main__':
    rusult = Solution.rob(nums=[1,2,4,124,231,12,4,12])
    print(rusult)