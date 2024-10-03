from base import Base
from openGLUtils import OpenGLUtils
from OpenGL.GL import *

# renderizar um único ponto
class Test(Base):

    def initialize(self):
        print("Inicializando o programa...")
        
        ### inicializar o programa ###

        # código do vertex shader
        vsCode = """
        void main()
        {
            gl_Position = vec4(0.3, 0.5, 0.0, 1.0);
        }
        """

        # código do fragment shader
        fsCode = """
        out vec4 fragColor;
        void main()
        {
            fragColor = vec4(1.0, 1.0, 0.0, 1.0);
        }
        """
        # enviar o código para a GPU e compilar; armazenar a referência do programa
        self.programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)
        
        # configurar o objeto de array de vértices
        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef)
        
        ### configurações de renderização (opcional)
        
        # definir a largura e altura do ponto
        glPointSize(10)
    
    def update(self):
        # selecionar o programa a ser usado na renderização
        glUseProgram(self.programRef)

        # renderiza objetos geométricos usando o programa selecionado
        glDrawArrays(GL_POINTS, 0, 1)
        
# instanciar esta classe e executar o programa
Test().run()
