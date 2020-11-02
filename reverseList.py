#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 11/2/20 22:57
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : reverseList.py
from Cython.Compiler.ExprNodes import ListNode


class Solution:
    @staticmethod
    def reverseList(head: ListNode) -> ListNode:
        if not head: return None
        prev = None
        cur = head
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkList(object):
    def __init__(self):
        self.head = None

    def initList(self, data):
        # 创建头结点
        self.head = ListNode(data[0])
        r = self.head
        p = self.head
        # 逐个为 data 内的数据创建结点, 建立链表
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return r

    def printlist(self, head):
        if head == None:
            return
        node = head
        while node != None:
            print(node.val, end='')
            node = node.next


if __name__ == '__main__':
    l = LinkList()
    data1 = [1, 2, 3, 4, 5]
    l1 = l.initList(data1)
    l2 = Solution.reverseList(l1)
    l.printlist(l2)
