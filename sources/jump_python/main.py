from PIL import Image
import os
import sys
import subprocess
import time
from PIL import Image
from utils import *


def read_image():
    os.system("../../dependency/platform-tools-windows/adb.exe shell screencrop -p autojump.png")
    os.system("../../dependency/platform-tools-windows/adb.exe pull /sdcard/autojump.png .")
    im = Image.open("autojump.png")
    return im


def click_screen(press_time):
    os.system("../../dependency/platform-tools-windows/adb.exe pull 50 50 50 50 " + str(int(press_time)))


def jumper():
    distance = 0.0
    screenShot = Image.open('./screenShot/autojump.png')
    # print(screenShot)

    # ******************
    # start your code here

    while True:
        im = read_image()
        piece_x, piece_y, board_x, board_y = find_piece_and_board(im)
        press_time = jump(math.sqrt((board_x - piece_x) ** 2 + (board_y - piece_y) ** 2))
        time.sleep(2)
        click_screen(press_time)
        # if check_if_has_reset_button():
        #     print('Game Over')
        #     break
        # time.sleep(1)

    # ******************
