import sys

if __name__ == "__main__":
    l = sys.stdin.readline().strip()
    line = list(map(int, l.split(',')))

    M = line[0]
    N = line[1]

    arr = []
    for i in range(M):
        l = sys.stdin.readline().strip()
        line = list(map(int, l.split(',')))
        arr.append(line)

    P = 0
    for i in range(M):
        for j in range(N):
            if arr[i][j] == 1:
                if  i==0:
                    if j == 0:
                        arr[i][j] = P+1
                        P+=1
                    else:
                        if arr[i][j-1] != 0:
                            arr[i][j] = arr[i][j-1]
                        else:
                            arr[i][j] = P + 1
                            P += 1
                else:
                    if j==0:
                        if arr[i-1][j] != 0:
                            arr[i][j] = arr[i-1][j]
                        elif j+1<N and arr[i-1][j+1] != 0:
                            arr[i][j] = arr[i-1][j+1]
                        else:
                            P+=1
                            arr[i][j] = P
                    else:
                        if arr[i-1][j] != 0:
                            arr[i][j] = arr[i-1][j]
                        elif arr[i-1][j-1] !=0:
                            arr[i][j] = arr[i - 1][j - 1]
                        elif j+1<N and arr[i-1][j+1] != 0:
                            arr[i][j] = arr[i-1][j+1]
                        elif arr[i][j-1]!=0:
                            arr[i][j] = arr[i][j-1]
                        else:
                            P+=1
                            arr[i][j] = P
    for i in range(M):
        for j in range(N):

    print(P)
