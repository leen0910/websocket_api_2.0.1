

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
blend1=0
blend2=0
blend3=0
blend4=0

-- 点到点运动,目标点为关节值
--R.MP(pose1,vel,blend2)
while(1)
do
  R.MP(posit1,vel,blend)
  R.MP(posit2,vel,blend1)
  R.DELAY_MS(500)
  R.MP(posit3,vel,blend2)
  R.DELAY_MS(500)
  R.MP(posit2,vel,blend3)
  R.DELAY_MS(500)
  R.MP(posit1,vel,blend4)
  MT23200=0
  R.DELAY_MS(500)
  MT23100=100
  R.DELAY_MS(500)
  print(LX0)
  print(LX1)
  print(LX2)
  print(LX3)
  print(LX4)
  print(LX5)
  LY0=1
  LY1=1
  LY2=1
  LY3=1
  LY4=1
  LY5=1
  LY6=1
  LY7=1
  LY8=1
  LY9=1
  LY10=1
  LZ0=1

  loop=3
  R.MP(posel2,vel,blend,0)
  R.DELAY(1)
  R.MP(posel2,vel,blend1,1)
  R.DELAY(1)
  R.ML(pose1,vel,blend2)
  MT23100=0
  R.DELAY_MS(500)
  MT23300=300
  R.DELAY_MS(500)
  print(LX0)
  print(LX1)
  print(LX2)
  print(LX3)
  print(LX4)
  print(LX5)
  LY0=0
  LY1=0
  LY2=0
  LY3=0
  LY4=0
  LY5=0
  LY6=0
  LY7=0
  LY8=0
  LY9=0
  LY10=0
  LZ0=0
  while(loop>0)
  do
      loop=loop-1;
      R.MC(posem1,pose2,vel,blend3)
      R.MC(posem2,pose1,vel,blend)
      MT23300=0
      R.DELAY_MS(500)
      MT23200=200
      R.DELAY_MS(500)
  print(LX0)
  print(LX1)
  print(LX2)
  print(LX3)
  print(LX4)
  print(LX5)
  LY0=1
  LY1=1
  LY2=1
  LY3=1
  LY4=1
  LY5=1
  LY6=1
  LY7=1
  LY8=1
  LY9=1
  LY10=1
  LZ0=1
  end
-- 等待运动结束
  R.WAIT()
-- 设置为世界坐标系
  R.RCS(pose_ref1)
  R.ML(posel1,30,blend4)
-- 调节运动速度
--vel=80

--R.DELAY(1)

-- 回到开始点
  R.MP(posit1,vel,blend)
  R.DELAY(1)
end
-- 结束
