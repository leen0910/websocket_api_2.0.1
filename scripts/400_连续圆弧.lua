--400连续圆弧轨迹
vel=100;
blend=0;

--F点开始
pose1 ={X = 325.06757, Y =  144.23063, Z = 0,A = 0,B = 0,C = 0}
pose2 ={X = 292.87358, Y = 141.16453, Z = 0,A = 0,B = 0,C = 0}
pose3 ={X = 266.04526, Y = 130.4332, Z = 0,A = 0,B = 0,C = 0}
pose4 ={X = 240, Y =  100, Z = 0,A = 0,B = 0,C = 0}
pose5 ={X = 248.41521, Y = 35.38428, Z = 0,A = 0,B = 0,C = 0}
pose6 ={X =272.94397, Y = -19.0389, Z = 0,A = 0,B = 0,C = 0}
pose7 ={X = 275.24354, Y =-88.02602, Z = 0,A = 0,B = 0,C = 0}
pose8 ={X = 276.01006, Y = -124.81916, Z = 0,A = 0,B = 0,C = 0}
pose9 ={X = 291.34053, Y = -159.31272, Z = 0,A = 0,B = 0,C = 0}
pose10 ={X = 325.8341, Y = -171.5771, Z = 0,A = 0,B = 0,C = 0}
pose11 ={X = 360.3683, Y = -135.64671, Z = 0,A = 0,B = 0,C = 0}
pose12 ={X = 376.13343, Y = -94.26325, Z = 0,A = 0,B = 0,C = 0}
pose13 ={X = 389.92792, Y = -29.2321, Z = 0,A = 0,B = 0,C = 0}
pose14 ={X = 388.68903, Y = 53.01432, Z = 0,A = 0,B = 0,C = 0}
pose15 ={X = 372.59204, Y =99.77226, Z = 0,A = 0,B = 0,C = 0}
pose16 ={X = 351.8959, Y =  125.06754, Z = 0,A = 0,B = 0,C = 0}

R.MP(pose1,vel,blend)

while(1)
do

--
	R.MP(pose1,vel,blend)
    R.MC(pose2,pose3,vel,blend)
    R.MC(pose4,pose5,vel,blend)
    R.MC(pose6,pose7,vel,blend)
    R.MC(pose8,pose9,vel,blend)
    R.MC(pose10,pose11,vel,blend)
    R.MC(pose12,pose13,vel,blend)
    R.MC(pose14,pose15,vel,blend)
    R.MC(pose16,pose1,vel,blend)

end