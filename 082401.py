from sys import stdin

n = int(stdin.readline().strip())
score = stdin.readline().strip().split()
q = int(stdin.readline().strip())
invited = []
for i in range(q):
    invited.append(stdin.readline().strip().split())
    print(score[int(invited[i][0]) - 1:int(invited[i][1])].count(invited[i][2]))