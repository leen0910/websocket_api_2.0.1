-- 关节坐标
vel=100;
blend=0;


posit1 =  {J1=1.112, J2=1.158, J3=-71.029, J4=-0.000, J5=0, J6=0 }
posit2 =  {J1=0.423, J2=-1.497, J3=-71.029, J4=-0.000, J5=0, J6=0 }
posit3 =  {J1=-0.293, J2=-0.013, J3=-71.029, J4=-0.000, J5=0, J6=0 }
posit4 =  {J1=-0.220, J2=-1.130, J3=-71.029, J4=-0.000, J5=0, J6=0 }
posit5 =  {J1=-0.308, J2=-1.051, J3=-71.028, J4=-0.000, J5=0, J6=0 }


while(1)
do
	R.MP(posit1,vel,blend)
	R.MP(posit2,vel,blend)
	R.MP(posit3,vel,blend)
	R.MP(posit4,vel,blend)
	R.WAIT()
	R.MP(posit5,vel,blend)
	R.DELAY(5)
	R.MP(posit4,vel,blend)
	R.MP(posit3,vel,blend)
end