from base import Base

class Test(Base):
	
	def initialize(self):
		print("Inicializando programa...")
	
	def update(self):
		pass

# instantiate this class and run the program
Test().run()