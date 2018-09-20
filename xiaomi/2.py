import sys

class solution(object):

    def run(self):
        self.n,self.m = list(map(int, sys.stdin.readline().strip().split()))
        self.nums = list(map(int, sys.stdin.readline().strip().split()))
        self.res = sum(self.nums)
        self.length = len(self.nums)
        max_val = max(self.nums)
        if  max_val > sum(self.nums):
            print(max_val)
        else:
            self.solver([],0,self.m)
            print(self.res)


    def solver(self, partition,begin, remain_part):
        if remain_part==1:
            tmp = sum(self.nums[begin:])
            if tmp >= self.res:
                return
            partition.append(tmp)
            tmp = max(partition)
            self.res = tmp
            partition.pop()
            return
        tmp = 0
        for end in range(begin, self.length-remain_part+1):
            tmp = tmp+self.nums[end]
            if tmp>=self.res:
                return
            partition.append(tmp)
            self.solver(partition, end+1, remain_part-1)
            partition.pop()


s = solution()
s.run()