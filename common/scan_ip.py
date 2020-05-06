import sys
import json

if __name__ == "__main__":
    # \u4e2d\u6587\u6d4b\u8bd5
    # if len(sys.argv) != 2:
    #     exit(1)

    str1 = "\u4e2d\u6587\u6d4b\u8bd5"
    print(str1)
    print(str1.encode('utf8'))
    print(str1.encode('utf8').decode('utf8'))
    #

    file_name = "C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\files\\dev_modifiable_info.json"
    # 打开文件
    file_handle = open(file_name,encoding="utf-8")
    file_detail = file_handle.read()
    # 源
    print(file_detail)
    file_handle.close()
    # json
    json_dict = json.load(open(file_name,encoding="utf-8"))
    print(json_dict)
    json_dict["device_name"] = '中文测试'
    print(json_dict)
    # 转str
    json_str = json.dumps(json_dict,ensure_ascii=False)
    print(json_str)

    # 写入
    file_handle = open(file_name,'w',encoding="utf-8")
    file_handle.write(json_str)
    exit(0)