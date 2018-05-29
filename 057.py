# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if len(intervals)==0:
            return [newInterval]
        index = self.binarySearch(intervals, newInterval, 0, len(intervals)-1)
        if index == len(intervals):
            if intervals[-1].end < newInterval.start:
                intervals.append(newInterval)
                return intervals
            else:
                if intervals[-1].end < newInterval.end:
                    intervals[-1].end = newInterval.end
                return intervals
        else:
            intervals.insert(index, newInterval)
            if index==0:
                i = 0
            else:
                i = index-1

            end = len(intervals) - 1
            while i < end:
                if intervals[i].end >= intervals[i + 1].start:
                    if intervals[i].end < intervals[i + 1].end:
                        intervals[i].end = intervals[i + 1].end
                    intervals.pop(i + 1)
                    end -= 1
                else:
                    break
            i=i+1
            while i < end:
                if intervals[i].end >= intervals[i + 1].start:
                    if intervals[i].end < intervals[i + 1].end:
                        intervals[i].end = intervals[i + 1].end
                    intervals.pop(i + 1)
                    end -= 1
                else:
                    return intervals
        return intervals

    def binarySearch(self, intervals,newInterval, begin, end):
        while begin <= end:
            mid = int((begin+end)/2)
            if intervals[mid].start == newInterval.start:
                return mid
            if intervals[mid].start < newInterval.start:
                begin = mid + 1
            else:
                end = mid - 1
        return begin

    # def sort(self, intervals, i, j):
    #     begin = i
    #     end = j
    #     if begin < end:
    #         key = intervals[begin]
    #         while begin < end:
    #             while begin < end and intervals[end].start > key.start:
    #                 end-=1
    #             intervals[begin] = intervals[end]
    #             while begin < end and intervals[begin].start <= key.start:
    #                 begin+=1
    #             intervals[end] = intervals[begin]
    #         intervals[begin] = key
    #         self.sort(intervals, i, begin -1)
    #         self.sort(intervals, begin+1, j)
    #     else:
    #         return


if __name__=="__main__":
    solu = Solution()
    a = Interval(1,3)
    b = Interval(2,5)
    c = Interval(6,9)
    d = Interval(8, 10)
    e = Interval(12,16)
    f = Interval(4,8)
    l = [a,c]
    ret = solu.insert(l, b)

    for i in range(len(ret)):
        print(ret[i].end)