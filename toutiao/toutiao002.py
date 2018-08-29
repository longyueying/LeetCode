import sys

if __name__ == "__main__":
    l = sys.stdin.readline().strip()
    line = list(map(int, l.split(',')))

    m = line[0]

    res = []
    for i in range(m):
        l = sys.stdin.readline().strip()
        line = list(l.split(';'))

        for duration in line:
            d = list(map(int, duration.split(',')))

            if len(res) == 0:
                res.append(d)
            elif d[0] >= res[-1][0]:
                if d[0] > res[-1][1]:
                    res.append(d)
                else:
                    res[-1][0] = min(d[0], res[-1][0])
                    res[-1][1] = max(d[1], res[-1][1])
            else:
                i = 0
                while i < len(res) and d[0] > res[i][1]:
                    i+=1
                if d[1] < res[i][0]:
                    res.insert(i, d)

                elif d[1] <= res[i][1]:
                    res[i][0] = min(d[0], res[i][0])
                else:
                    res[i][0] = min(d[0], res[i][0])
                    res[i][1] = d[1]
                    while i < len(res)-1 and res[i][1] >= res[i+1][0]:
                       res[i][1] = max(res[i][1], res[i+1][1])
                       res.pop(i+1)
    s= ''
    for d in res:
        s+='{},{};'.format(d[0],d[1])
    if len(s)>0:
        s = s[:-1]
    print(s)
