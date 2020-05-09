# class Testclass:
#
#     def __init__(self):
#         pass
#
#     def setup(self):
#         print('start')
#
#     def teardown(self):
#         print('stop')
#
#     def testfunc1(self):
#         print('this is case1')
#
#     def testfunc2(self):
#         print('this is case2')
#
#     def testfunc3(self):
#         print('this is case3')

import json

data={
    "action":"publish.motion.info",
    "data":{
        "cart_pose":[0,0,0,0,0,0],
        "joint_info":
        {
            "arm_joint":[
                {
                    "driver_id":0,
                    "posit":0.0,
                    "velocity":0.0,
                    "torque":0.0,
                    "hard_limit":[0.0,0.0],
                    "voltage":0.0,
                    "temperature":0.0
                },
                {
                    "driver_id":1,
                    "posit":1.0,
                    "velocity":1.0,
                    "torque":1.0,
                    "hard_limit":[0.0,0.0],
                    "voltage":1.0,
                    "temperature":1.0
                }
            ],
            "ext_joint":[]
        },

    }
}
data=json.dumps(data)
data=json.loads(data)
lenth=len(data["data"])
# print("[%s,2]"%data["data"]["joint_info"]["arm_joint"][0]["posit"])
# data_1 = ['hello','world']
# data_2 = {'name': '小明', 'age': 12}
# print('{0} {1} 我的名字是{name},我今年{age}岁了,{0}!'.format(*data_1, **data_2))
i=0
J=[]
while i < 4:
    J.append(i*100)
    i=i+1
print(J)


