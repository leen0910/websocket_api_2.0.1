

--[[
--打开温控设置温度300度

R.MODBUS_DISCONNECT(5)
R.DELAY_MS(200)

R.DELAY_MS(200)
R.MODBUS_CONNECT(5)
R.DELAY_MS(200)
--]]



P = {}
P[1] =  {X=400, Y=0, Z=0, A=0.000, B=0.000, C=0, POSE=1} --安全位置

P[2] = {X=135.138, Y=-316.540, Z=-83.466, A=0.000, B=0.000, C=1.696, POSE=1}  --打表检测位置406
P[3] = {X=163.112, Y=-316.539, Z=-83.466, A=0.000, B=0.000, C=1.696, POSE=1}--打表过渡0
P[31] = {X=163.112, Y=-316.539, Z=4.986, A=0.000, B=0.000, C=1.696, POSE=1}--打表上方值



P[4]={X=-54.807, Y=-216.748, Z=-11.308, A=0.000, B=0.000, C=1.696, POSE=1} --吹气位置
P[5]= {X=-54.807, Y=-216.748, Z=4.986, A=0.000, B=0.000, C=1.696, POSE=1}--吹气位置过渡点


P[7]={X=366.139, Y=63.177, Z=-87.019, A=0.000, B=0.000, C=0.151, POSE=1} --焊点1
P[8]={X=366.139, Y=63.177, Z=-74.383, A=0.000, B=0.000, C=0.151, POSE=1}--焊点1过渡
P[81]={X=366.139, Y=63.177, Z=4.9, A=0.000, B=0.000, C=0.151, POSE=1}--焊点1上方


P[9]={X=232.763186, Y=-434.493617, Z=-119.522563, A=0, B=0, C=1.692767,POSE = 0} --焊点2
P[10]={X=232.763534, Y=-386.719512, Z=-119.522705, A=0, B=0, C=1.692770,POSE = 0}--焊点2上方过渡


R.MP(P[1], 100, 0)

R.DELAY_MS(100)



--吹气去杂质
R.MP(P[5], 100, 0)
R.WAIT()
R.MP(P[4], 20, 0)
B0Y6=1
R.DELAY(2)
B0Y6=0
R.MP(P[5], 100, 0)

--打表检测位置
R.MODBUS_CONNECT(6)
R.DELAY_MS(100)
R.MP(P[31], 100, 0)
R.MP(P[3], 100, 0)
R.WAIT()
R.MP(P[2], 20, 0)
R.DELAY(5)
var=M6D0
R.DELAY_MS(100)

if (var>=456 or var<=356)
then
R.MP(P[3], 20, 0)
R.MP(P[31], 60, 0)
R.MP(P[1], 60, 0)
exit()
else
--焊点1
R.MP(P[3], 20, 0)
R.MP(P[31], 60, 0)
R.MP(P[81], 100, 0)
R.MP(P[8], 100, 0)
R.WAIT()
R.DELAY(2)
R.MP(P[7], 20, 0)
R.WAIT()
R.DELAY(4)
B0Y0=1
R.DELAY_MS(1500)
R.MP(P[8], 50, 0)
B0Y0=0
R.DELAY_MS(100)
R.MP(P[81], 100, 0)
R.MP(P[1], 100, 0)
end
