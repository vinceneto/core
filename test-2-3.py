from base import Base
from openGLUtils import OpenGLUtils
from attribute import Attribute
from OpenGL.GL import *

# render six points in a hexagon arrangement
class Test(Base):

    def initialize(self):

        print("Initializing program...")
        
        ### initialize program ###

        # código do vertex shader
        vsCode = """
        in vec3 position;
        void main()
        {
            gl_Position = vec4(position.x, position.y, position.z, 1.0);
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
        
        # render settings (optional)
        glLineWidth( 4 )
        
        # configurar o objeto de array de vértices
        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef)

        # set up vertex attribute
        positionData = [[ 0.8, 0.0, 0.0], [ 0.4, 0.6, 0.0],
                        [-0.4, 0.6, 0.0], [-0.8, 0.0, 0.0],
                        [-0.4, -0.6, 0.0], [0.4, -0.6, 0.0]]
        
        self.vertexCount = len(positionData)
        positionAttribute = Attribute("vec3", positionData)
        positionAttribute.associateVariable(self.programRef, "position")
    
    def update(self):
        # selecionar o programa a ser usado na renderização
        glUseProgram( self.programRef )

        # renderiza objetos geométricos usando o programa selecionado
        glDrawArrays( GL_TRIANGLE_FAN , 0 , self.vertexCount )

# instanciar esta classe e executar o programa
Test().run()