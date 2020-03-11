--400，600通用三段直线轨迹
vel=100;
blend=50;

pose1 ={X = 200, Y =  300, Z = 0,A = 0,B = 0,C = 0}
pose2 ={X = 358.86856, Y =  98.87101, Z = 0,A = 0,B = 0,C = 0}
pose3 ={X = 300, Y =  -200, Z = 0,A = 0,B = 0,C = 0}
pose4 ={X = 200, Y =  -300, Z = 0,A = 0,B = 0,C = 0}




while(1)
do

--三段相连直线
	R.MP(pose1,vel,blend)
    R.ML(pose2,vel,blend)
    R.ML(pose3,vel,blend)
    R.ML(pose4,vel,blend)
end