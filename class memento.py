class Memento:

	def __init__(self, file, content):
		self.file = file     
		self.content = content       
class X:
	def __init__(self, file_path):

		self.file = file_path
		self.content = ""
	def write(self, string):
		self.content += string
	def save(self):
		return Memento(self.file, self.content)
	def undo(self, memento):
		self.file = memento.file
		self.content = memento.content
class Y:
	def save(self, x):
		self.mem = x.save()
	def undo(self, x):
		x.undo(self.mem)
if __name__ == '__main__':
	y = Y()
	x = X("GFG.txt")   
	x.write("First vision of Data\n")   
	print(x.content + "\n\n")
	y.save(x) 
	x.write("Second vision of Data\n")  

	print(x.content + "\n\n")
	
	y.undo(x)

	print(x.content + "\n\n")  
