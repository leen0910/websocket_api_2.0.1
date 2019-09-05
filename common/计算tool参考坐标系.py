import math
import numpy as np
#
def getRotx(deg):
    rx=np.mat([[1,0,0],[0,np.cos(deg),-np.sin(deg)],[0,np.sin(deg),np.cos(deg)]])
    return rx

def getRoty(deg):
    ry=np.mat([[np.cos(deg),0,np.sin(deg)],[0,1,0],[-np.sin(deg),0,np.cos(deg)]])
    return ry

def getRotz(deg):
    rz=np.mat([[np.cos(deg),-np.sin(deg),0],[np.sin(deg),np.cos(deg),0],[0,0,1]])
    return rz



class Pose_t():
    def __init__(self,p_=np.array([0,0,0]),M_=np.array([0,0,0])):
        self.p=np.transpose(p_)
        self.rx=M_[0]
        self.ry=M_[1]
        self.rz=M_[2]

    def Norm(self):
        _norm=math.sqrt(np.sum(np.power(self.p,2)))
        return _norm

    def Normalize(self):
        _normalize=self.p/self.Norm()
        return _normalize

    def RPY(self):
        return np.array([self.rx,self.ry,self.rz])

    def M(self):
        return np.dot(np.dot(getRotx(self.rx),getRoty(self.ry)),getRotz(self.rz))

def clacRef(p1,p2,p3):
    ref=Pose_t()
    temp1=Pose_t()
    coor_x=Pose_t()
    coor_y=Pose_t()
    coor_z=Pose_t()
    #
    coor_x.p=p2.p-p1.p
    temp1.p=p3.p-p1.p
    if(coor_x.Norm()<1e-2):
        print("calculate reframe failed: error point...")
        return ref
    if(temp1.Norm()<1e-2):
        print("calculate reframe failed: error point...")
        return ref
    coor_x.p=coor_x.Normalize()
    temp1.p=temp1.Normalize()
    if((coor_x.p==temp1.p).all()):
        print("calculate reframe failed: three point in one line...")
        return ref
    coor_z.p=np.cross(coor_x.p,temp1.p)
    coor_y.p=np.cross(coor_z.p,coor_x.p)
    coor_z.p=coor_z.Normalize()
    coor_y.p=coor_y.Normalize()
    # 获取旋转矩阵
    rotation=np.transpose(np.array([np.transpose(coor_x.p),np.transpose(coor_y.p),np.transpose(coor_z.p)]))
    print("rotation:",rotation)
    # 计算 a,b,c
    sy=math.sqrt(rotation[0,0]*rotation[0,0]+rotation[1,0]*rotation[1,0])
    if(sy>=1e-6):
        ref.rx=math.atan2(rotation[2,1],rotation[2,2])
        ref.ry=math.atan2(-rotation[2,0],sy)
        ref.rz=math.atan2(rotation[1,0],rotation[0,0])
    else:
        ref.rx=math.atan2(-rotation[1,2],rotation[1,1])
        ref.ry=math.atan2(-rotation[2,0],sy)
        ref.rz=0
    ref.p=p1.p
    return ref

def calcEndEffector(pose1_,pose2_):
    # 暂时只计算xy
    print("# # # # #")
    M1=pose1_.M()
    M2=pose2_.M()
    print("pose1.M:",M1)
    print("pose2.M:",M2)
    # tool=Pose_t()
    # 准备开始参数提取系数
    coefficient=np.transpose(M1)-np.transpose(M2)
    constant=np.transpose(pose1_.p-pose2_.p)
    coefficient=coefficient[0:2,0:2]
    constant=constant[0:2]
    print("coefficient:",coefficient)
    print("constant:",constant)
    tool=np.linalg.solve(coefficient,constant)
    print("calc tool:",tool)
    print("# # # # #")
    return tool



if __name__ == "__main__":
    # 得到的标定点
    np.set_printoptions(precision=3)
    # 计算夹具,随意的两个点
    p1=np.array([[385.403,97.112,0],[0,0,0]])
    p2=np.array([[286.933,21.037,0],[0,0,np.pi]])
    # 开始计算
    # 将输入点换算为计算点
    cp1=Pose_t(p1[0,...],p1[1,...])
    cp2=Pose_t(p2[0,...],p2[1,...])
    # 夹具
    calcEndEffector(cp1,cp2)

    # 参考坐标系
    r1=np.array([[319.312,84.528,-139.213],[0,0,0]])
    r2=np.array([[382.808,84.528,-128.750],[0,0,0]])
    r3=np.array([[362.663,32.059,-132.973],[0,0,0]])
    refp1=Pose_t(r1[0,...],r1[1,...])
    refp2=Pose_t(r2[0,...],r2[1,...])
    refp3=Pose_t(r3[0,...],r3[1,...])

    ref=clacRef(refp1,refp2,refp3)
    print("ref.p:",ref.p,ref.RPY())