#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 12/19/20 00:02
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : isValidSubsequence.py

def isValidSubsequence(array, sequence):
    # Write your code here.
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)


if __name__ == '__main__':
    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [1, 6, -1, 10]
    result = isValidSubsequence(array, sequence)
    print(result)
