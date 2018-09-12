def  solve(S, T):
    res = 0
    dic = {}
    t_list = []
    for i in range(len(T)):
        dic.setdefault(T[i], [])
        dic[T[i]].append(i)
    for k in dic:
        t_list.append(len(dic[k]))
        t_list.extend(dic[k])
    for i in range(len(S)-len(T)+1):
        dic_s = {}
        for j in range(len(T)):
            dic_s.setdefault(S[i+j], [])
            dic_s[S[i+j]].append(j)
        tmp = []
        for k in dic_s:
            tmp.append(len(dic_s[k]))
            tmp.extend(dic_s[k])
        # flag = True
        # if len(tmp) == len(t_list):
        #     for j in range(len(tmp)):
        #         if tmp[j]!=t_list[j]:
        #             flag = False
        #             break
        #     if flag == True:
        #         res+=1
        print(tmp-t_list)
        if len(tmp) == len(t_list):
            for j in range(len(tmp)):
                if tmp[j]!=t_list[j]:
                    res-=1
                    break
            res+=1
    return res
print(solve('ababcb','xyx'))

