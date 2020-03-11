--400设备圆弧轨迹
vel=100;
blend=50;


--第一段轨迹：接近圆
pose1 ={X = 300, Y =  100, Z = 0,A = 0,B = 0,C = 0}
pose2 ={X = 351.54827, Y = -4.58169, Z = 0,A = 0,B = 0,C = 0}
pose3 ={X = 346.1228, Y = 72.73136, Z = 0,A = 0,B = 0,C = 0}

--第二段轨迹：两个返向相连接圆弧
pose4 ={X = -200, Y =  100, Z = 0,A = 0,B = 0,C = 0}
pose5 ={X = -154.37748, Y = 314.1651, Z = 0,A = 0,B = 0,C = 0}
pose6 ={X = 100, Y =  300, Z = 0,A = 0,B = 0,C = 0}
pose7 ={X = 198.27854, Y =158.18263, Z = 0,A = 0,B = 0,C = 0}
pose8 ={X = 300, Y =  200, Z = 0,A = 0,B = 0,C = 0}

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