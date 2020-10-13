import math


# 找到u所在的节点区间
# n=m-p-1,m是U的长度-1
def FindSpan(n, p, u, U):
    if (u >= U[n + 1]):
        return n-1
    # 次数
    low = p
    high = n + 1
    mid = int((low + high) / 2)
    while (u < U[mid] or u >= U[mid + 1]):
        if u < U[mid]:
            high = mid
        else:
            low = mid
        mid = int((low + high) / 2)
    return mid


# 计算所有P次B样条的基函数的值
# i :u所在的节点区间,u:节点变量 p:次数,U:节点空间
def BasisFuns(i, u, p, U):
    N = [0] * (p + 1)
    left = [0] * (p + 1)
    right = [0] * (p + 1)
    N[0] = 1.0
    for j in range(1, p + 1):
        left[j] = u - U[i + 1 - j]
        right[j] = U[i + j] - u
        saved = 0.0
        for r in range(j):
            temp = N[r] / (right[r + 1] + left[j - r])
            N[r] = saved + right[r + 1] * temp
            saved = left[j - r] * temp
        N[j] = saved
    return N


# 计算所有B样条基函数以及导数
# n:只带要计算的n阶导数
def DersBasisFuns(i, u, p, n, U):
    ndu = [[0 for col in range(p + 1)] for row in range(p + 1)]
    ders = [[0 for col in range(p + 1)] for row in range(n + 1)]
    left = [0 for col in range(p + 1)]
    right = [0 for col in range(p + 1)]
    ndu[0][0] = 1.0
    # 计算基函数
    for j in range(1, p + 1):
        left[j] = u - U[i + 1 - j]
        right[j] = U[i + j] - u
        saved = 0.0
        for r in range(j):
            ndu[j][r] = right[r + 1] + left[j - r]
            temp = ndu[r][j - 1] / ndu[j][r]
            ndu[r][j] = saved + right[r + 1] * temp
            saved = left[j - r] * temp
        ndu[j][j] = saved
    for j in range(p + 1):
        ders[0][j] = ndu[j][p]
    a = [[0 for col in range(p + 1)] for row in range(p + 1)]
    # 计算导数
    for r in range(p + 1):
        s1 = 0
        s2 = 1
        a[0][0] = 1.0
        # 计算k阶导数
        for k in range(1, n + 1):
            d = 0.0
            rk = r - k
            pk = p - k
            if r >= k:
                a[s2][0] = a[s1][0] / ndu[pk + 1][rk]
                d = a[s2][0] * ndu[rk][pk]
            if rk >= -1:
                j1 = 1
            else:
                j1 = -rk
            if (r - 1 <= pk):
                j2 = k - 1
            else:
                j2 = p - r
            for j in range(j1, j2 + 1):
                a[s2][j] = (a[s1][j] - a[s1][j - 1]) / ndu[pk + 1][rk + j]
                d += a[s2][j] * ndu[rk + j][pk]
            if r <= pk:
                a[s2][k] = -a[s1][k - 1] / ndu[pk + 1][r]
                d += a[s2][k] * ndu[r][pk]
            ders[k][r] = d
            j = s1
            s1 = s2
            s2 = j
    r = p
    for k in range(1, n + 1):
        for j in range(p + 1):
            ders[k][j] *= r
        r *= (p - k)
    return ders


# 只计算一个基函数
def OneBasisFun(p, m, U, i, u):
    N = [0 for col in range(p + 1)]
    if (i == 0 and u == U[0]) or (i == m - p - 1 and u == U[m]):
        Nip = 1.0
        return Nip
    if u < U[i] or u >= U[i + p + 1]:
        Nip = 0.0
        return Nip
    for j in range(p + 1):
        if u >= U[i + j] and u < U[i + j + 1]:
            N[j] = 1.0
        else:
            N[j] = 0.0
    saved = 0.0
    for k in range(1, p + 1):
        if N[0] == 0:
            saved = 0.0
        else:
            saved = ((u - U[i]) * N[0]) / (U[i + k] - U[i])
        for j in range(p - k + 1):
            Uleft = U[i + j + 1]
            Uright = U[i + j + k + 1]
            if N[j + 1] == 0.0:
                N[j] = saved
                saved = 0.0
            else:
                temp = N[j + 1] / (Uright - Uleft)
                N[j] = saved + (Uright - u) * temp
                saved = (u - Uleft) * temp
    return N[0]


# 计算基函数的各阶导数
def DersOneBasisFun(p, m, U, i, u, n):
    N = [[0 for col in range(p + 1)] for row in range(p + 1)]
    ND = [0 for col in range(n + 1)]
    ders = [0 for col in range(n + 1)]
    if u < U[i] or u >= U[i + p + 1]:
        for k in range(n + 1):
            ders[k] = 0.0
        return ders
    for j in range(p + 1):
        if u >= U[i + j] and u < U[i + j + 1]:
            N[j][0] = 1.0
        else:
            N[j][0] = 0.0
    saved = 0.0
    for k in range(1, p + 1):
        if N[0][k - 1] == 0.0:
            saved = 0.0
        else:
            saved = ((u - U[i]) * N[0][k - 1]) / (U[i + k] - U[i])
        for j in range(p - k + 1):
            Uleft = U[i + j + 1]
            Uright = U[i + j + k + 1]
            if N[j + 1][k - 1] == 0.0:
                N[j][k] = saved
                saved = 0.0
            else:
                temp = N[j + 1][k - 1] / (Uright - Uleft)
                N[j][k] = saved + (Uright - u) * temp
                saved = (u - Uleft) * temp
    ders[0] = N[0][p]
    for k in range(1, n + 1):
        for j in range(k + 1):
            ND[j] = N[j][p - k]
        for jj in range(1, k + 1):
            if ND[0] == 0.0:
                saved = 0.0
            else:
                saved = ND[0] / (U[i + p - k + jj] - U[i])
            for j in range(k - jj + 1):
                Uleft = U[i + j + 1]
                Uright = U[i + j + p + jj + 1]
                if ND[j + 1] == 0.0:
                    ND[j] = (p - k + jj) * saved
                    saved = 0.0
                else:
                    temp = ND[j + 1] / (Uright - Uleft)
                    ND[j] = (p - k + jj) * (saved - temp)
                    saved = temp
        ders[k] = ND[0]
    return ders


if __name__ == "__main__":
    U = [0, 0, 0, 1, 2, 3, 4, 4, 5, 5, 5]
    # print(FindSpan())

    p = 2
    u = 5 / 2
    m = len(U) - 1
    i = FindSpan(m - p - 1, p, u, U)
    print("### all ###")
    print("i:", i)
    print("basic:", BasisFuns(i, u, p, U))
    print("ders:", DersBasisFuns(i, u, p, 2, U))

    print("### one ###")
    print("i:", i)
    print("basic:", OneBasisFun(p, m, U, i, u))
    print("ders:", DersOneBasisFun(p, m, U, i, u, 2))
