import sys

class solution(object):
    res = -1
    def run(self):
        list_num = list(map(int, sys.stdin.readline().strip().split()))
        if len(list_num)<2:
            return -1
        a = list_num[0]
        b = list_num[1]
        total = a+b

        i = 1
        tmp = 0

        while tmp < total:
            tmp = tmp+i
            i+=1
        self.end = i-1

        if tmp!=total:
            return -1
        else:
            self.find(1, 0, 0, a)
            return self.res
    def find(self,now_num, now_sum,length, target):
        if now_sum==target:
            if self.res==-1:
                self.res = length
            else:
                if self.res > length:
                    self.res=length
            return
        if now_num > self.end:
            return
        self.find(now_num + 1, now_sum+now_num, length+1, target)
        self.find(now_num + 1, now_sum, length, target)

s = solution()
print(s.run())