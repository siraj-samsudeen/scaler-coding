# https://www.scaler.com/academy/mentee-dashboard/class/27004/assignment/problems/216?navref=cl_pl_pr
# 99_recover_binary_search_tree.py
# leetcode problem expects the tree to be modified whereas here we are expected to return the swapped nodes

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def recoverTree(self, A):
        def inorder(root):
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []
        
        tree = inorder(A)
        n = len(tree)

        # ideally not needed - but this is better than an IndexOutofBoundsError
        if n < 2:
            return tree

        item1 = item2 = None

        # we don't want i to touch the last index since we use i+1
        for i in range(n-1):
            if tree[i] > tree[i+1]:
                item1 = tree[i]
                break
        for i in range(n-1, 0, -1):
            if tree[i] < tree[i-1]:
                item2 = tree[i]
                break
        
        return [item1, item2]
    
    # using morris
    def recoverTree(self, A):
        # tomorrow