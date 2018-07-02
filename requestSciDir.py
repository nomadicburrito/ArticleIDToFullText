import requests

class requestSciDir:

	def __init__(self, token, id):
		self.token=token	#APIKey for science direct
		self.id=id
		self.headers={'Accept':'text/xml', 'X-ELS-APIKEY':self.token}	#Ask for XML and provide api key
		self.payload={'view':'FULL'}	#Ask for all article information, including full article text

	def requestPMID(self):	#perform html request
		self.r = requests.get('https://api.elsevier.com/content/article/pubmed_id/'+self.id, params=self.payload, headers=self.headers)

	def requestDOI(self):
		self.r = requests.get('https://api.elsevier.com/content/article/doi/'+self.id, params=self.payload, headers=self.headers)


	def write(self):
		with open(self.id.replace('/', '_')+'.xml', 'w+') as file:
			file.write(self.r.content)
