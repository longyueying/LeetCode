class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        dic = {}
        length = len(formula)
        i = 0
        tmp = []
        while i < length:
            while not ((ord('a')<=ord(formula[i]) and ord(formula[i])<=ord('z')) or (ord('A')<=ord(formula[i]) and ord(formula[i])<=ord('Z'))):
                tmp.append(formula[i])
                i+=1
                if i >= length:
                    break
            if i >= length:
                break
            begin = i
            i+=1
            while i< length and ((ord('a')<=ord(formula[i]) and ord(formula[i])<=ord('z'))):
                i+=1
            tmp.append(formula[begin:i])
            dic[formula[begin:i]] = 0

        formula = tmp

        print(formula)
        print(dic)

        def solver(stack, times):
            pass
if __name__ == '__main__':
    solu = Solution()
    print(solu.countOfAtoms('H2O2He3Mg4'))