--600设备圆弧轨迹
vel=100;
blend=50;


--第一段轨迹：接近圆
pose1 ={X = 500, Y =  150, Z = 0,A = 0,B = 0,C = 0}
pose2 ={X = 400, Y =  0, Z = 0,A = 0,B = 0,C = 0}
pose3 ={X = 475.82622, Y = 149.9831, Z = 0,A = 0,B = 0,C = 0}

--第二段轨迹：两个返向相连接圆弧
pose4 ={X = -300, Y =  200, Z = 0,A = 0,B = 0,C = 0}
pose5 ={X = -200, Y =  500, Z = 0,A = 0,B = 0,C = 0}
pose6 ={X = 200, Y =  500, Z = 0,A = 0,B = 0,C = 0}
pose7 ={X = 200, Y =  300, Z = 0,A = 0,B = 0,C = 0}
pose8 ={X = 500, Y =  300, Z = 0,A = 0,B = 0,C = 0}

while(1)
do

--第一段轨迹：接近圆
	R.MP(pose1,vel,blend)
    R.MC(pose2,pose3,vel,blend)

--第二段轨迹：两个返向相连接圆弧
	R.MP(pose4,vel,blend)
    R.MC(pose5,pose6,vel,blend)
    R.MC(pose7,pose8,vel,blend)

end