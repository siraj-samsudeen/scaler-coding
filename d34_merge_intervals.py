# https://www.scaler.com/academy/mentee-dashboard/class/16127/assignment/problems/58
# 56_merge_intervals.py
# leetcode problem is slightly different that all the data is in the array
# here a new interval is given and we have to put it in the right place in the array

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __repr__(self) -> str:
        return f"({self.start, self.end}"

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        # new is to the left of all the intervals - so just merge them
        
        ans = []
        for i, currentInterval in enumerate(intervals):
            if newInterval.end < currentInterval.start:
                return ans + [newInterval] + [intervals][i:]
            elif currentInterval.end < newInterval.start:
                ans.append(currentInterval)
            else :
                newInterval.start = min(currentInterval.start, newInterval.start)
                newInterval.end = max(currentInterval.end, newInterval.end)
        ans.append(newInterval)
        return ans
    
A = [ Interval(3, 6), Interval(8, 10) ]
B = Interval(1, 2)    
print(Solution().insert(A, B))