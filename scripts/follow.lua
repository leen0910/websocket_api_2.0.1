   -- config
   encoder_count=2500  --
   encoder_perimeter=250  --


   --
   pose_ready={X = 400, Y =  0, Z = -50,A = 0,B = 0,C = 0}
   pose_ref = {X=450.428897, Y=-253.133021, Z=-49.994690, A=0, B=0, C=-0.924404}
   --
   pose_direction={X = 0, Y =  1, Z = 0,A = 0,B = 0,C = 0}
   --
   pose0 = {X = 0, Y =  0, Z = 0,A = 0,B = 0,C = 0}
   pose1 = {X = 0, Y =  0, Z = -70,A = 0,B = 0,C = 0}

   pose2= {X = -5, Y =  -5, Z = -70,A = 0,B = 0,C = 0}
   pose3= {X = 5, Y =  -5, Z = -70,A = 0,B = 0,C = 0}
   pose4= {X = 5, Y =  5, Z = -70,A = 0,B = 0,C = 0}
   pose5= {X = -5, Y =  5, Z = -70,A = 0,B = 0,C = 0}


   --
   R.modbus_connect(6)
   R.MV(false,0,true,100)
   R.DELAY(1)
   while(1)
   do
      R.MP(pose_ready,100,100)
      --
      R.WAIT_IO("M1X0",0)
      --
      modbus_value = M6D40
      conveyor_vel =(modbus_value/encoder_count)*encoder_perimeter
      R.FOLLOW(pose_ref,pose_direction,conveyor_vel,45)
      --
      R.MP(pose0,100,100)
      R.DELAY(1)
      --
      -- R.ML(pose2,100,100)
      -- R.DELAY(1)
      -- R.ML(pose3,100,100)
      -- R.ML(pose4,100,100)
      -- R.ML(pose5,100,100)
      -- R.ML(pose2,100,100)
      -- R.DELAY(1)
      --
      R.MP(pose1,100,100)
      R.DELAY(1)
      R.MP(pose0,100,100)
      R.FOLLOW_EXIT()
   end