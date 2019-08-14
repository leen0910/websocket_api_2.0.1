

pose_ref1={X =  0, Y =  0, Z = 0, A = 0, B = 0, C = 0}
pose_ref2={X = 10, Y = 10, Z = 0, A = 0, B = 0, C = math.pi/2}

-- 预先定义一些坨scara机械臂中,有效的是[X,Y,Z,c]
pose1 ={X = 350, Y =  0, Z = -50,A = 0,B = 0,C = 0}
posem1={X = 400, Y = 50, Z = -50,A = 0,B = 0,C = 0}
pose2 ={X = 450, Y =  0, Z = -50,A = 0,B = 0,C = 0}
posem2={X = 400, Y =-50, Z = -50,A = 0,B = 0,C = 0}
posel1 ={X = 350, Y =  100, Z = -50,A = 0,B = 0,C = 0}
posel2 ={X = 350, Y = -100, Z = -50,A = 0,B = 0,C = 0}

-- 预先定义一些关节点,在scara机械臂中,有效的是[j1,j2,j3,j4],其中j3为Z轴,依然表示Z方向的长度
posit1={J1= 0,J2= 0,J3=   0,J4=0,J5=0,J6=0}
posit2={J1=-1.8,J2=2,J3=   0,J4=0,J5=0,J6=0}
posit3={J1= 1.8,J2=-2,J3=-100,J4=0,J5=0,J6=0}
posit4={J1= 1.8,J2=2,J3=   0,J4=0,J5=0,J6=0}

-- 预先定义运动速度和过渡参数
vel  =100
blend=0

-- 点到点运动,目标点为关节值
--R.MP(pose1,vel,blend)
while(1)
do
  R.MP(posit1,vel,blend)
  R.MP(posit2,vel,blend)
  R.DELAY_MS(500)
  R.MP(posit3,vel,blend)
  R.DELAY_MS(500)
  R.MP(posit2,vel,blend)
  R.DELAY_MS(500)
  R.MP(posit1,vel,blend)


  loop=3
  R.MP(posel2,vel,blend,0)
  R.DELAY(1)
  R.MP(posel2,vel,blend,1)
  R.DELAY(1)
  R.ML(pose1,vel,blend)
  while(loop>0)
  do
      loop=loop-1;
      R.MC(posem1,pose2,vel,blend)
      R.MC(posem2,pose1,vel,blend)
  end
-- 等待运动结束
  R.WAIT()
-- 设置为世界坐标系
  R.RCS(pose_ref1)
  R.ML(posel1,vel,blend)
-- 调节运动速度
--vel=80

--R.DELAY(1)

-- 回到开始点
  R.MP(posit1,vel,blend)
  R.DELAY(1)
end
-- 结束