# https://www.scaler.com/academy/mentee-dashboard/class/27001/homework/problems/221?navref=cl_pl_pr
# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    def isValidBST(self, A):
        root = A
        min_val = float('-inf')
        max_val = float('inf')
        
        def is_valid_range(root, min_val, max_val):
            # An empty node is valid as the leaf nodes will have 2 empty child nodes
            if root is None: return True
            if root.val < min_val or root.val > max_val:
                return False
            
            return is_valid_range(root.left, min_val, root.val-1) and is_valid_range(root.right, root.val+1, max_val)
        return +is_valid_range(root, min_val, max_val)             