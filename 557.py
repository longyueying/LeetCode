class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = s[::-1]
        print(a)
        s = a.split(' ')
        s = s[::-1]
        return " ".join(s)

if __name__ == "__main__":
    solu = Solution()
    print(solu.reverseWords("Let's take LeetCode contest"))