--400，600通用两段圆弧轨迹
vel=100;
blend=50;

pose1 ={X = 300, Y =  200, Z = 0,A = 0,B = 0,C = 0}
pose2 ={X = 350, Y =  150, Z = 0,A = 0,B = 0,C = 0}
pose3 ={X = 350, Y =  50, Z = 0,A = 0,B = 0,C = 0}
pose4 ={X = 350, Y =  -50, Z = 0,A = 0,B = 0,C = 0}
pose5 ={X = 371.62485, Y =  -98.88305, Z = 0,A = 0,B = 0,C = 0}



while(1)
do
--两段相连圆弧
	R.MP(pose1,vel,blend)
    R.MC(pose2,pose3,vel,blend)
    R.MC(pose4,pose5,vel,blend)
end