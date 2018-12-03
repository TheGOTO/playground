@echo off


for /f "tokens=2" %%a in ('tasklist^|find /i "mumble"') do (set pid=%%a)
REM echo "%PID%"

nircmd.exe changeappvolume /%PID% 0.1


nircmd.exe speak text "volume up"