import sys
n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))

begin = 0
end = 0
res = 1
flag = True
change_pos = 0

while end < n-1:
    while end+2< end and nums[end] == nums[end+2]:
        begin+=1
        end+=1
        change_pos=end
    if nums[end] >= nums[end+1]:
        if res < end-begin+1:
            res = end-begin+1
        if flag == False:
            begin=change_pos+1
            end = change_pos+1
        else:
            flag=False
            change_pos=end
    end+=1
if res < end - begin + 1:
    res = end - begin + 1
print(res)
