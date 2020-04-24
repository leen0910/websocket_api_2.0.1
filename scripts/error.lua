RCS={}
RCS[1]={X = 10, Y =  0, Z = -10,A = 0,B = 0,C = 0}

P = {}
P[1] = { X = 400, Y = 0, Z = 0, A = 0, B = 0, C = 0, POSE = 0, RCS = 1 }
P[2] = { X = 350, Y = 0, Z = 0, A = 0, B = 0, C = 0, POSE = 0 }
posit3 = {J1= 1, J2=   0, J3=-100, J4= 0, J5=0, J6=0}

point1={X = 20, Y =  0, Z = -20,A = 0,B = 0,C = 0}

--R.RCS(1,point1)

while (true)
do
R.WAIT_IO("LY9",1)



R.MP(P[1], 50, 50)
R.MP(P[2], 50, 50)
R.MP(posit3,50,50)
end