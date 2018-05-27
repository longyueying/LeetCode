class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        str_list = s.split(sep=' ')
        for i in range(len(str_list)-1, -1, -1):
            if len(str_list[i]) != 0:
                return len(str_list[i])
        return 0


if __name__ == "__main__":
    solu = Solution()
    print(solu.lengthOfLastWord('a                          '))