#1.安装python3
#2.安装matplotlib: sudo apt-get install python3-matplotlib
#3.执行 python3 plotMotion.py ../../build/main/motion_file.txt j1
import sys
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
import numpy.matlib

# ax.plot3D(data[..., 4], data[..., 5], data[..., 6], "green")
# pdata = data[::200, ...]
# ax.scatter3D(pdata[..., 4], pdata[..., 5], pdata[..., 6], "green")
if __name__ == "__main__":
    # 初始化
    dic = {
        "j1": 0,
        "j2": 1,
        "j3": 2,
        "j4": 3,
        "x": 4,
        "y": 5,
        "z": 6,
        "c": 7,
        "xyz": 8,
        "all": 9
    }
    cycleTime = 0.002
    plt.figure(1)
    ax1 = plt.subplot(3, 1, 1)
    ax2 = plt.subplot(3, 1, 2)
    ax3 = plt.subplot(3, 1, 3)
    # ax = plt.axes(projection='3d')
    # 判断输入参数
    if len(sys.argv) != 3:
        print(
            "please enter 3 argument: <name.py> ,<plot axis>and <file path>!")
        exit(1)
    if False == (sys.argv[2] in dic):
        print(
            "unknow param ,please select right param: <j1,j2,j3,j4,x,y,z,c>!")
    tfile = sys.argv[1]
    # 获取数据
    fdata = np.loadtxt(tfile)
    data = np.asarray(fdata)
    if sys.argv[2] == "xyz":
        plt.sca(ax1)
        plt.grid()
        plt.plot(data[..., dic["x"]], data[..., dic["y"]], '-o')
        # plt.sca(ax2)
        # plt.plot(data[..., dic["x"]], data[..., dic["z"]])
        # plt.sca(ax3)
        # plt.plot(data[..., dic["y"]], data[..., dic["z"]])
        # 速度和加速度
        xyzq = data[..., (dic["x"]):(dic["z"] + 1)]
        xyz = np.subtract(xyzq[1:, ...],
                          xyzq[:(len(xyzq) - 1), ...]) / cycleTime
        xyz = np.power(xyz, 2)
        v = xyz[..., 0] + xyz[..., 1] + xyz[..., 2]
        v = np.sqrt(v)
        time = np.arange(0, cycleTime * len(v), cycleTime)
        # 速度
        plt.sca(ax2)
        plt.grid()
        # v = np.subtract(s[1:], s[:(len(s) - 1)]) / cycleTime
        plt.plot(time[:len(v)], v, '-o')
        # 加速度
        plt.sca(ax3)
        plt.grid()
        a = np.subtract(v[1:], v[:(len(v) - 1)]) / cycleTime
        plt.plot(time[:len(a)], a, '-o')

        fig = plt.figure(2)
        axe = mplot3d.Axes3D(fig)
        axe.plot3D(data[..., dic["x"]], data[..., dic["y"]],
                   data[..., dic["z"]], '-o')
        # s=np.power(,)
    elif sys.argv[2] == "all":
        if len(data) == 0:
            print("get empty data from:" + tfile)
            exit(1)
        time = np.arange(0, cycleTime * len(data), cycleTime)
        for i in range(dic["j1"], dic["j4"] + 1):
            # if i == dic["j3"] or i == dic["j4"]:
            #     continue
            axis = i
            # 路程
            plt.sca(ax1)
            plt.grid()
            s = data[..., axis]
            plt.plot(time[:len(s)], s, '-o')
            # 速度
            plt.sca(ax2)
            plt.grid()
            v = np.subtract(s[1:], s[:(len(s) - 1)]) / cycleTime
            plt.plot(time[:len(v)], v, '-o')
            # 加速度
            plt.sca(ax3)
            plt.grid()
            a = np.subtract(v[1:], v[:(len(v) - 1)]) / cycleTime
            plt.plot(time[:len(a)], a, '-o')
        plt.sca(ax1)
        plt.grid()
        plt.sca(ax2)
        plt.grid()
        plt.sca(ax3)
        plt.grid()
    else:
        axis = dic[sys.argv[2]]
        if len(data) == 0:
            print("get empty data from:" + tfile)
            exit(1)
        time = np.arange(0, cycleTime * len(data), cycleTime)
        # 路程
        plt.sca(ax1)
        plt.grid()
        s = data[..., axis]
        plt.plot(time[:len(s)], s, '-o')

        # 速度
        plt.sca(ax2)
        plt.grid()
        v = np.subtract(s[1:], s[:(len(s) - 1)]) / cycleTime
        plt.plot(time[:len(v)], v, '-o')
        # 加速度
        plt.sca(ax3)
        plt.grid()
        a = np.subtract(v[1:], v[:(len(v) - 1)]) / cycleTime
        plt.plot(time[:len(a)], a, '-o')
    plt.show()
    exit(0)