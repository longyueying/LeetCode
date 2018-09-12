import sys
n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))
res = 1
if n==1:
    prefix = nums[0] >> 7
    if bin(prefix)!='0b0':
        res = 0
elif n==2:
    prefix = nums[0] >> 5
    if bin(prefix) != '0b110':
        res = 0
elif n==3:
    prefix = nums[0] >> 4
    if bin(prefix)!='0b1110':
        res = 0
elif n==4:
    prefix = nums[0] >> 3
    if bin(prefix) != '0b11110':
        res = 0

for i in range(1, n):
    if res==0:
        break
    prefix = nums[i]>>6
    if bin(prefix)!='0b10':
        res = 0
print(res)

