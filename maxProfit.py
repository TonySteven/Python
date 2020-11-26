#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 11/26/20 15:53
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : maxProfit.py

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost, profit = float("+inf"), 0
        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
        return profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    s = Solution()
    result = s.maxProfit(prices=prices)
    print(result)
