import sys

def binarysearch(arr, target):
    i, j = 0, len(arr) - 1
    while i <= j:
        mid = int((i + j) / 2)
        if arr[mid] == target: return True
        if arr[mid] < target:
            i = mid + 1
        else:
            j = mid - 1
    return False

def solver():
    m,n = list(map(int, sys.stdin.readline().strip().split()))
    matrix = []
    for i in range(m):
        line = list(map(int, sys.stdin.readline().strip().split()))
        matrix.append(line)
    target = int(sys.stdin.readline().strip())
    m = len(matrix)
    for i in range(m):
        if binarysearch(matrix[i],target):
            return 'true'
    return 'false'

print(solver())