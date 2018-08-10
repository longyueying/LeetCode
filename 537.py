class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = a[:-1]
        b = b[:-1]
        a = a.split('+')
        b = b.split('+')

        a_res = int(a[0])*int(b[0]) - int(a[1])*int(b[1])
        b_res = int(a[0])*int(b[1]) + int(a[1])*int(b[0])

        return str(a_res)+'+'+str(b_res)+'i'