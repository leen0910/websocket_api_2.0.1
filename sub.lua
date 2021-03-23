--测试写入sub_script文件123

--测试写入sub_script文件123


while (1)
do

R.DELAY(1)
M0D19=1
R.INFO("M0D19:", M0D19)

R.DELAY_MS(500)
M1D3=33333333
R.INFO("M1D3-3:", M1D3)




R.DELAY_MS(500)
a=R.GET("POSIT")
R.INFO("J1:","测试")
R.INFO("J1:",a["J1"])
R.INFO("J2:",a["J2"])
R.INFO("J3:",a["J3"])
R.INFO("J4:",a["J4"])
R.DELAY_MS(500)
c=R.GET("POSE",0)
R.INFO("X:",c["X"])
R.INFO("Y:",c["Y"])
R.INFO("Z:",c["Z"])
R.INFO("A:",c["A"])
R.INFO("B:",c["B"])
R.INFO("C:",c["C"])

R.DELAY_MS(500)
b=R.GET("POSE","CHAIN0")
R.INFO("X:",b["X"])
R.INFO("Y:",b["Y"])
R.INFO("Z:",b["Z"])
R.INFO("A:",b["A"])
R.INFO("B:",b["B"])
R.INFO("C:",b["C"])


end