import BSplineBaisc as b
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import datetime
import math
# bspline


# n=m-p-1,m是U的长度-1


def CurvePoint(n, p, U, W, P, u):
    span = b.FindSpan(n, p, u, U)
    N = b.BasisFuns(span, u, p, U)
    c = 0.0
    cw = 0.0
    # print(span)
    for i in range(p + 1):
        c = c + N[i] * W[span-p+i] * P[span - p + i]
        cw = cw+N[i]*W[span-p+i]
    return c/cw


def curveDeriv(n, p,  U, W, P, u):
    '''
    n:控制点个数|p:次数|U:节点矢量|P:控制点|d:求导次数
    '''
    Px = np.array([P[0] for i in range(n-1)])
    Wx = np.array([W[0] for i in range(n-1)])
    Ux = U[1:-1]
    nx = n-1
    px = p-1
    for i in range(nx):
        Px[i] = p*(W[i+1]*P[i+1]-W[i]*P[i])/(U[i+p+1]-U[i+1])
        Wx[i] = p*(W[i+1]-W[i])/(U[i+p+1]-U[i+1])
        if Wx[i] == 0:
            Wx[i] = 1

    span = b.FindSpan(n, p, u, U)
    spanx = b.FindSpan(nx, px, u, Ux)
    N = b.BasisFuns(span, u, p, U)
    Nx = b.BasisFuns(spanx, u, px, Ux)
    w = 0.0
    dw = 0.0
    da = 0.0
    c = 0.0
    for i in range(px+1):
        da = da+Nx[i]*Wx[spanx-px+i]*Px[spanx-px+i]
        dw = dw+Nx[i]*Wx[spanx-px+i]
        c = c + N[i] * W[span-p+i] * P[span - p + i]
        w = w + N[i] * W[span-p+i]
    c = c + N[p] * W[span] * P[span]
    w = w+N[p]*W[span]
    dc = (da-dw*(c/w))/w
    return dc


def curveDerivWithN(n, p, U, W, P, u):
    span = b.FindSpan(n, p, u, U)
    N = b.DersBasisFuns(span, u, p, 1, U)
    a = 0.0
    da = 0.0
    w = 0.0
    dw = 0.0
    for i in range(p+1):
        a = a+N[0][i]*W[span-p+i]*P[span-p+i]
        w = w+N[0][i]*W[span-p+i]

        da = da+N[1][i]*W[span-p+i]*P[span-p+i]
        dw = dw+N[1][i]*W[span-p+i]
    c = a/w
    dc = (da-dw*c)/w
    return dc


def curveDDeriv(n, p, U, W, P, u):
    span = b.FindSpan(n, p, u, U)
    N = b.DersBasisFuns(span, u, p, 2, U)
    a = 0.0
    da = 0.0
    dda = 0.0
    w = 0.0
    dw = 0.0
    ddw = 0.0

    for i in range(p+1):
        a = a+N[0][i]*W[span-p+i]*P[span-p+i]
        w = w+N[0][i]*W[span-p+i]

        da = da+N[1][i]*W[span-p+i]*P[span-p+i]
        dw = dw+N[1][i]*W[span-p+i]

        dda = dda+N[2][i]*W[span-p+i]*P[span-p+i]
        ddw = ddw+N[2][i]*W[span-p+i]
    c = a/w
    dc = (da-dw*c)/w
    ddc = (dda-2*dw*dc-ddw*c)/w
    return ddc


def curveDerivN(n, p, U, W, P, d, u):
    span = b.FindSpan(n, p, u, U)
    N = b.DersBasisFuns(span, u, p, 2, U)
    Ader = np.array([[0.0 for _ in range(len(P[0]))] for _ in range(d+1)])
    Wder = np.array([0.0 for _ in range(d+1)])
    Bin = np.array([[0.0 for _ in range(d+1)] for _ in range(d+1)])
    CK = np.array([[0.0 for _ in range(len(P[0]))] for _ in range(d+1)])

    for i in range(0, d+1):
        Bin[i][0] = 1
        for k in range(1, i+1):
            Bin[i][k] = Bin[i][k-1]*(i-k+1)/k
    for r in range(d+1):
        for i in range(p+1):
            Ader[r] = Ader[r]+N[r][i]*W[span-p+i]*P[span-p+i]
            Wder[r] = Wder[r]+N[r][i]*W[span-p+i]
            # print("r:", r, "N:", N[r][i], "W:",
            #       W[span-p-+i], 'P:', P[span-p+i], Ader[r])
    for k in range(d+1):
        v = Ader[k]
        for i in range(1, k+1):
            v = v-Bin[k][i]*Wder[i]*CK[i-1]
        CK[k] = v/Wder[0]
    return CK


def calcTarget(n, p, U, W, P, a, b, precision):
    u = a
    end = b
    target = 0.0
    point_pre = CurvePoint(n, p, U, W, P, u)
    while u < end:
        u = u+precision
        if(u > end):
            u = end
        point_next = CurvePoint(n, p, U, W, P, u)
        s = np.sqrt(np.sum(np.power((point_next-point_pre), 2)))
        point_pre = point_next
        target += s
        # print(u)
    # print(u)
    return target

# 计算长度


def calcFSpan(n, p, U, W, P, a, b):
    fa = np.sqrt(np.sum(np.power(curveDerivWithN(n, p, U, W, P, a), 2)))
    f2ab = np.sqrt(
        np.sum(np.power(curveDerivWithN(n, p, U, W, P, (2*a+b)/3), 2)))
    fa2b = np.sqrt(
        np.sum(np.power(curveDerivWithN(n, p, U, W, P, (a+2*b)/3), 2)))
    fb = np.sqrt(np.sum(np.power(curveDerivWithN(n, p, U, W, P, b), 2)))
    return (b-a)*(fa+3*f2ab+3*fa2b+fb)/8


