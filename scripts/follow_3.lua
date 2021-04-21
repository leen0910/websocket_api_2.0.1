    -- pose:[X,Y,Z,A,B,C]世界坐标系下坐标点,在scara机械臂中,有效的是[X,Y,Z,C]
    pose_ref1 = {X = 250, Y =  0, Z = -50,A = 0,B = 0,C = 0}
    pose_ref2 = {X = 260, Y =  0, Z = -50,A = 0,B = 0,C = 0}
    pose_ref3 = {X = 250, Y =  10, Z = -50,A = 0,B = 0,C = 0}

    pose_direction1={X = 0, Y =  1, Z = 0,A = 0,B = 0,C = 0}
    pose_direction2={X = 1, Y =  0, Z = 0,A = 0,B = 0,C = 0}
    pose_direction3={X = 0, Y =  -1, Z = 0,A = 0,B = 0,C = 0}

    vel  =40
    -- 与跟踪参考坐标系的相对位置
    pose0 = {X = 0, Y =  0, Z = 0,A = 0,B = 0,C = 0}
    pose1 = {X = 10, Y =  0, Z = 0,A = 0,B = 0,C = 0}
    -- 准备开始运动
count=0
while (true)
do
if(count==0)
then
    R.FOLLOW_ADD(pose_ref1,pose_direction1,vel,0,10,100,2)

    R.FOLLOW_ADD(pose_ref2,pose_direction2,vel,0,10,100,2)

    R.FOLLOW_ADD(pose_ref3,pose_direction3,vel,0,10,100,2)
count=2
end
    R.FOLLOW_NEXT()
    R.MP(pose0,100)
    R.MP(pose1,100)
    R.MP(pose0,100)
    R.FOLLOW_EXIT()
count=count-1
end