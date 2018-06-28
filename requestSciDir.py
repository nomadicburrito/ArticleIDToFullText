import requests

class requestSciDir:

	def __init__(self, token, pmid):
		self.token=token	#APIKey for science direct
		self.pmid=pmid
		self.headers={'Accept':'text/xml', 'X-ELS-APIKEY':self.token}	#Ask for XML and provide api key
		self.payload={'view':'FULL'}	#Ask for all article information, including full article text

	def request(self):	#perform html request
		self.r = requests.get('https://api.elsevier.com/content/article/pubmed_id/'+self.pmid, params=self.payload, headers=self.headers)

	def write(self):
		with open(self.pmid+'.xml', 'w+') as file:
			file.write(self.r.text.encode('utf-8'))
