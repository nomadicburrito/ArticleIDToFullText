

class parseIDs:

	def __init__(self, fileName):
		self.IDList=[]
		self.fileName=fileName

	def parse(self):
		with open(self.fileName,'r') as file:
			for line in file:
				self.IDList.append(line.strip())
		return self.IDList
