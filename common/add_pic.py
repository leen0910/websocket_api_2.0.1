
import imageio

import glob
import matplotlib.pyplot as plt
import os

def add_icon():
    path='/Users/test/AppData/Local/Programs/Python/Python36/autotest/websocket_api_2.0'
    os.chdir(path)
    head_pic = imageio.imread('./pics/head.jpg')
    pic_name=input("请选择你需要的图标（fla、leg、iphone、mate30)")
    postion_name=input("请选择图标位置（topleft、topright、bottomleft、bottomright）")
    icon_pic = imageio.imread('./pics/icon.jpg'.format(pic_name)) # 读取图标
    # 获取头像和图标的长宽
    head_w, head_h = head_pic.shape[:2]
    icon_w, icon_h = icon_pic.shape[:2]
    # 计算图案缩放比例
    if icon_w > icon_h:
        icon_pic = imageio.imresize(icon_pic, (head_w, int(icon_w/icon_h*head_h)))
    else:
        icon_pic = imageio.imresize(icon_pic, (head_h, int(icon_h/icon_w*head_w)))
    print(icon_pic.shape)
    # 缩放图案
    icon_w, icon_h = icon_pic.shape[:2]
    icon_pic = imageio.imresize(icon_pic, (int(icon_w/ 6), int(icon_h / 6)))

    icon_w, icon_h = icon_pic.shape[:2]
    print(icon_pic.shape[:2])

    if postion_name == "topleft":
        head_pic[:icon_w+20, :icon_h+20, :] = np.ones_like(head_pic[:icon_w+20, :icon_h+20, :]) * 255
        head_pic[10:icon_w+10, 10:icon_h+10, :] = icon_pic[:, :] # 左上角
    elif postion_name == "topright":
        head_pic[:icon_w + 20, -icon_h - 20:, :] = np.ones_like(head_pic[:icon_w + 20, -icon_h - 20:, :]) * 255
        head_pic[10:icon_w + 10, -icon_h - 10:-10, :] = icon_pic[:, :] # 右上角
    elif postion_name == "bottomleft":
        head_pic[-icon_w - 20:, :icon_h + 20, :] = np.ones_like(head_pic[-icon_w - 20:, :icon_h + 20, :]) * 255
        head_pic[-icon_w - 10:-10, 10:icon_h + 10, :] = icon_pic[:, :] # 左下角

    else:
        head_pic[-icon_w-20:, -icon_h-20:, :] = np.ones_like(head_pic[-icon_w-20:, -icon_h-20:, :]) * 255
        head_pic[-icon_w-10:-10, -icon_h-10:-10, :] = icon_pic[:, :] # 右下角

    plt.imshow(head_pic)
    plt.show()

if __name__ == "__main__":
    add_icon()