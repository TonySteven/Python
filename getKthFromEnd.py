#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 11/1/20 23:51
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : getKthFromEnd.py


# 输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。
#
#  
#
# 示例：
#
# 给定一个链表: 1->2->3->4->5, 和 k = 2.
#
# 返回链表 4->5.
from Cython.Compiler.ExprNodes import ListNode


class Solution:
    @staticmethod
    def getKthFromEnd(head: ListNode, k: int) -> ListNode:
        former, latter = head, head
        for _ in range(k):
            if not former:
                return
            former = former.next
        while former:
            former, latter = former.next, latter.next
        return latter


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
    l2 = Solution.getKthFromEnd(l1, k=3)
    l.printlist(l2)
