from base import Base

class Test(Base):
	
	def initialize(self):
		print("Inicializando programa...")
	
	def update(self):
		pass

# instanciar esta classe e executar o programa
Test().run()
