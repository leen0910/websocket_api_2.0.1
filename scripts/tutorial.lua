-- 关节坐标
vel=100;
blend=50;

posit0 = {J1=   0, J2=   0, J3=   0, J4= 0, J5=0, J6=0}
posit1 = {J1= 1.8, J2= 1.8, J3=   0, J4= 0, J5=0, J6=0}
posit2 = {J1=-1.8, J2=-1.8, J3=   0, J4= 0, J5=0, J6=0}
posit3 = {J1=   0, J2=   0, J3=-100, J4= 0, J5=0, J6=0}
posit4 = {J1=   0, J2=   0, J3=   0, J4=-6, J5=0, J6=0}
posit5 = {J1=   0, J2=   0, J3=   0, J4= 6, J5=0, J6=0}


while(1)
do
	R.MP(posit0,vel,blend)
	R.MP(posit1,vel,blend)
	R.MP(posit2,vel,blend)
	R.MP(posit0,vel,blend)
	R.MP(posit3,vel,blend)
	R.MP(posit0,vel,blend)
	R.MP(posit4,vel,blend)
	R.MP(posit5,vel,blend)
end
