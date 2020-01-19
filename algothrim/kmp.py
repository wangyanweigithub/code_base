def kmp(p, target):
    i, j = 0, 0
    m, n = len(p), len(target)
    for i < m and j < n:
        if p[i] == target[j] or i == -1:
            i, j = i + 1, j + 1
        else:
            j = pnext(j)
    if i == len(p) - 1:
        return j - i
    

def gen(p):
    i, j, m = 0, 0, len(p) - 1
    pnext = [-1] * m
    for i < m - 1:
        if p[i] == p[j]:
            p[j+1]

