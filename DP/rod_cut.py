"""Rod_cut Memorized approach"""


def rod_cut(p, n, memo):
    r = float('-inf')
    if n == 0:
        r = 0
    if n in memo:
        r = memo[n]
    else:
        for i in range(1,n+1):
            r = max(r, p[i-1] + rod_cut(p, n - i, memo))
        memo[n] = r
    return r


p = [1,5,8,9,10,17,17,20,24,30]
memo = {}
print(rod_cut(p, 6, memo))


"""Rod_cut bottom up approach"""


def rod_cut_iter(p,n):
    r = [None]*(n+1)
    r[0] = 0
    if n == 0:
        q = 0
    else:
        for j in range(1,n+1):
            q = float('-inf')
            for i in range(1,j+1):
                q = max(q, p[i-1]+r[j-i])
            r[j] = q
    return q


print(rod_cut_iter(p, 6))