#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-19
# @Author  : steven
# @Email   : stevenl365404@gmail.com
# @File    : isValidSubsequence.py

# 快速排序

def qsort(L):
    if len(L) <= 1:
        return L
    return qsort([lt for lt in L[1:] if lt < L[0]]) + L[0:1] + qsort([ge for ge in L[1:] if ge >= L[0]])


if __name__ == '__main__':
    array = [8, 10, 9, 6, 4]
    print(qsort(array))
