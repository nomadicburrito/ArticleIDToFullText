import sys, requests, time
from collections import deque
from requestSciDir import requestSciDir
from parseIDs import parseIDs
from requestSpringer import requestSpringer

IDFile=sys.argv[1]

parser=parseIDs(IDFile)
IDList=parser.parse()

idType=sys.argv[2].lower()

def makeRequest():
	sciDir=requestSciDir(sys.argv[3], x)
	print x
	sciDir.requestDOI() #Request the article from science direct
	print 'SciDir status: '+str(sciDir.r.status_code)
	if sciDir.r.status_code == requests.codes.ok:   #only write to file if our request is handled well
		sciDir.write()
	elif sciDir.r.status_code !=requests.codes.ok:
		spring=requestSpringer(x)
		spring.request()
		print 'Springer Status: '+str(spring.r.status_code)
		if spring.r.status_code == requests.codes.ok:
			spring.write()

if idType=='pmid':
	for x in IDList:
		print x
		sciDir=requestSciDir(sys.argv[3], x)

		sciDir.requestPMID() #Request the article from science direct

		if sciDir.r.status_code == requests.codes.ok:	#only write to file if our request is handled well
			sciDir.write()

		print sciDir.r.status_code

elif idType=='doi':
	
	queue = deque(maxlen=5)	#springer has a rate limit, so it will be implemented for all requests
	timer=time.time()
	for x in IDList:
		if not queue:
			queue.append(time.time())
			makeRequest()
		elif len(queue)==queue.maxlen:
			while((time.time()-queue[0])<1):
				time.sleep(1-(time.time()-queue[0]))
			queue.popleft()
			queue.append(time.time())
			makeRequest()
		else:
			while((time.time()-queue[0])<1):
				time.sleep(1-(time.time()-queue[0]))
			queue.append(time.time())
			makeRequest()
	print 'Runtime: '+str(time.time()-timer)

else:
	print "Please enter a valid ID Type"
