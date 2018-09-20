import sys
n = int(sys.stdin.readline().strip())
nums = []
for i in range(n):
    nums.append(int(sys.stdin.readline().strip()))

res = 0

for i in range(n-1):
    for j in range(n-i-1):
        if nums[j]>nums[j+1]:
            tmp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = tmp
            res+=1
print(res)