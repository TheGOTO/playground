Set WShShell = WScript.CreateObject("WScript.Shell")
WShShell.Run "cmd /c nircmdc.exe changeappvolume focused 0.1  > volume_up.log", 0
WShShell.Run "cmd /c nircmdc.exe speak  text  ""volume up""", 0







