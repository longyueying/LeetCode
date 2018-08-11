import collections
def minWindow( s, t):
    need, missing = collections.Counter(t), len(t)
    print(need)
    i = I = J = 0
    for j, c in enumerate(s, 1):

        missing -= need[c] > 0
        need[c] -= 1
        if not missing:
            while i < j and need[s[i]] < 0:

                need[s[i]] += 1
                print(need)
                i += 1
            if not J or j - i <= J - I:
                I, J = i, j
    return s[I:J]
minWindow("ADOBECODEBANC","ABC")

