# coding=utf-8
import unittest
import HTMLTestRunner
import time

for i in range(1,2):

    # 相对路径
    test_dir ='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\test_case'
    test_dir1 ='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\report'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    # 定义带有当前测试时间的报告
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = test_dir1 + '/' + now + 'result.html'
    # 二进制打开，准备写入文件
    fp = open(filename, 'wb')
    # 定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'websocket接口自动化测试报告/V_2.5.1', description=u'用例执行情况')
    runner.run(discover)
    fp.close()