class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        res = []

        def solver(boxes, s):
            if len(boxes)==0:
                res.append(s)
            else:
                i = 0
                while i < len(boxes):
                    tmp = 1
                    begin = i
                    while i < len(boxes)-1 and boxes[i+1]==boxes[i]:
                        i+=1
                        tmp+=1
                    end = i
                    i+=1
                    boxes_tmp = [num for num in boxes[0:begin]] + [num for num in boxes[end+1:]]
                    solver(boxes_tmp,s+tmp*tmp)

        solver(boxes, 0)
        return max(res)

if __name__=="__main__":
    solu = Solution()
    print(solu.removeBoxes([1,2,3,4,5,6,7,8,9,10]))
