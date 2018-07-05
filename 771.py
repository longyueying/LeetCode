class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        j_list = list(J)
        s_list = list(S)

        for j in j_list:
            count+=s_list.count(j)
        return count