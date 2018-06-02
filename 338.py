class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        bits_list = [0]
        for i in range(1, num+1):
            if i & 1 == 0:
                bits_list.append(bits_list[int(i/2)])
            else:
                bits_list.append(bits_list[-1]+1)
        return bits_list

if __name__ == '__main__':
    solu = Solution()
    print(solu.countBits(5))