#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 11/5/20 01:17
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : isSubStructure.py


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):
        self.root = TreeNode(None)
        self.t = []

    def add(self, val):
        treenode = TreeNode(val)
        if self.root.val == None:
            self.root = treenode
            self.t.append(self.root)
            return
        else:
            tree_exist_node = self.t[0]
            print(self.t[0].val)
            if tree_exist_node.left == None:
                tree_exist_node.left = treenode
                self.t.append(tree_exist_node.left)
                return
            else:
                tree_exist_node.right = treenode
                self.t.append(tree_exist_node.right)
                self.t.pop(0)


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(A, B):
            if not B: return True
            if not A or A.val != B.val: return False
            return recur(A.left, B.left) and recur(A.right, B.right)

        return bool(A and B) and (
                recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))


if __name__ == '__main__':
    t1 = [3,4,5,1,2]
    tree1 = Tree()
    # tree1.add(1)
    # tree1.add(2)
    # tree1.add(3)
    for i in t1:
        # print("-----------", i)
        tree1.add(i)

    t2 = [4,1]
    tree2 = Tree()
    # tree2.add(3)
    # tree2.add(1)
    for i in t2:
        # print("-----------", i)
        tree2.add(i)

s = Solution()
result = s.isSubStructure(tree1.root, tree2.root)
print(result)
