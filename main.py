import sys, requests
from requestSciDir import requestSciDir
from parseIDs import parseIDs

IDFile=sys.argv[1]

parser=parseIDs(IDFile)
PMIDList=parser.parse()

for x in PMIDList:
	print x
	sciDir=requestSciDir(sys.argv[2], x)

	sciDir.request() #Request the article from science direct

	if sciDir.r.status_code == requests.codes.ok:	#only write to file if our request is handled well
		sciDir.write()

	print sciDir.r.status_code
