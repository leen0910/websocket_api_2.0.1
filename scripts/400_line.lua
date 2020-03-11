--400设备直线轨迹
vel=100;
blend=50;


--平行四边形
pose1 ={X = 300, Y =  200, Z = 0,A = 0,B = 0,C = 0}
pose2 ={X = 373.25018, Y = 3.55653, Z = 0,A = 0,B = 0,C = 0}
pose3 ={X = 300, Y =-200, Z = 0,A = 0,B = 0,C = 0}
pose4 ={X = 100, Y =  -300, Z = 0,A = 0,B = 0,C = 0}

R.MP(pose1,vel,blend)


while(1)
do
--平行四边形
    R.ML(pose2,vel,blend)
	R.ML(pose3,vel,blend)
	R.ML(pose4,vel,blend)
	R.ML(pose1,vel,blend)

end