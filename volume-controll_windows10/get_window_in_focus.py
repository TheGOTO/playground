import win32api, win32gui, win32process, psutil, time
from subprocess import call


curtid = win32api.GetCurrentThreadId()
whd = win32gui.GetForegroundWindow()
(tid, pid) = win32process.GetWindowThreadProcessId(whd)

#print (tid)
#print (pid)

print(psutil.Process(pid).name())
	
call(["nircmd.exe", "changeappvolume","/"+str(pid),"0.1"])

call(["nircmd.exe", "speak","text","volume up"])


