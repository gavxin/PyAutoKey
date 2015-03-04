# -*- coding: utf-8 -*-
"using winio lib. simulate keyboard input."
from ctypes import *
import time
user32 = windll.LoadLibrary("user32.dll")
winio = windll.LoadLibrary("WinIo32.dll")

def winio_initialize():
    bret = winio.InitializeWinIo()
    if bret == 0:
        print "fail to initialize WinIO"
        return False
    else:
        print "Success to initialize WinIO"
        return True

# define some functions
KBC_CMD = 0x64
KBC_DATA = 0x60
def KBCWait4IBE():
    dwVal = c_int()
    while True:
        winio.GetPortVal(KBC_CMD, byref(dwVal), 1)
        if dwVal.value & 0x2 == 0:
            break
    
def _key_down(vk_in):
    scancode = user32.MapVirtualKeyW(vk_in, 0);
    KBCWait4IBE()
    winio.SetPortVal(KBC_CMD, 0xD2, 1)
    #KBCWait4IBE()
    #winio.SetPortVal(KBC_DATA, 0xE2, 1)
    #KBCWait4IBE()
    #winio.SetPortVal(KBC_CMD, 0xD2, 1)
    KBCWait4IBE()
    winio.SetPortVal(KBC_DATA, scancode, 1)
    
def _key_up(vk_in):
    scancode = user32.MapVirtualKeyW(vk_in, 0);
    KBCWait4IBE()
    winio.SetPortVal(KBC_CMD, 0xD2, 1)
    #KBCWait4IBE()
    #winio.SetPortVal(KBC_DATA, 0xE0, 1)
    #KBCWait4IBE()
    #winio.SetPortVal(KBC_CMD, 0xD2, 1)
    KBCWait4IBE()
    winio.SetPortVal(KBC_DATA, scancode|0x80, 1)

def press_key(vitual_key_code):
    _key_down(vitual_key_code)
    time.sleep(0.1)
    _key_up(vitual_key_code)
    time.sleep(0.1)

def main():
    if winio_initialize() == False:
        print "winio initialize fail"
        return
    user32 = windll.LoadLibrary("user32.dll")
    hwnd = user32.FindWindowW(0, u"无标题 - 记事本")
    user32.SetForegroundWindow(hwnd)
    time.sleep(2)

    while True:
        print "press key 1"
        press_key(49)
        time.sleep(1)

if __name__ == "__main__":
    main()
