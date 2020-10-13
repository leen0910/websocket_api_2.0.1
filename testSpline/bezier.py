import math


# 计算berizer基函数多项式的值
def Bernstein(i, n, u):
    temp = [0] * (n + 1)
    temp[n - i] = 1.0
    u1 = 1.0 - u
    for k in range(1, n + 1):
        for j in range(n, k - 1, -1):
            temp[j] = u1 * temp[j] + u * temp[j - 1]
    return temp[n]


# 计算所有的n次bernstein多项式的值
def AllBernstein(n, u):
    b = [0] * (n + 1)
    b[0] = 1.0
    u1 = 1.0 - u
    for i in range(1, n + 1, 1):
        saved = 0.0
        for k in range(0, i, 1):
            temp = b[k]
            b[k] = saved + u1 * temp
            saved = u * temp
        b[i] = saved
    return b


def myBernstein(i, n, u):
    return (math.factorial(n) /
            (math.factorial(i) * math.factorial(n - i))) * math.pow(
                u, i) * math.pow(1 - u, n - i)


if __name__ == "__main__":
    u = 0.6
    n = 3
    for i in range(4):
        B1 = Bernstein(i, n, u)
        print("Bernstein:", B1)
        B2 = myBernstein(i, n, u)
        print("myBernstein:", B2)
    B3 = AllBernstein(n, u)
    print("AllBernstein:", B3)