def calcSpanTarget(n, p, U, W, P, a, b, precision, us=np.array([[0, 0, 0]])):
    mid = (a+b)/2
    f_front = calcFSpan(n, p, U, W, P, a, mid)
    f_back = calcFSpan(n, p, U, W, P, mid, b)
    f_all = calcFSpan(n, p, U, W, P, a, b)
    if np.fabs(f_front+f_back-f_all)/10 < precision:
        # target = calcTarget(n, p, U, W, P, a, b, precision)
        # target += us[-1][1]
        target = f_all
        target += us[-1][1]
        ret = np.append(us, [[b, target, precision]], axis=0)
        return ret
    us = calcSpanTarget(n, p, U, W, P, a, mid, precision/2, us)
    us = calcSpanTarget(n, p, U, W, P, mid, b, precision/2, us)
    return us


def calcTargetWithKnot(n, p, U, W, P, a, b, precision):
    count = 0
    low = a
    us = np.array([[0, 0, 0]])
    while low < b:
        while U[count] <= low:
            count += 1
        knot = U[count]
        if knot > b:
            knot = b
        ret = calcSpanTarget(n, p, U, W, P, low, knot, precision, [us[-1]])
        us = np.append(us, ret[1:, ...], axis=0)
        low = knot
    return us


if __name__ == "__main__":
    # k = 3
    # U = np.array([0, 0, 0, 0, 0.5, 1, 1, 1, 1])
    # n = len(U) - k - 1
    # W = np.array([1, 1, 1,  1, 1])
    # P = np.array([[0, 0, 0], [10, 0, 0], [20, 0, 0], [20, 10, 0], [20, 20, 0]])

    #
    k = 3
    U = np.array([0, 0, 0, 0, 0.10001, 0.20002, 0.30003, 0.40004,
                  0.50005, 0.60006, 0.70007, 0.80008, 1, 1, 1, 1])
    n = len(U) - k - 1
    W = np.array([1, 1, 1, 5, 1, 1, 1, 1, 5, 1, 1, 1])
    P = np.array([[0, 0, 0], [10, 0, 0], [20, 0, 0], [
                 50, 0, 0], [0, 10, 0], [0, 30, 0], [20, 50, 0], [40, 50, 0], [50, 0, 0], [50, 30, 0], [50, 40, 0], [50, 50, 0]])

    # 计算点
    point = [0, 0, 0]
    i = 0
    # 第一种计算方法
    start = datetime.datetime.now()
    # us = calcTargetWithKnot(n, k, U, W, P, 0, 1, 1e-5)
    us = calcSpanTarget(n, k, U, W, P, 0, 1, 1e-5)
    end = datetime.datetime.now()
    print("1", us[-1][1], 'use:', end-start)
    #
    start = datetime.datetime.now()
    us = calcTargetWithKnot(n, k, U, W, P, 0, 1, 1e-5)
    end = datetime.datetime.now()
    print("2:", us[-1][1], 'use', end-start)

    # print('us:', us)
    t = CurvePoint(n, k, U, W, P, 0.5)
    print("1:", t)
    # t = curveDeriv(n, k, U, W, P, 0.5)
    # print('2:', t)
    # exit(0)
    # curveDerivCpts(n, k, U, P, 1)
    # calcTarget(n, k, U, W, P, 1e-5)
    ck = curveDerivN(n, k, U, W, P, 2, 0.5)
    print(ck)
    # exit(0)
    print("###---###")
    count = 0
    step = 1e-3
    deriv_point = 0
    dderiv_point = 0
    while i <= 1:
        # for j in range(len(us)):
        # i = us[j][0]
        # 进行插补步进
        # print(i)
        point = CurvePoint(n, k, U, W, P, i)
        # deriv_point = curveDeriv(n, k, U, W, P, i)
        deriv_point = curveDerivWithN(n, k, U, W, P, i)
        dderiv_point = curveDDeriv(n, k, U, W, P, i)
        if i == 0:
            date = np.array([point])
            deriv = np.array([deriv_point])
            dderiv = np.array([dderiv_point])
        else:
            date = np.append(date, [point], axis=0)
            deriv = np.append(deriv, [deriv_point], axis=0)
            dderiv = np.append(dderiv, [dderiv_point], axis=0)
        # print("count:", count, "p:", point, "dp:",
        #       deriv_point, 'ddp:', dderiv_point)
        count += 1
        i += step
    # exit(0)
    point = np.array(date)
    fig = plt.figure(1)
    fig2 = plt.figure(2)
    # plt.plot(p[..., 0], p[..., 1], "-ob")
    # plt.plot(P[..., 0], P[..., 1], "-or")
    # plt.show()
    axe = mplot3d.Axes3D(fig)
    axe.plot3D(P[..., 0], P[..., 1], P[..., 2], '-ob')
    axe.plot3D(point[..., 0], point[..., 1], point[..., 2], '-or')
    # x-y
    plt.plot(P[..., 0], P[..., 1], '-ob')
    plt.plot(point[..., 0], point[..., 1], '-or')
    # for i in range(len(deriv)):
    #     if not i % 10 == 0:
    #         continue
    #     p = np.array([point[i], deriv[i]+point[i]])
    #     axe.plot3D(p[..., 0], p[..., 1], p[..., 2], '--og')
    #     plt.plot(p[..., 0], p[..., 1], 'g')
    #     if i < len(dderiv):
    #         p = np.array([deriv[i]+point[i], dderiv[i]+deriv[i]+point[i]])
    #         # print(p)
    #         axe.plot3D(p[..., 0], p[..., 1], p[..., 2], '--oy')
    #         plt.plot(p[..., 0], p[..., 1], '--y')
    plt.grid()
    plt.show()
