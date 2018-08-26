import numpy as np

class solution(object):
    def m(self, pre, p):
        self.dic = {}
        self.sovler(0, pre, 0, '', p)
        return self.dic

    def sovler(self, i, pre, complain, status, p):
        if i >= p:
            self.dic[status] = complain
            return
        self.sovler(i + 1, pre, complain + list(pre[i]).count('1'), status + '0', p)
        self.sovler(i + 1, pre, complain + list(pre[i]).count('0'), status + '1', p)



s = solution()
res = []
with open('B-large.in') as f:
    t = int(f.readline().strip())
    for i in range(t):
        n, m, p = list(map(int, f.readline().strip().split()))
        preference = []
        for j in range(n):
            line = list(f.readline().strip())
            preference.append(line)
        preference = np.array(preference).transpose()

        combine = s.m(preference, p)

        fobid = []
        for j in range(m):
            line = f.readline().strip()
            fobid.append(line)

        for fob in fobid:
            combine.pop(fob)
        res.append(min(list(combine.values())))


with open('anwer.out','w') as f:
    for i, c in enumerate(res):
        string = "Case #{}: {}\n".format(i+1, c)
        f.write(string)












