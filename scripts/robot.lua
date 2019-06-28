-- 开始

-- 预先定义参考坐标系,全为0时即设置为世界坐标
-- notice:参考坐标系只对空间坐标下的运动起作用,世界坐标位置=设定坐标+参考坐标
pose_ref1={X = 0, Y = 0, Z = 0, A = 0, B = 0, C = 0}
pose_ref2={X = 10, Y = 10, Z = 0, A = 0, B = 0, C = math.pi/2}

-- 预先定义一些坐标点,在scara机械臂中,有效的是[X,Y,Z,c]
pose1 ={X = 250, Y = 0, Z = -50,A = 0,B = 0,C = 0}
posem1={X = 300, Y = 50, Z = -50,A = 0,B = 0,C = 0}
pose2 ={X = 350, Y = 0, Z = -50,A = 0,B = 0,C = 0}
posem2={X = 300, Y =-50, Z = -50,A = 0,B = 0,C = 0}
posel1 ={X = 250, Y = 100, Z = -50,A = 0,B = 0,C = 0}
posel2 ={X = 250, Y = -100, Z = -50,A = 0,B = 0,C = 0}

-- 预先定义一些关节点,在scara机械臂中,有效的是[j1,j2,j3,j4],其中j3为Z轴,依然表示Z方向的长度
posit1={J1= 0,J2= 0,J3= 0,J4=0,J5=0,J6=0}
posit2={J1=-2,J2=-2,J3= 0,J4=0,J5=0,J6=0}
posit3={J1= 2,J2= 2,J3=-100,J4=0,J5=0,J6=0}
posit4={J1= 1,J2=-1,J3= 0,J4=0,J5=0,J6=0}

-- 预先定义运动速度和过渡参数
vel =100
blend=100

-- 点到点运动,目标点为关节值
--robot.MP(pose1,vel,blend)
robot.MP(posit1,vel,blend)
robot.MP(posit2,vel,blend)
robot.MP(posit3,vel,blend)
robot.MP(posit2,vel,blend)
robot.MP(posit1,vel,blend)


loop=200
while(loop>0)
do
loop=loop-1;
-- 设置1.5s的延时
robot.DELAY(1)
robot.DELAY_MS(500)
-- 设置参考坐标系
if loop==1 then
-- 设置参考坐标系1
robot.RCS(pose_ref1)
else
-- 改变参考坐标系尝试一下
robot.RCS(pose_ref2)
end
-- 点到点运动,目标点为世界值,采用世界值进行运动时,建议设置参考坐标系
robot.MP(posel2,vel,blend)
-- 直线运动
robot.ML(pose1,vel,blend)
-- 圆弧运动
robot.MC(posem1,pose2,vel,blend)
robot.MC(posem2,pose1,vel,blend)
-- 直线运动
robot.ML(posel1,vel,blend)
end
-- 等待运动结束
robot.WAIT()
-- 设置为世界坐标系
robot.RCS(pose_ref1)

-- 调节运动速度
vel=80

robot.WAIT()

-- 回到开始点
robot.MP(posit1,vel,blend)

-- 结束