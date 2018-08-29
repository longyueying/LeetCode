import sys

if __name__ == "__main__":
    l = sys.stdin.readline().strip()
    line = list(map(int, l.split(' ')))
    n = line[0]

    l = sys.stdin.readline().strip()
    a = list(map(int, l.split(' ')))

    l = sys.stdin.readline().strip()
    b = list(map(int, l.split(' ')))

    dp_a = [[0]* n for i in range(n)]
    dp_b = [[999999999] * n for i in range(n)]

    res = 0

    for i in range(n):
        dp_a[i][i] = a[i]
        dp_b[i][i] = b[i]
    for i in range(n):
        for j in range(i+1,n):
            if a[j] > dp_a[i][j-1]:
                dp_a[i][j] = a[j]
            else:
                dp_a[i][j] = dp_a[i][j-1]

            if b[j] < dp_b[i][j-1]:
                dp_b[i][j] = b[j]
            else:
                dp_b[i][j] = dp_b[i][j-1]
    for i in range(n):
        for j in range(i,n):
            if dp_a[i][j] < dp_b[i][j]:
                res+=1
    print(res)
