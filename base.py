import pygame
import sys
from input import Input

class Base(object):

    def __init__(self, screenSize=[512, 512]):
        # inicializar todos os módulos do pygame
        pygame.init()

        # indicar detalhes de renderização
        displayFlags = pygame.DOUBLEBUF | pygame.OPENGL
        
        # inicializar buffers para realizar antialiasing
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 4)
        
        # usar um perfil OpenGL core para compatibilidade entre plataformas
        pygame.display.gl_set_attribute(
        pygame.GL_CONTEXT_PROFILE_MASK,
        pygame.GL_CONTEXT_PROFILE_CORE)
        
        # criar e exibir a janela
        self.screen = pygame.display.set_mode(screenSize, displayFlags)
        
        # definir o texto que aparece na barra de título da janela
        pygame.display.set_caption("Janela Gráfica")
        
        # determinar se o loop principal está ativo
        self.running = True
        
        # gerenciar dados e operações relacionados ao tempo
        self.clock = pygame.time.Clock()
        
        # gerenciar a entrada do usuário
        self.input = Input()

        # number of seconds application has been running
        self.time = 0
    
    # implementar estendendo a classe
    def initialize(self):
        pass

    # implementar estendendo a classe
    def update(self):
        pass
    
    def run(self):
        ## inicialização ##
        self.initialize()
    
        ## loop principal ##
        while self.running:
            ## processar entrada ##
            self.input.update()
            if self.input.quit:
                self.running = False

            # seconds since iteration of run loop
            self.deltaTime = self.clock.get_time() / 1000

            # increment time application has been running
            self.time += self.deltaTime# seconds since iteration of run loop
            self.deltaTime = self.clock.get_time() / 1000

            # increment time application has been running
            self.time += self.deltaTime
            
            ## atualizar ##
            self.update()

            ## renderizar ##
            # exibir imagem na tela
            pygame.display.flip()
            
            # pausar, se necessário, para alcançar 60 FPS
            self.clock.tick(60)
            
        ## finalização ##
        pygame.quit()
        sys.exit()
