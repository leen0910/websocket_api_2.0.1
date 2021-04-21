
-- 以臂长400mm机器人为例
    RCS={}
    RCS[0]={X = 0, Y = 0, Z = 0,A = 0,B = 0,C = 0}
    RCS[1]={X = 100, Y = 0, Z = 0,A = 0,B = 0,C = 0}
    -- point1,point2:[X,Y,Z,A,B,C],世界坐标系下坐标点,在scara机械臂中,有效的是[X,Y,Z,C]
    point1 = {X = 150, Y = -150, Z = -100,A = 0,B = 0,C = 0,RCS=1}
    point2 = {X = 150, Y = 150, Z = -100,A = 0,B = 0,C = 0,RCS=1}
    -- 运动速度
    vel  =100
    -- 过渡参数
    blend={BLEND=100}
    -- 拱门运动
while (1)
do
    EXTEND_ARCH(point1,point2,25,25,vel,blend)
    EXTEND_ARCH(point2,point1,25,25,vel,blend)
-- 等待运动结束
    --R.WAIT()
end

