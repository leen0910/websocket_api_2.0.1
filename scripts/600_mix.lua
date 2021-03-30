--600设备多种路径组合
vel=100;
blend={BLEND=50};



pose1 ={X = -400.91962, Y =  291.44289, Z = 0,A = 0,B = 0,C = 0}
pose2 ={X = -400, Y =  400, Z = 0,A = 0,B = 0,C = 0}
pose3 ={X = -300, Y = 300, Z = 0,A = 0,B = 0,C = 0}
pose4 ={X = -200, Y =  300, Z = 0,A = 0,B = 0,C = 0}
pose5 ={X = -200, Y =  500, Z = 0,A = 0,B = 0,C = 0}
pose6 ={X = 0, Y =  500, Z = 0,A = 0,B = 0,C = 0}
pose7 ={X = 200, Y =  500, Z = 0,A = 0,B = 0,C = 0}
pose8 ={X = 200, Y =  300, Z = 0,A = 0,B = 0,C = 0}
pose9 ={X = 500, Y =  -100, Z = 0,A = 0,B = 0,C = 0}
pose10 ={X = 400, Y =  -200, Z = 0,A = 0,B = 0,C = 0}
pose11 ={X = 400, Y =  -100, Z = 0,A = 0,B = 0,C = 0}
pose110 ={X = 445.8, Y =  -79.4, Z = 0,A = 0,B = 0,C = 0}

pose12 ={X = 545.39579, Y =  -170.07112, Z = 0,A = 0,B = 0,C = 0,POSE=1}
pose13 ={X = -206.15225, Y =  -504.56292, Z = 0,A = 0,B = 0,C = 0}
pose14 ={X = 0, Y =  -569.99105, Z = 0,A = 0,B = 0,C = 0}
pose15 ={X = 97.73875, Y =  -569.99105, Z = 0,A = 0,B = 0,C = 0}
pose16 ={X = 100, Y = -400, Z = 0,A = 0,B = 0,C = 0}
pose17 ={X = 200, Y = -400, Z = 0,A = 0,B = 0,C = 0}
pose18 ={X = 200, Y = -500, Z = 0,A = 0,B = 0,C = 0}
pose19 ={X = 300, Y =  -500, Z = 0,A = 0,B = 0,C = 0}
pose20 ={X = 300, Y =  -300, Z = 0,A = 0,B = 0,C = 0}
pose21 ={X = 400, Y =  -300, Z = 0,A = 0,B = 0,C = 0}
pose22 ={X = 400, Y =  -400, Z = 0,A = 0,B = 0,C = 0}
pose23 ={X = 500, Y =  300, Z = 0,A = 0,B = 0,C = 0,POSE=0}
pose24 ={X = -321.81943, Y =  470.0438, Z = 0,A = 0,B = 0,C = 0}





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
	R.MC(pose10,pose9,vel,blend)
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