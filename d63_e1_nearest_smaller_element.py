# https://www.scaler.com/academy/mentee-dashboard/class/26983/assignment/problems/332?navref=cl_tt_nv
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        arr = A
        ans = [-1]* len(arr)
        
        stack = [arr[0]]
        for i in range(1,len(arr)):
            current = arr[i]
            while stack and current < stack[-1]:
                stack.pop()
            if stack and stack[-1] < current:
                ans[i] = stack[-1]
            stack.append(current)
        
        return ans