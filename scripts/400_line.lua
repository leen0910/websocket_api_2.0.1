--[[
--400设备直线轨迹
vel=100;
blend=50;


--平行四边形
pose0 ={J1 = 1, J2 =  -1, J3= 0,J4= 0}
pose1 ={X = 250, Y =  -50, Z = 0,A = 0,B = 0,C = 0}
pose2 ={X = 250, Y = 50, Z = 0,A = 0,B = 0,C = 0}
pose3 ={X = 350, Y =50, Z = 0,A = 0,B = 0,C = 0}
pose4 ={X = 350, Y =  -50, Z = 0,A = 0,B = 0,C = 0}

R.MP(pose0,vel,blend)


while(1)
do
--平行四边形
    R.ML(pose1,vel,blend)
	R.ML(pose2,vel,blend)
	R.ML(pose3,vel,blend)
	R.ML(pose4,vel,blend)

end
]]--
--400设备直线轨迹
vel=100;
blend=50;


--平行四边形
pose0 ={J1 = 1, J2 =  -1, J3= 0,J4= 0}
pose1 ={X = 330, Y =  -120, Z = 0,A = 0,B = 0,C = 0}
pose2 ={X = 330, Y = 120, Z = 0,A = 0,B = 0,C = 0}
pose3 ={X = 380, Y =120, Z = 0,A = 0,B = 0,C = 0}
pose4 ={X = 380, Y =  -120, Z = 0,A = 0,B = 0,C = 0}

R.MP(pose0,vel,blend)


while(1)
do
--平行四边形

    R.ML(pose1,vel,blend)
	R.ML(pose2,vel,blend)
	R.ML(pose3,vel,blend)
	R.ML(pose4,vel,blend)

end