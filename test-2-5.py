from base import Base
from openGLUtils import OpenGLUtils
from attribute import Attribute
from OpenGL.GL import *

# renderizar formas com cores de vértices
class Test(Base):
    def initialize(self):

        print("Inicializando programa...")

        ### inicializar o programa ###
        vsCode = """
        in vec3 position;
        in vec3 vertexColor;
        out vec3 color;
        void main()
        {
            gl_Position = vec4(position.x, position.y, position.z, 1.0);
            color = vertexColor;
        }
        """

        fsCode = """
        in vec3 color;
        out vec4 fragColor;
        void main()
        {
            fragColor = vec4(color.r, color.g, color.b, 1.0);
        }
        """
        self.programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)
        
        ### configurações de renderização (opcional) ###
        glPointSize(10)
        glLineWidth(4)
        
        ### configurar o objeto de array de vértices ###
        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef)
        
        ### configurar os atributos de vértice ###
        positionData = [[0.8, 0.0, 0.0], [0.4, 0.6, 0.0], 
                        [-0.4, 0.6, 0.0], [-0.8, 0.0, 0.0], 
                        [-0.4, -0.6, 0.0], [0.4, -0.6, 0.0]]
        self.vertexCount = len(positionData)
        positionAttribute = Attribute("vec3", positionData)
        positionAttribute.associateVariable(self.programRef, "position")
        
        colorData = [[1.0, 0.0, 0.0], [1.0, 0.5, 0.0],
                     [1.0, 1.0, 0.0], [0.0, 1.0, 0.0], 
                     [0.0, 0.0, 1.0], [0.5, 0.0, 1.0]]
        colorAttribute = Attribute("vec3", colorData)
        colorAttribute.associateVariable(self.programRef, "vertexColor")

    def update(self):
        glUseProgram(self.programRef)
        glDrawArrays(GL_POINTS, 0, self.vertexCount)

# instanciar esta classe e executar o programa
Test().run()