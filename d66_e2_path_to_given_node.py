# https://www.scaler.com/academy/mentee-dashboard/class/26992/assignment/problems/11837/?navref=cl_pb_nv_tb
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        res = []

        def path(root, k):
            if root is None:
                return False
            if root.val == k:
                res.append(root.val)
                return True
            if path(root.left, k) or path(root.right, k):
                res.append(root.val)
                return True
            return False
        
        path(A, B)
        return res[::-1]

# Top down approach based on the scaler solution
    def solve(self, A, B):
        res = []

        def path(root, k):
            if root is None:
                return False
            
            # append the current node - if we can't find a match, then we will pop it back
            res.append(root.val)
            if root.val == k:
                return True
            if path(root.left, k) or path(root.right, k):
                return True
            else:
                res.pop()
                return False
        
        path(A, B)
        return res

