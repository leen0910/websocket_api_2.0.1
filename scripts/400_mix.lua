--400设备多种路径组合
vel=100;
blend={BLEND=100};



pose1 ={X = -292.98387, Y =  149.69718, Z = 0,A = 0,B = 0,C = 0}

pose2 ={X = -193.74803, Y = 314.33846, Z = 0,A = 0,B = 0,C = 0}
pose3 ={X = -86.2539, Y =  202.91405, Z = 0,A = 0,B = 0,C = 0}
pose4 ={X = 38.42454, Y =  202.91405, Z = 0,A = 0,B = 0,C = 0,POSE=1}
pose5 ={X = 38.42454, Y =  321.35857, Z = 0,A = 0,B = 0,C = 0}
pose6 ={X = 187.40778, Y =  323.35989, Z = 0,A = 0,B = 0,C = 0}
pose7 ={X = 329.49546, Y =  158.71862, Z = 0,A = 0,B = 0,C = 0}
pose8 ={X = 248.29992, Y = 3.42854, Z = 0,A = 0,B = 0,C = 0}
pose9 ={X = 296.09332, Y = -144.10761, Z = 0,A = 0,B = 0,C = 0}
pose10 ={X = 243.95506, Y = -219.4814, Z = 0,A = 0,B = 0,C = 0}
pose11 ={X = 173.30395, Y =  -190.38976, Z = 0,A = 0,B = 0,C = 0}
pose110 ={X = 246.5, Y =  -88.9, Z = 0,A = 0,B = 0,C = 0}

pose12 ={X = 323.10698, Y =  -206.44683, Z = 0,A = 0,B = 0,C = 0,POSE=1}
pose13 ={X = -229.83379, Y =  -265.28903, Z = 0,A = 0,B = 0,C = 0}
pose14 ={X = -123.83188, Y =  -355.50343, Z = 0,A = 0,B = 0,C = 0}
pose15 ={X = -58.42644, Y =  -353.24807, Z = 0,A = 0,B = 0,C = 0,POSE=0}
pose16 ={X = -56.17108, Y =  -278.82119, Z = 0,A = 0,B = 0,C = 0}
pose17 ={X = 0.21292, Y =  -276.56583, Z = 0,A = 0,B = 0,C = 0}
pose18 ={X = 2.46828, Y =   -355.50343, Z = 0,A = 0,B = 0,C = 0}
pose19 ={X = 65.61835, Y =  -357.75879, Z = 0,A = 0,B = 0,C = 0}
pose20 ={X = 63.36299, Y =  -272.05511, Z = 0,A = 0,B = 0,C = 0}
pose21 ={X = 125.51055, Y =  -271.43075, Z = 0,A = 0,B = 0,C = 0}
pose22 ={X = 131.02379, Y =  -350.99271, Z = 0,A = 0,B = 0,C = 0}
pose23 ={X = 287.78143, Y =  -227.22657, Z = 0,A = 0,B = 0,C = 0}
pose24 ={X = 100.57486, Y =  371.70221, Z = 0,A = 0,B = 0,C = 0}






while(1)
do
    R.MP(pose1,vel,blend)
    R.ML(pose2,vel,blend)
	R.ML(pose3,vel,blend)
	R.ML(pose4,vel,blend)
	R.ML(pose5,vel,blend)
    R.ML(pose6,vel,blend)
	R.MC(pose7,pose8,vel,blend)
	R.ML(pose9,vel,blend)
	R.MC(pose10,pose11,vel,blend)
    R.MC(pose110,pose9,vel,blend)

	--R.MP(pose9,vel,blend)
	R.ML(pose12,vel,blend)
        R.MP(pose12,vel,blend)
	R.ML(pose13,vel,blend)
    R.ML(pose14,vel,blend)
	R.ML(pose15,vel,blend)
	R.ML(pose16,vel,blend)
	R.ML(pose17,vel,blend)
    R.ML(pose18,vel,blend)
    R.ML(pose19,vel,blend)
	R.ML(pose20,vel,blend)
	R.ML(pose21,vel,blend)
	R.ML(pose22,vel,blend)
    R.ML(pose23,vel,blend)
    R.MP(pose23,vel,blend)
    R.ML(pose24,vel,blend)

end