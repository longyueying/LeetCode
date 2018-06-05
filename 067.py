class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = list(a)
        b = list(b)
        a.reverse()
        b.reverse()

        if len(a) < len(b):
            temp = a
            a = b
            b = temp

        carry = 0
        i = 0
        ret = []
        while i< len(b):
            sum = int(a[i])+int(b[i])+carry
            carry = int(sum/2)
            ret.append(chr(ord('0')+(sum%2)))
            i+=1
        while i <len(a):
            sum = int(a[i])+carry
            carry = int(sum/2)
            ret.append(chr(ord('0')+(sum%2)))
            i+=1
        if carry==1:
            ret.append('1')
        ret.reverse()
        return ''.join(ret)

if __name__=='__main__':
    solu = Solution()
    print(solu.addBinary("101", '1011'))