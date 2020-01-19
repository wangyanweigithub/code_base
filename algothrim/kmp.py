def kmp(p, target, pnext):
    i, j = 0, 0
    m, n = len(p), len(target)
    while (i < m and j < n):
        if p[i] == target[j] or i == -1:
            i, j = i + 1, j + 1
        else:
            j = pnext[j]
    if i == len(p) - 1:
        return j - i
    

def gen(p):
    i, j, m = 0, -1, len(p)
    pnext = [-1] * m
    while i < (m - 1):
        if j==-1 or p[i] == p[j]:
            i, j = i+1, j+1
            pnext[i] = j
        else:
            j = pnext[j]

    return pnext

pnext = gen('aab')
res = kmp('aab', 'bcaabc', pnext)
print(res)
