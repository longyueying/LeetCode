#Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals)==0:
            return []
        self.sort(intervals, 0, len(intervals)-1)
        for i in range(len(intervals)):
            print(intervals[i].start)
        ret = []
        ret.append(intervals[0])
        for i in range(1, len(intervals)):
            if ret[-1].end >= intervals[i].start:
                if ret[-1].end < intervals[i].end:
                    ret[-1].end = intervals[i].end
            else:
                ret.append(intervals[i])
        return ret

    def sort(self, intervals, begin, end):
        if begin < end:
            loc = begin
            low = begin
            high = end
            while  high > low:
                while high >=loc and intervals[high].start >= intervals[loc].start:
                    high-=1
                if high > loc:
                    temp = intervals[high]
                    intervals[high] = intervals[loc]
                    intervals[loc] = temp
                    loc = high
                while low<=loc and intervals[low].start <= intervals[loc].start:
                    low+=1
                if low<loc:
                    temp = intervals[low]
                    intervals[low] = intervals[loc]
                    intervals[loc] = temp
                    loc = low
            self.sort(intervals,begin, loc-1)
            self.sort(intervals,loc+1,end)
if __name__=="__main__":
    solu = Solution()
    a = Interval(1,4)
    b = Interval(0,2)
    c = Interval(3,5)
    d = Interval(15, 18)

    l = [a,b,c]
    solu.merge(l)