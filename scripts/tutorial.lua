-- 开始

-- 预先定义参考坐标系,全为0时即设置为世界坐标
-- notice:参考坐标系只对空间坐标下的运动起作用,世界坐标位置=设定坐标+参考坐标
pose_ref1={["x"] =  0, ["y"] =  0, ["z"] = 0, ["a"] = 0, ["b"] = 0, ["c"] = 0}
pose_ref2={["x"] = 10, ["y"] = 10, ["z"] = 0, ["a"] = 0, ["b"] = 0, ["c"] = math.pi/2}

-- 预先定义一些坐标点,在scara机械臂中,有效的是[x,y,z,c]
pose1 ={["x"] = 250, ["y"] =  0, ["z"] = -50,["a"] = 0,["b"] = 0,["c"] = 0}
posem1={["x"] = 300, ["y"] = 50, ["z"] = -50,["a"] = 0,["b"] = 0,["c"] = 0}
pose2 ={["x"] = 350, ["y"] =  0, ["z"] = -50,["a"] = 0,["b"] = 0,["c"] = 0}
posem2={["x"] = 300, ["y"] =-50, ["z"] = -50,["a"] = 0,["b"] = 0,["c"] = 0}
posel1 ={["x"] = 250, ["y"] =  100, ["z"] = -50,["a"] = 0,["b"] = 0,["c"] = 0}
posel2 ={["x"] = 250, ["y"] = -100, ["z"] = -50,["a"] = 0,["b"] = 0,["c"] = 0}

-- 预先定义一些关节点,在scara机械臂中,有效的是[j1,j2,j3,j4],其中j3为z轴,依然表示z方向的长度
posit1={["j1"]= 0,["j2"]= 0,["j3"]=   0,["j4"]=0,["j5"]=0,["j6"]=0}
posit2={["j1"]=-2,["j2"]=-2,["j3"]=   0,["j4"]=0,["j5"]=0,["j6"]=0}
posit3={["j1"]= 2,["j2"]= 2,["j3"]=-100,["j4"]=0,["j5"]=0,["j6"]=0}
posit4={["j1"]= 1,["j2"]=-1,["j3"]=   0,["j4"]=0,["j5"]=0,["j6"]=0}

-- 预先定义运动速度和过渡参数
vel  =100
blend=100

-- 点到点运动,目标点为关节值
robot.move_p2p_posit(posit1,vel,blend)
robot.move_p2p_posit(posit2,vel,blend)
robot.move_p2p_posit(posit3,vel,blend)
robot.move_p2p_posit(posit2,vel,blend)
robot.move_p2p_posit(posit1,vel,blend)



loop=2
while(loop>0)
do
    loop=loop-1;
    -- 设置1.5s的延时
    robot.set_delay_sec(1)
    robot.set_delay_ms(500)
    -- 设置参考坐标系
    if loop==1 then
        -- 设置参考坐标系1
        robot.set_ref_frame(pose_ref1)
    else
        -- 改变参考坐标系尝试一下
        robot.set_ref_frame(pose_ref2)
    end
    -- 点到点运动,目标点为世界值,采用世界值进行运动时,建议设置参考坐标系
    robot.move_p2p_pose(posel2,vel,blend)
    -- 直线运动
    robot.move_line_pose(pose1,vel,blend)
    -- 圆弧运动
    robot.move_arc_pose(posem1,pose2,vel,blend)
    robot.move_arc_pose(posem2,pose1,vel,blend)
    -- 直线运动
    robot.move_line_pose(posel1,vel,blend)
end
-- 等待运动结束
robot.wait_move_done()
-- 设置为世界坐标系
robot.set_ref_frame(pose_ref1)

if false then
    -- modbus设置点位
    FT13100=280.5
    FT13104=106.7
    FT13108=-50.2
    FT13112=2.1

    -- 调节运动速度
    vel=80

    -- 运动到设定点
    poseM ={["x"] = FT13100, ["y"] =  FT13104, ["z"] = FT13108,["a"] = 0,["b"] = 0,["c"] = FT13112}
    robot.move_p2p_pose(poseM,vel,blend)
    robot.wait_move_done()
end
-- 回到开始点
robot.move_p2p_posit(posit1,vel,blend)

-- 结束