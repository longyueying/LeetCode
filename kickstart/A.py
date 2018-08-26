
res = []
with open('A-large.in') as f:
    n = int(f.readline().strip())
    for i in range(n):
        n, k = list(map(int, f.readline().strip().split()))
        expire = list(map(int, f.readline().strip().split()))

        expire.sort()
        cups = 0
        i = 0
        cur = 0
        while cur < n:
            eated = 0
            while cur < n and eated < k:
                if expire[cur] > i:
                    cups+=1
                    eated+=1
                cur+=1
            i+=1
        print(cups)
        res.append(cups)

with open('anwer.out','w') as f:
    for i, c in enumerate(res):
        string = "Case #{}: {}\n".format(i+1, c)
        f.write(string)












