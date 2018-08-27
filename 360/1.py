import sys


n = int(sys.stdin.readline().strip())
res = 0
if n <= 1:
    print(0)
else:
    x_min, y_min = list(map(int, sys.stdin.readline().strip().split()))
    x_max = x_min
    y_max = y_min

    for i in range(1, n):
        x, y = list(map(int, sys.stdin.readline().strip().split()))
        if x < x_min:
            x_min = x
        elif x > x_max:
            x_max = x

        if y < y_min:
            y_min = y
        elif y > y_max:
            y_max = y
    side = max(y_max - y_min, x_max - x_min)
    squer = side * side
    print(squer)