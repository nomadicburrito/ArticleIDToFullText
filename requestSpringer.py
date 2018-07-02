import requests

class requestSpringer:

	def __init__(self, doi):
		self.DOI=doi

	def request(self):	#perform html request
		self.r = requests.get('https://link.springer.com/'+self.DOI+'.pdf')

	def write(self):
		with open(self.DOI.replace('/', '_')+'.pdf', 'w+') as file:
			file.write(self.r.content)
