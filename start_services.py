# -*- coding: UTF-8 -*-
from ctypes import *
import time
#user32 = windll.LoadLibrary("user32.dll")
Advapi32 = windll.LoadLibrary("Advapi32.dll")

SC_MANAGER_ALL_ACCESS = 0xF003F
hSCManager = Advapi32.OpenSCManagerW(0, 0, SC_MANAGER_ALL_ACCESS)
print "hSCManager", hSCManager

SERVICE_ALL_ACCESS = 0xF01FF

hService = Advapi32.OpenServiceW(hSCManager, c_wchar_p("WINIO"), SERVICE_ALL_ACCESS);
print "hService", hService

bret = Advapi32.StartServiceW(hService, 0, 0)
print "StartServiceW", bret

ERROR_SERVICE_ALREADY_RUNNING = 1056
if bret == 0:
    error = windll.kernel32.GetLastError()
    if error == ERROR_SERVICE_ALREADY_RUNNING:
        print "already running!"
    else:
        print "error:", error


Advapi32.CloseServiceHandle(hSCManager)
Advapi32.CloseServiceHandle(hService)