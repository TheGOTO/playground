Set WShShell = WScript.CreateObject("WScript.Shell")
WShShell.Run "cmd /c python volume_default.py  > volume_default.log", 0
WShShell.Run "cmd /c nircmdc.exe speak  text  ""volume default""", 0





