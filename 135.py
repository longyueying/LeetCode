class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        length = len(ratings)
        res = [0]*length
        dic = {}
        for i in range(length):
            dic.setdefault(ratings[i], [])
            dic[ratings[i]].append(i)
        ratings_sort = list(set(ratings))
        ratings_sort.sort()
        for rateing in ratings_sort:
            for index in dic[rateing]:
                if index-1<0 and index+1>=length:
                    res[index]=1
                elif index-1<0:
                    if ratings[index+1]<ratings[index]:
                        res[index] = res[index+1]+1
                    else:
                        res[index] = 1
                elif index+1>=length:
                    if ratings[index-1] < ratings[index]:
                        res[index] = res[index-1]+1
                    else:
                        res[index] = 1
                else:
                    if ratings[index-1] < ratings[index] and ratings[index+1]<ratings[index]:
                        res[index] = max(res[index-1], res[index+1])+1
                    elif ratings[index+1]<ratings[index]:
                        res[index] = res[index + 1] + 1
                    elif ratings[index-1] < ratings[index]:
                        res[index] = res[index - 1] + 1
                    else:
                        res[index] = 1
                print(res)
        print(res)
        return sum(res)

if __name__=="__main__":
    s = Solution()
    print(s.candy([29,51,87,87,72,12]))



