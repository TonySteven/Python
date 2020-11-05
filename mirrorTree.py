#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 11/5/20 16:45
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : mirrorTree.py

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
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root: return
        tmp = root.left
        root.left = self.mirrorTree(root.right)
        root.right = self.mirrorTree(tmp)
        return root

if __name__ == '__main__':
    t1 = [4,2,7,1,3,6,9]
    tree1 = Tree()
    for i in t1:
        tree1.add(i)


    s = Solution()
    result = s.mirrorTree(tree1.root)
    print(result)