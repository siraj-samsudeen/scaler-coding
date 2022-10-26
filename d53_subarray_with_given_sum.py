# https://www.scaler.com/academy/mentee-dashboard/class/20528/assignment/problems/4116
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        a = A
        k = B
        n = len(A)
        
        p1 = p2 = 0
        sum = a[0]
        
        while p1 < n and p2 < n:
            if sum == k:
                return a[p1:p2+1]
            elif sum < k:
                p2 += 1
                if p2 != n: sum += a[p2]
            else:
                sum -= a[p1]
                p1 +=1
        # no match found so far
        return [-1]

# print(Solution().solve([1, 2, 3, 4, 5], 5))                
# print(Solution().solve( [ 5, 10, 20, 100, 105 ], 110))