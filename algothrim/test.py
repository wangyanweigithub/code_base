def gen_pnext(p):
    i, j, m = 0, -1, len(p)
    pnext = [-1] * m 
    while i < m - 1:
        if j == -1 or p[i] ==  p[j]:
            i, j = i + 1, j + 1 
            pnext[i] = j 
        else:
            j = pnext[j]
    print(pnext)
    return pnext


def match(t, p, pnext):
    m, n = len(p), len(t)
    i, j = 0, 0

    while i < m and j < n:
        if i == -1 or t[j] == p[i]:
            i, j = i + 1, j + 1 
        else:
            i = pnext[i]

    if i == m:
        return j - i 


def main():
    p = "abcabc"
    t = "eeeabcabc"
    pnext = gen_pnext(p)
    print("Pnext", pnext)


main()
