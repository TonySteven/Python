#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 11/1/20 01:29
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : Offer 21.py

# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
#
#  
#
# 示例：
#
# 输入：nums = [1, 2, 3, 4]
# 输出：[1, 3, 2, 4]
# 注：[3, 1, 2, 4]
# 也是正确的答案之一。
#  
#
# 提示：
#
# 1 <= nums.length <= 50000
# 1 <= nums[i] <= 10000
from typing import List


class Solution:
    @staticmethod
    def exchange(nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            while i < j and nums[i] & 1 == 1: i += 1
            while i < j and nums[j] & 1 == 0: j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        return nums



if __name__ == '__main__':
    rusult = Solution.exchange(nums=[1,2,3,4])
    print(rusult)