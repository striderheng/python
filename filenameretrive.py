import os
import pprint
import re
import win32api

mypathraw = raw_input("Enter directory:")
if ( len(mypathraw) < 1 ) : mypath = r'g:\working'
else : mypath = mypathraw

#pprint.pprint(os.listdir(mypath))
#print mypath

for dirname, dirnames, filenames in os.walk(mypath):
	print "DIRNAME: "
	print dirname
	print "DIRNAMES: " 
	print dirnames
	print "FILENAMES: "
	#pprint.pprint(filenames)
	for fname in filenames:
		#fnameshort = win32api.GetShortPathName(fname)
		fname2 = os.path.join(dirname, fname)
		#print fname2
		fnameshort = win32api.GetShortPathName(fname2)
		print fname2		
		newfname = re.findall('.*Ong - (.*)', fname)
		#newfname[0] = 'Brendel - ' + newfname[0]
		print newfname[0]
		newfname2 = os.path.join(dirname, newfname[0])
		#newfname2short = win32api.GetShortPathName(newfname2)
		if os.path.isfile(fnameshort):
			print "OK OK OK OK OK"
			os.rename(fnameshort, newfname2)


