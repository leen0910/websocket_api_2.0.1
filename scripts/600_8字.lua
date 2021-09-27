--600_4个圆弧组成8字轨迹
vel=100;
blend={BLEND=50};

HOME = {J1=0, J2=0, J3=0, J4=0}

--第一组圆弧起始点，经过点，目标点
pose1 ={X = 435.69135,Y =146.20794, Z = 0,A = 0,B = 0,C = 0}
pose2 ={X = 480.39536, Y =308.46697, Z = 0,A = 0,B = 0,C = 0}
pose3 ={X = 328.07056, Y =378.00655, Z = 0,A = 0,B = 0,C = 0}

--第二组圆弧经过点，起始点是pose3，目标点是pose1

pose4 ={X =313.16922, Y =204.15759, Z = 0,A = 0,B = 0,C = 0}

--第三组圆弧经过点，目标点，起始点是pose1

pose5 ={X =570.63125, Y =62.59487, Z = 0,A = 0,B = 0,C = 0}
pose6 ={X =516.82086, Y =-113.73765, Z = 0,A = 0,B = 0,C = 0}

--第四组圆弧经过点，起始点是pose6，目标点是pose1
pose7 ={X =393.47089, Y =-33.43598, Z = 0,A = 0,B = 0,C = 0}

R.MP(HOME,vel,blend)

while(1)
do

R.MP(pose1,vel,blend)
R.MC(pose2,pose3,vel,blend)
R.MC(pose5,pose6,vel,blend)
R.MC(pose7,pose1,vel,blend)
end