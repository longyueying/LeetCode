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

        i=0
        tmp = []
        while i < len(formula):

            if formula[i].isdigit():
                begin = i
                while i+1 < len(formula) and formula[i+1].isdigit():
                    i+=1
                end = i
                num = 0
                for j in range(begin,end+1):
                    num = num*10 + int(formula[j])
                tmp.append(str(num))
                i+=1
            else:
                tmp.append(formula[i])
                i+=1
        formula = tmp

        i = 0
        while i < len(formula):
            if formula[i] == ')':
                end = i
                if i+1 < len(formula) and formula[i+1].isdigit():
                    times = int(formula[i+1])
                    formula.pop(i+1)
                j = i-1
                while formula[j] != '(':

                    if not formula[j].isdigit():
                        if formula[j+1].isdigit():
                            formula[j+1] =  str( int(formula[j+1]) * times)
                        else :
                            formula.insert(j+1,str(times))
                            end +=1
                    j-=1
                begin = j
                formula.pop(end)
                formula.pop(begin)
                i-=2
            else:
                i+=1

        i = 0
        while i < len(formula):
            if i+1 < len(formula) and formula[i+1].isdigit():
                dic[formula[i]]+= int(formula[i+1])
                i+=2
            else:
                dic[formula[i]] += 1
                i += 1
        tmp = []
        for k in dic:
            tmp.append(k)
        tmp.sort()
        s = []
        for k in tmp:
            s.append(k)
            if dic[k] > 1:
                s.append(str(dic[k]))
        return ''.join(s)





if __name__ == '__main__':
    solu = Solution()
    print(solu.countOfAtoms('H2O'))