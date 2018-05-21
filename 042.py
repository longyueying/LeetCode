class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0:
            return 0

        sum = 0
        flag = False

        begin = 0
        while (begin < (len(height)-1) and height[begin] <= height[begin+1]):
            begin+=1
        end = begin

        while end < len(height)-1:
            if flag == False and height[end] < height[end+1]:
                flag = True
            if flag == True and height[end] > height[end+1]:

                if height[begin] <= height[end]:
                    h = height[begin]
                else:
                    h = height[end]
                    for i in range(end, len(height)):
                        if height[i]>=height[end] and height[i] < height[begin]:
                            end = i
                            h = height[end]
                        elif height[i] >= height[begin]:
                            end = i
                            h = height[begin]
                            break
                sum  = sum + (h* (end - begin -1))
                for i in range(begin+1, end):
                    if height[i] < h:
                        sum-=height[i]
                    else:
                        sum-=h
                begin = end
                while (begin < (len(height) - 1) and height[begin] <= height[begin + 1]):
                    begin += 1
                end = begin
                flag = False
            end+=1

        if end == len(height)-1 and flag==True:
            if height[begin] < height[end]:
                h = height[begin]
            else:
                h = height[end]
            sum = sum + (h * (end - begin - 1))
            for i in range(begin + 1, end):
                if height[i] < h:
                    sum -= height[i]
                else:
                    sum -= h
        return sum

if __name__=="__main__":
    solu = Solution()
    print(solu.trap([2,4,1,2,3,0,6,8,5,9,0,8,5,8,3]))