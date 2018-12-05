Set WShShell = WScript.CreateObject("WScript.Shell")
WShShell.Run "cmd /c nircmdc.exe changeappvolume focused -0.1  > volume_down.log", 0
WShShell.Run "cmd /c nircmdc.exe speak  text  ""volume down""", 0







