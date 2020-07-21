def gen(p):
    i, j, pnext = 0, -1, [-1] * len(p)
    while i < len(p) - 1:
        if j == -1 or p[i] == p[j]:
            i, j = i + 1, j + 1
            pnext[i] = j
        else:
           j = pnext[j] 

    print(pnext)
    return pnext


def match(s, p, pnext):
    i, j = 0, 0
    res = []
    while j < len(s):
        if s[j] == p[i] or i == -1:
            i, j = i + 1, j + 1
        else:
            i = pnext[i]

        if i == len(p):
            res.append(j - i)
            i = 0

    for sub in res:
        print(s[sub:sub + len(p)])
    return res


pnext = gen('aab')
res = match('bcaabcaab', 'aab', pnext)
print(res)
print()
