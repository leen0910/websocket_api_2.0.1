vel=100;
blend=0;


pose0 ={J3=0}
pose1 = {J1= 0,J2= 0,J3=0,J4=0,J5=0,J6=0} --安全点

pose2 = {X=434.820, Y=69.220, Z=-6.288, A=0.000, B=0.000, C=0.483, POSE=0} --中间点
pose3 = {X=283.348, Y=-283.701, Z=-82.694, A=0.000, B=0.000, C=-0.353, POSE=0} --过渡点
pose4 ={X=299.008, Y=-283.701, Z=-82.694, A=0.000, B=0.000, C=-0.353, POSE=0} --目标点
pose5 = {X=283.348, Y=-283.701, Z=0, A=0.000, B=0.000, C=-0.353, POSE=0} --过渡点上方



R.DELAY_MS(200)
R.MODBUS_CONNECT(6)
R.DELAY_MS(200)
R.MP(pose0,vel,blend)
R.MP(pose1,vel,blend)

while(1)
do
    R.MP(pose2,vel,blend)
    R.MP(pose5,vel,blend)
    R.MP(pose3,vel,blend)
    R.WAIT()
    R.MP(pose4,1,blend)
    R.DELAY(5)
    R.INFO("打表值：",M6D0)
    R.DELAY_MS(200)
    R.MP(pose3,2,blend)
    R.WAIT()
    R.MP(pose5,vel,blend)

end