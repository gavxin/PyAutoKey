# -*- coding: utf-8 -*-
"get color"
from ctypes import *
    
user32 = windll.LoadLibrary("user32.dll")
gdi32 = windll.LoadLibrary("gdi32.dll")

hwnd = 0

def get_hdc(window_name):
    global hwnd
    hwnd = user32.FindWindowW(0, window_name)
    if hwnd == 0:
        print "window not found!"
    return user32.GetDC(hwnd)

def get_color(hdc, x, y):
    return gdi32.GetPixel(hdc, 0, 0)

def release_hdc(hdc):
    global hwnd
    user32.ReleaseDC(hwnd, hdc)
    #user32.CloseHandle(hwnd)

def main():
    window_name=u"[MMT]洛奇5星料理工具V1.75 For R83"
    hdc = get_hdc(window_name)
    color = get_color(hdc, 0, 0,)
    print "%06x" % color
    release_hdc(hdc)

if __name__ == "__main__":
   main()
