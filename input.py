import pygame

class Input(object):
	def __init__(self):
		# o usuário encerrou a aplicação?
		self.quit = False
	
	def update(self):
		# iterar sobre todos os eventos de entrada do usuário (como
		# teclado ou mouse) que ocorreram desde a última verificação de eventos
		for event in pygame.event.get():
			# evento de encerramento ocorre ao clicar no botão para fechar a janela
			if event.type == pygame.QUIT:
				self.quit = True
