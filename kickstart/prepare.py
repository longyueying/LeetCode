anwer = []
with open('A-small-practice.in') as f:
    print(f.readline())
    print(f.readline())
    for line in f:
        anwer.append(line.strip())

with open('anwer.out', 'w') as f:
    for i, line in enumerate(anwer):
        string = "Case #{}: {}\n".format(i, line)
        f.write(string)


