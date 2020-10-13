import BSplineBaisc as b
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


# n=m-p-1,m是U的长度-1
def CurvePoint(n, p, U, P, u):
    span = b.FindSpan(n, p, u, U)
    N = b.BasisFuns(span, u, p, U)
    c = 0.0
    for i in range(p + 1):
        c = c + N[i] * P[span - p + i]
    return c


if __name__ == "__main__":
    k = 3
    U = np.array([0, 0, 0, 0, 1 / 3, 2 / 3, 1, 1, 1, 1])
    n = len(U) - k - 1
    P = np.array([[20, 59, 0], [0, 0, 10], [10, 29, -20], [
                 78, 92, 11.30], [-22, 68, 5.450], [-4, -15, 0]])

    # 计算点
    step = 0.0001
    point = [0, 0, 0]
    i = 0
    date = np.empty([0, 0])
    while i <= 1:
        point[0] = CurvePoint(n, k, U, P[..., 0], i)
        point[1] = CurvePoint(n, k, U, P[..., 1], i)
        point[2] = CurvePoint(n, k, U, P[..., 2], i)
        if len(date) == 0:
            date = np.array([point])
        else:
            date = np.append(date, [point], axis=0)
        i += step
    point = np.array(date)
    fig = plt.figure(1)
    # plt.plot(p[..., 0], p[..., 1], "-ob")
    # plt.plot(P[..., 0], P[..., 1], "-or")
    # plt.show()
    axe = mplot3d.Axes3D(fig)
    axe.plot3D(P[..., 0], P[..., 1], P[..., 2], '-ob')
    axe.plot3D(point[..., 0], point[..., 1], point[..., 2], '-or')
    plt.show()
