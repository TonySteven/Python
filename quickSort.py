#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 12/23/20 11:29
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : quickSort.py

# Best: O(nlog(n)) time | O(log(n)) space
# Average: O(nlog(n)) time | O(log(n)) space
# Worst: O(n^2) time | O(log(n)) space


# 快排方法
def quickSort(array):
    # 快排核心算法
    quickSortHelper(array, 0, len(array) - 1)
    # 排序后返回数组
    return array


def quickSortHelper(array, startIdx, endIdx):
    # 如果开始指针大于等于结束指针 则直接返回
    if startIdx >= endIdx:
        return

    # 定义pivot left right 指针
    pivotIdx = startIdx
    leftIdx = startIdx + 1
    rightIdx = endIdx

    #
    while rightIdx >= leftIdx:
        if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
            swap(leftIdx, rightIdx, array)

        if array[leftIdx] <= array[pivotIdx]:
            leftIdx += 1

        if array[rightIdx] >= array[pivotIdx]:
            rightIdx -= 1

    swap(pivotIdx, rightIdx, array)

    leftSubarrayIsSmaller = rightIdx - 1 - startIdx < endIdx - (rightIdx + 1)

    if leftSubarrayIsSmaller:
        quickSortHelper(array, startIdx, rightIdx - 1)
        quickSortHelper(array, rightIdx + 1, endIdx)
    else:
        quickSortHelper(array, rightIdx + 1, endIdx)
        quickSortHelper(array, startIdx, rightIdx - 1)


## 交换方法
def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


# main函数 程序入口
if __name__ == '__main__':
    array = [8, 5, 2, 9, 5, 6, 3]
    print(quickSort(array))
