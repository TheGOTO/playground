from subprocess import Popen, PIPE
import csv,sys


process = Popen(["SoundVolumeView.exe", " /scomma", ""], stdout=PIPE)
(output, err) = process.communicate()


if sys.version[0] != '2':
	output=output.decode("windows-1252")#set encoding for python3

lines = output.splitlines()

spamreader = csv.reader(lines,delimiter=",")
for row in spamreader:

	pid=row[18]
	name=row[0]
	if pid is not "" and name is not "":
		print (pid+":"+name)
		
		Popen(["nircmdc.exe", "setappvolume", "/"+str(pid),"0.5"], stdout=PIPE)
		
		
		