# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        intervals.sort()
        result = []
        result.append(intervals[0])
        for i in range(1, len(intervals)):
            a = result.pop()
            b = intervals[i]
            if a.end >= b.start:
                result.append(Interval(min(a.start, b.start), max(a.end, b.end)))
            else:
                result.append(a)
            result.append(b)

        return result











if __name__ == '__main__':
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(Solution().merge(intervals))
