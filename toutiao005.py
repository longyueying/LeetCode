import sys

if __name__ == "__main__":
    l = sys.stdin.readline().strip()
    line = list(map(int, l.split(' ')))
    n = line[0]

    l = sys.stdin.readline().strip()
    line = list(map(int, l.split(' ')))
    m = line[0]

    l = sys.stdin.readline().strip()
    line = list(map(int, l.split(' ')))

    d = []
    i=0
    tmp = m
    while i < len(line):
        if line[i] > line[i+1]:
            t = m-line[i]+line[i+1]
            d.append([t,line[i]])
            if t+1>m:
                tmp = t+1
        else:
            d.append([line[i+1],line[i]])
        i+=2
    d.sort()

    dp = [0]*tmp

    for i in range(d[0][0],tmp):
        dp[i] = 1
    for dur in d:
        for i in range(dur[0],tmp):
            dp[i] = max(1+dp[dur[1]], dp[dur[1]])
    print(dp[-1])

