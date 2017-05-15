import sqlite3
import pprint
import csv

contactlist = []

conn = sqlite3.connect('contacts.sqlite')
cur = conn.cursor()

#cur.execute('''DROP TABLE IF EXISTS Contacts ''')
#cur.execute('''CREATE TABLE Contacts (name TEXT, email TEXT, phnumber INTEGER)''')

fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'contactsascsv.csv'

fh = open(fname)

#for index, line in enumerate(fh):
#	#print index, line
#	linepiece = line.split(',')
#	if index == 0:  #getting names of headers to be used for db indices
#		print linepiece
#		pprint.pprint(linepiece)
#		headernames = linepiece

csvfh =csv.DictReader(fh)
for index, line in enumerate(csvfh):
	contactlist.append(line)
	#print index
	print(type(contactlist[index]['First Name']),type(contactlist[index]['Last Name']))
	#print(contactlist[index][])		

pprint.pprint(type(contactlist[index].keys()))
#print(contactlist[index]['First Name'])
#pprint.pprint(contactlist)




#conn.close()




