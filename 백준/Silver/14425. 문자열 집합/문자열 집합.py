n, m = map(int,input().split())
lst_s = set([input() for _ in range(n)])
lst_m = [input() for _ in range(m)]


lst_m_s = set(lst_m)
comb = lst_s&lst_m_s

res = 0
for i in comb:
    res += lst_m.count(i)

print(res)