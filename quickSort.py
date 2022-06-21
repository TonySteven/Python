#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 12/23/20 11:29
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : quickSort.py

# Best: O(nlog(n)) time | O(log(n)) space
# Average: O(nlog(n)) time | O(log(n)) space
# Worst: O(n^2) time | O(log(n)) space

# 算法核心: 分治算法很好的应用. divide and conquer
# 快速排序和归并排序很相似, 都是先将一个大数组一分为二,然后对两个子序列分别排序,再合并结果,完成整个数组排序.
# 快排和归并排序 有两点不同:
# 1. 快排不是直接的从中间分开,而是把大的数放到一个子序列,小的数放在另一个里面. (指针扫描)
# 具体来讲,我们先挑选一个枢值(pivot), 让序列中所有元素和这个pivot一一比较.
# 如果大于或者等于就把它放在右面,反之则放在左边.
# 再进行子序列排序.(递归)
# 2. 合并时,不需要做任何的比较,直接进行即可.


# 快排方法
def quick_sort(array):
    # 快排核心算法
    quick_sort_helper(array, 0, len(array) - 1)
    # 排序后返回数组
    return array


def quick_sort_helper(array, start_index, end_index):
    # 如果开始指针大于等于结束指针 则直接返回
    if start_index >= end_index:
        return

    # 定义pivot left right 指针
    pivot_index = start_index
    left_index = start_index + 1
    right_index = end_index

    #
    while right_index >= left_index:
        if array[left_index] > array[pivot_index] > array[right_index]:
            swap(left_index, right_index, array)

        if array[left_index] <= array[pivot_index]:
            left_index += 1

        if array[right_index] >= array[pivot_index]:
            right_index -= 1

    swap(pivot_index, right_index, array)

    left_subarray_is_smaller = right_index - 1 - start_index < end_index - (right_index + 1)

    if left_subarray_is_smaller:
        quick_sort_helper(array, start_index, right_index - 1)
        quick_sort_helper(array, right_index + 1, end_index)
    else:
        quick_sort_helper(array, right_index + 1, end_index)
        quick_sort_helper(array, start_index, right_index - 1)


# 交换方法
def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


# main函数 程序入口
if __name__ == '__main__':
    array = [8, 5, 2, 9, 5, 6, 3]
    print(quick_sort(array))
