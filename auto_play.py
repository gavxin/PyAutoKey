# -*- coding: utf-8 -*-
"""auto playing instrument for mabinogi
author:Falcon"""
from ctypes import *
from key_input import winio_initialize, press_key
from get_color import *
import time
import logging

mabinogi = u"洛奇"
mmt_helper = u"[MMT]洛奇5星料理工具V1.75 For R83"

user32 = windll.LoadLibrary("user32.dll")

logger = logging.getLogger("auto_play")
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(message)s")

handler.setFormatter(formatter)

logger.addHandler(handler)

def main():
    if winio_initialize() == False:
        logger.error("Can't initialize winio")
        return
    else:
        logger.info("Success to initialize winio")

    #get mabinogi window
    hwnd = user32.FindWindowW(0, mabinogi)
    if hwnd == 0:
        logger.error("Can't find mabinogi window")
        return

    #get helper hdc
    hdc = get_hdc(mmt_helper)
    if hdc == 0:
        logger.error("Can't get the DC of mmt helper")
        return

    #set mabinogi window front
    user32.SetForegroundWindow(hwnd)
    time.sleep(2)

    logger.info("start playing")
    try:
        while True:
            hwnd2 = user32.GetForegroundWindow()
            if hwnd != hwnd2:
                user32.SetForegroundWindow(hwnd)

            #press key 1 to playing
            logger.info("press key 1")
            press_key(ord('1'))
            time.sleep(1)

            #get color
            color = get_color(hdc, 0, 0,)
            if color == 0xF0F0F0:
                #playing will fail. press ESC to cancel skill
                logger.info("color not right. press ESC")
                press_key(0x1B)
                time.sleep(1)
            else:
                #playing will success. wait for ending.
                logger.info("color right. wait 5 seconds")
                time.sleep(5)
    except KeyboardInterrupt:
        print "program stoped!"
        return
    except Exception, e:
        print e
        release_hdc(hdc)
        return

if __name__ == "__main__":
    main()





