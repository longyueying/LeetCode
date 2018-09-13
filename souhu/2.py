import sys

def solver():
    a = int(sys.stdin.readline().strip())
    if a==3:
        return 2
    if a==2:
        return 3
    if a==1:
        return 1
    if a == 0:
        return 0

    i = 1
    while not (i * (i + 1) / 2 >= a and (i * (i + 1) / 2 - a) % 2 == 0):
        i += 1
    return i
print(solver())