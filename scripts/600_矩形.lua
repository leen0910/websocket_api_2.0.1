--600设备直线轨迹
vel=100;
blend={BLEND=0};


--不规则四边形
pose1 ={X = 300, Y =  200, Z = 0,A = 0,B = 0,C = 0}
pose2 ={X = 300, Y =  -200, Z = 0,A = 0,B = 0,C = 0}
pose3 ={X = 500, Y = -200, Z = 0,A = 0,B = 0,C = 0}
pose4 ={X = 500, Y =  200, Z = 0,A = 0,B = 0,C = 0}

R.MP(pose1,vel,blend)


while(1)
do
--矩形
    R.ML(pose1,vel,blend)
	R.ML(pose2,vel,blend)
	R.ML(pose3,vel,blend)
	R.ML(pose4,vel,blend)

end