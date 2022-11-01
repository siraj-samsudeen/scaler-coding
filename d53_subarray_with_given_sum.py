# https://www.scaler.com/academy/mentee-dashboard/class/20528/assignment/problems/4116
# Given an array of positive integers A and an integer B,
# find and return first continuous subarray which adds to B.
# If the answer does not exist return an array with a single element "-1".
# First sub-array means the sub-array for which starting index in minimum.

# A simple problem turned out to be very complex when handling all the boundary cases
def test():
    s = Solution()
    assert s.solve([0], 0) == []
    assert s.solve([1], 1) == [1]
    assert s.solve([1], 2) == [-1]
    assert s.solve([1, 2], 3) == [1, 2]
    assert s.solve([1, 2], 4) == [-1]
    assert s.solve([1, 2], 2) == [2]

    assert s.solve([1, 2, 3, 4, 5], 5) == [2, 3]
    assert s.solve([5, 10, 20, 100, 105], 110) == [-1]


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        arr = A
        k = B
        n = len(arr)

        left = right = sum = 0
        while left < right or right < n:
            if sum == k:
                return arr[left:right]
            elif sum < k:
                if right == n:
                    break
                sum += arr[right]
                right += 1
            else:
                sum -= arr[left]
                left += 1

        return [-1]
