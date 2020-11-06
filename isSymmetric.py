#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 11/6/20 10:02
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : isSymmetric.py

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
    def isSymmetric(self, root: TreeNode) -> TreeNode:
        def recur(L, R):
            if not L and not R: return True
            if not L or not R or L.val != R.val: return False
            return recur(L.left, R.right) and recur(L.right, R.left)

        return recur(root.left, root.right) if root else True


if __name__ == '__main__':
    t1 = [1,2,2,3,4,4,3]
    tree1 = Tree()
    for i in t1:
        tree1.add(i)

    s = Solution()
    result = s.isSymmetric(tree1.root)
    print(result)
