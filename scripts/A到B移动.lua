--[[
吸盘吸取物体从A移动到B
p1：抓取位置
p11：抓取位置上方点
p2：目标位置
P21：目标位置上方点
vel：运动速度
v_slow：过渡速度
blend：运动过渡参数
EY1：吸盘工具 上/下
EY2：吸盘打开/关闭
t1：程序间间时间
t2： IO间隔时间
--]]


function move(p1,p11,p2,p21)

vel=100
blend=0
t2=100

R.MP(p11,vel,blend)  --移动到抓取位置上方
R.WAIT()   --等待运动结束
EY1=1  --吸盘工具下探
R.DELAY_MS(t2)
R.MP(p1,vel,blend)  --移动到抓取位置
R.WAIT()   --等待运动结束
EY2=1  --吸盘打开
R.DELAY_MS(t2)
R.MP(p11,vel,blend)  --移动到抓取位置上方
R.MP(p21,vel,blend)  --移动到目标位置上方
R.MP(p2,vel,blend)  --移动到目标位置
R.WAIT()   --等待运动结束
EY2=0  --吸盘关闭
R.DELAY_MS(t2)
R.MP(p21,vel,blend)  --移动到目标位置上方
R.WAIT()   --等待运动结束
EY1=0  --吸盘工具收回
R.DELAY_MS(t2)

end