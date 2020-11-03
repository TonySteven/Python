#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 11/3/20 11:50
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : mergeTwoLists.py
from Cython.Compiler.ExprNodes import ListNode


class Solution:
    @staticmethod
    def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
        # 1.初始化： 伪头节点 dumdum ，节点 curcur 指向 dumdum 。
        cur = dum = ListNode(0)
        # 2. 循环合并：当l1或者l2为空时跳出
        while l1 and l2:

            if l1.val < l2.val:
                # 2.1 curcur 的后继节点指定为l1，l1向前走一步
                cur.next, l1 = l1, l1.next
            else:
                # 2.2 curcur 的后继节点指定为l2，l2向前走一步
                cur.next, l2 = l2, l2.next
            # 节点curcur向前走一步，即:cur = cur.nextcur = cur.next 。
            cur = cur.next
        # 3. 合并剩余尾部： 跳出时有两种情况, 即l1为空或者l2为空。
        # 3.1 如果if不为空 l1添加至cur之后 否则将l2添加到cur之后
        cur.next = l1 if l1 else l2

        # 4. 返回值： 合并链表在伪头结点dum之后，因此返回dum.next即可。
        return dum.next


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
    data1 = [1, 2, 4, 5]
    data2 = [1, 3, 4, 5]
    l1 = l.initList(data1)
    l2 = l.initList(data2)
    result = Solution.mergeTwoLists(l1,l2)
    l.printlist(result)