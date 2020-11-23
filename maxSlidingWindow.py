#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 11/23/20 23:39
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : maxSlidingWindow.py
import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = collections.deque()
        res, n = [], len(nums)
        for i, j in zip(range(1 - k, n + 1 - k), range(n)):
            if i > 0 and deque[0] == nums[i - 1]:
                deque.popleft()  # 删除 deque 中对应的 nums[i-1]
            while deque and deque[-1] < nums[j]:
                deque.pop()  # 保持 deque 递减
            deque.append(nums[j])
            if i >= 0:
                res.append(deque[0])  # 记录窗口最大值
        return res

    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        # 可以将 “未形成窗口” 和 “形成窗口后” 两个阶段拆分到两个循环里实现。代码虽变长，但减少了冗余的判断操作。
        if not nums or k == 0: return []
        deque = collections.deque()
        for i in range(k):  # 未形成窗口
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
        res = [deque[0]]
        for i in range(k, len(nums)):  # 形成窗口后
            if deque[0] == nums[i - k]:
                deque.popleft()
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
            res.append(deque[0])
        return res


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    s = Solution()
    result = s.maxSlidingWindow2(nums=nums, k=k)
    print(result)
