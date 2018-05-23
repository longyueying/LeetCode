class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        n1 = list(num1)
        n2 = list(num2)

        n1.reverse()
        n2.reverse()
        res = [0] * (len(n1) + len(n2))


        for i in range(len(n1)):
            for j in range(len(n2)):
                temp = int(n1[i]) * int(n2[j])
                high = int(temp/10)
                low = int(temp%10)
                res[i+j] = res[i+j]+low
                res[i+j+1] = res[i+j+1] + high


        for i in range(len(res)-1):
            if res[i] > 9:
                res[i+1] = res[i+1] + int(res[i]/10)
                res[i] = int(res[i]%10)
        res.reverse()

        for i in range(len(res)):
            res[i] = chr(ord('0')+res[i])

        i = 0
        while i < len(res):
            if res[i] != '0':
                break
            i+=1
        if len(res[i:])!=0:
            return ''.join(res[i:])
        else:
            return '0'


if __name__=='__main__':
    solu = Solution()
    print(solu.multiply("123", "456"))


