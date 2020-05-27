pose1 ={X = 300, Y =  200, Z = 0,A = 0,B = 0,C = 0}
pose2 ={X = 373.25018, Y = 3.55653, Z = 0,A = 0,B = 0,C = 0}
pose3 ={X = 300, Y =-200, Z = 0,A = 0,B = 0,C = 0}
pose4 ={X = 100, Y =  -300, Z = 0,A = 0,B = 0,C = 0}
vel=100
blend=0

--[[
 a=M0D10
 b=M0D11
 c=M0D12
 d=M0D13
 ref_x={a,b,c,d}
 f=R.INT_TO_DOUBLE(ref_x)
print("f的值是:",f)
--]]


--[[
R.DELAY_MS(1000)

R.MODBUS_WRITE(2,"motor_speed",25)
R.DELAY_MS(100)
--]]


R.MODBUS_WRITE(2,"follow_ref_X",352.146)
R.DELAY_MS(100)
R.MODBUS_WRITE(2,"type_id",30)
R.DELAY_MS(100)
R.MODBUS_WRITE(2,"motor_on",1)
R.DELAY_MS(100)
R.MODBUS_WRITE(0,"motor_speed",2500)
R.DELAY_MS(100)
R.MODBUS_WRITE(0,"follow_ref_X",352.146)
R.DELAY_MS(100)
R.MODBUS_WRITE(0,"type_id",30)
R.DELAY_MS(100)


print(R.MODBUS_READ(2,"motor_speed"))
R.DELAY_MS(100)
print(R.MODBUS_READ(2,"follow_ref_X"))
R.DELAY_MS(100)
print(R.MODBUS_READ(2,"motor_on"))
R.DELAY_MS(100)
print(R.MODBUS_READ(2,"type_id"))
R.DELAY_MS(100)
print(R.MODBUS_READ(0,"motor_speed"))
R.DELAY_MS(100)
print(R.MODBUS_READ(0,"follow_ref_X"))
R.DELAY_MS(100)
print(R.MODBUS_READ(0,"type_id"))


--[[
print(M2D62)
R.DELAY_MS(1000)

a=M0D62
R.DELAY_MS(1000)
R.WAIT_IO("M0D62",12)


R.MP(pose1,vel,blend)
 R.ML(pose2,vel,blend)
R.ML(pose3,vel,blend)
R.ML(pose4,vel,blend)
R.ML(pose1,vel,blend)
--]]
