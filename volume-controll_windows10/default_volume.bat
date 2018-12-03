@echo off


for /f "tokens=2" %%a in ('tasklist^|find /i "mumble"') do (set mumble_pid=%%a)
for /f "tokens=2" %%a in ('tasklist^|find /i "Heroes"') do (set hots_pid=%%a)
REM echo "%hots_pid%"

nircmd.exe setappvolume /%mumble_pid% 0.5
nircmd.exe setappvolume /%hots_pid% 0.5

nircmd.exe speak text "volume default"