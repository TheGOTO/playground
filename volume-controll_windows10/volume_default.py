from subprocess import Popen, PIPE
import csv


process = Popen(["SoundVolumeView.exe", " /scomma", ""], stdout=PIPE)
(output, err) = process.communicate()

print (output)

#print output.find(",")

#output="sere,ich"

lines = output.splitlines()

spamreader = csv.reader(lines,delimiter=",")
for row in spamreader:

	pid=row[18]
	name=row[0]
	if pid is not "" and name is not "":
		print row[0]+":"+row[18] 