
pose1 ={X = 300, Y =  200, Z = 0,A = 0,B = 0,C = 0}
pose2 ={X = 373.25018, Y = 3.55653, Z = 0,A = 0,B = 0,C = 0}
pose3 ={X = 300, Y =-200, Z = 0,A = 0,B = 0,C = 0}
pose4 ={X = 100, Y =  -300, Z = 0,A = 0,B = 0,C = 0}
vel=100
blend=0



while (true)
do
 a=M0D10
 b=M0D11
 c=M0D12
 d=M0D13
 ref_x={a,b,c,d}


R.MODBUS_CONNECT(5)
R.DELAY_MS(500)


M1D5=345
R.DELAY_MS(100)
R.INFO("打表值：",M1D5)
R.DELAY_MS(100)

print(EX0)
R.DELAY_MS(100)
print(EX1)
R.DELAY_MS(100)
print(EX2)
R.DELAY_MS(100)
print(EX3)
R.DELAY_MS(100)
print(EX4)
R.DELAY_MS(100)
print(EX5)
R.DELAY_MS(100)
print(EX6)
R.DELAY_MS(100)
print(EX7)
R.DELAY_MS(100)
print(EX8)
R.DELAY_MS(100)
print(EX9)
R.DELAY_MS(100)
print(EX10)
R.DELAY_MS(100)
print(EX11)
R.DELAY_MS(100)
print(EX12)
R.DELAY_MS(100)
print(EX13)
R.DELAY_MS(100)
print(EX14)
R.DELAY_MS(100)
print(EY16)
R.DELAY_MS(100)
print(EY17)
R.DELAY_MS(100)

EY0=0
R.DELAY_MS(100)
EY1=0
R.DELAY_MS(100)
EY2=0
R.DELAY_MS(100)
EY3=0
R.DELAY_MS(100)
EY4=0
R.DELAY_MS(100)
EY5=0
R.DELAY_MS(100)
EY6=0
R.DELAY_MS(100)
EY7=0
R.DELAY_MS(100)
EY8=0
R.DELAY_MS(100)
EY9=0
R.DELAY_MS(100)
EY10=0
R.DELAY_MS(100)
EY11=0
R.DELAY_MS(100)
EY12=0
R.DELAY_MS(100)
EY13=0
R.DELAY_MS(100)
EY14=0
R.DELAY_MS(100)
EY15=0
R.DELAY_MS(100)

EY0=1
R.DELAY_MS(100)
EY1=1
R.DELAY_MS(100)
EY2=1
R.DELAY_MS(100)
EY3=1
R.DELAY_MS(100)
EY4=1
R.DELAY_MS(100)
EY5=1
R.DELAY_MS(100)
EY6=1
R.DELAY_MS(100)
EY7=1
R.DELAY_MS(100)
EY8=1
R.DELAY_MS(100)
EY9=1
R.DELAY_MS(100)
EY10=1
R.DELAY_MS(100)
EY11=1
R.DELAY_MS(100)
EY12=1
R.DELAY_MS(100)
EY13=1
R.DELAY_MS(100)
EY14=1
R.DELAY_MS(100)
EY15=1
R.DELAY_MS(100)


--[[
R.MODBUS_WRITE(2,"motor_speed",25)
R.DELAY_MS(100)



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

]]--

print(M2D62)
R.DELAY_MS(1000)

a=M0D3
R.DELAY_MS(1000)
R.WAIT_IO("M0D3",a)


R.MP(pose1,vel,blend)
 R.ML(pose2,vel,blend)
R.ML(pose3,vel,blend)
R.ML(pose4,vel,blend)
R.ML(pose1,vel,blend)

R.DELAY_MS(100)

print(M5X0)
R.DELAY_MS(100)
print(M5X1)
R.DELAY_MS(100)
print(M5X2)
R.DELAY_MS(100)
print(M5X3)
R.DELAY_MS(100)
print(M5X4)
R.DELAY_MS(100)
print(M5X5)
R.DELAY_MS(100)
print(M5X6)
R.DELAY_MS(100)
print(M5X7)

M5Y0=0
R.DELAY_MS(100)
M5Y1=0
R.DELAY_MS(100)
M5Y2=0
R.DELAY_MS(100)
M5Y3=0
R.DELAY_MS(100)
M5Y4=0
R.DELAY_MS(100)
M5Y5=0
R.DELAY_MS(100)
M5Y6=0
R.DELAY_MS(100)
M5Y7=0
R.DELAY_MS(100)

M5Y0=1
R.DELAY_MS(100)
M5Y1=1
R.DELAY_MS(100)
M5Y2=1
R.DELAY_MS(100)
M5Y3=1
R.DELAY_MS(100)
M5Y4=1
R.DELAY_MS(100)
M5Y5=1
R.DELAY_MS(100)
M5Y6=1
R.DELAY_MS(100)
M5Y7=1
R.DELAY_MS(100)




R.DELAY_MS(100)
M3Y1280=0
R.DELAY_MS(100)
M3Y1281=0
R.DELAY_MS(100)
M3Y1282=0
R.DELAY_MS(100)
M3Y1283=0
R.DELAY_MS(100)
M3Y1284=0
R.DELAY_MS(100)
M3Y1285=0
R.DELAY_MS(100)
M3Y1286=0
R.DELAY_MS(100)
M3Y1287=0
R.DELAY_MS(100)

M3Y1280=1
R.DELAY_MS(100)
M3Y1281=1
R.DELAY_MS(100)
M3Y1282=1
R.DELAY_MS(100)
M3Y1283=1
R.DELAY_MS(100)
M3Y1284=1
R.DELAY_MS(100)
M3Y1285=1
R.DELAY_MS(100)
M3Y1286=1
R.DELAY_MS(100)
M3Y1287=1
R.DELAY_MS(100)


print(M3X1024)
R.DELAY_MS(100)
print(M3X1025)
R.DELAY_MS(100)
print(M3X1026)
R.DELAY_MS(100)
print(M3X1027)
R.DELAY_MS(100)
print(M3X1028)
R.DELAY_MS(100)
print(M3X1029)
R.DELAY_MS(100)
print(M3X1030)
R.DELAY_MS(100)
print(M3X1031)
R.DELAY_MS(100)


M1D5=0
R.DELAY_MS(100)
R.INFO("打表值回零：",M1D5)
R.DELAY_MS(100)

M3Y2048=32
R.DELAY_MS(100)

print(M3Y2048)
R.DELAY_MS(100)
M3Y45056=236
R.DELAY_MS(100)
print(M3Y45056)
R.DELAY_MS(100)

M3D4096=256
R.DELAY_MS(100)
M3D36864=3333
R.DELAY_MS(100)
print(M3D4096)
R.DELAY_MS(100)
print(M3D36864)


end
