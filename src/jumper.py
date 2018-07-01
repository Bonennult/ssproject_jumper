import os
# from PIL import Image
#import matplotlib
#import matplotlib.pyplot as plt
import numpy as np
from skimage import io, transform, data, color, feature, filters
#import cv2 as cv

time_coeff = 1.200 #1.392

def get_screenshot():
    # Change 'platform-tools-windows' to 'platform-tools-macos' and 'adb.exe' to './adb' on macOS; you may need to use `chmod +X ../dependency/platform-tools-macos/adb` first
    os.system(
        'cd ../dependency/platform-tools-windows/ && adb.exe shell screencap -p /sdcard/autojump.png')
    os.system(
        'cd ../dependency/platform-tools-windows/ && adb.exe pull /sdcard/autojump.png ../../src/')


def press_screen(distance):
    # Change 'platform-tools-windows' to 'platform-tools-macos' and 'adb.exe' to './adb' on macOS; you may need to use `chmod +X ../dependency/platform-tools-macos/adb` first
    press_time = int(distance * time_coeff)
    os.system('cd ../dependency/platform-tools-windows/ && adb.exe shell input swipe 500 1000 500 1002 ' + str(press_time))


def edge_detc(img_gray):
    #img = np.mat(img_gray)
    #temp = img[:,:-1] - img[:,1:]
    #print(temp)
    #io.imshow(temp, cmap='gray')
    '''
    for i in range(img_gray.shape[0]):
        for j in range(1,img_gray.shape[1]):
            #if temp[i,j] != 0 :
            #    temp[i,j] = True
            #else :
            #    temp[i,j] = False
            if img_gray[i,j] != img_gray[i,j-1] | img_gray[i,j] != img_gray[i,j+1] :
                temp[i,j] = True
            else :
                temp[i,j] = False
        temp[i,0] = temp[i,-1] = False
    '''
    temp = abs(img_gray[:,:-1] - img_gray[:,1:])
    temp = temp > 0.001
    return temp


if __name__ == '__main__':
    main()


jer = io.imread('jer0.png')                        # 读取棋子模板图像
jer_gray = color.rgb2gray(jer)                    # 转化为灰度图
jer_gray = 1 - jer_gray                           # 进行灰度反转
mat1 = np.mat(jer_gray)
#print(mat1)
for i in range(mat1.shape[0]) :
    for j in range(mat1.shape[1]) :
        if mat1[i,j] < 0.3 :
            mat1[i,j] = 0;
io.imshow(mat1,cmap='gray')
np.savetxt('jer.csv',mat1,delimiter=',')

