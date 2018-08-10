class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        dic = {'U':0, 'D':0, 'R':0,'L':0}

        for i in range(len(moves)):
            dic[moves[i]]+=1
        return dic['R']==dic['L'] and dic['U']==dic['D']