import os
from subprocess import call

python = 'C:\\Python27\\python.exe'
codeCov = '..\\2.Coverage\\Coverage.py' 
inputDir = ".\\"
exePath = "pathToExe\\notepad.exe"

for root, subFolder, files in os.walk(inputDir):
	for item in files:
		fname = os.path.join(inputDir, root, item)     
        print "Coverage... '%s'" % fname
        call([python, codeCov, exePath, fname])
