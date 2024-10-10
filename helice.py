from base import Base
from openGLUtils import OpenGLUtils
from attribute import Attribute
from uniform import Uniform
from matrix import Matrix
from OpenGL.GL import *
from math import pi

# hélice controlada por teclas
class Helice(Base):
    def initialize(self):
        print("Initializing program...")
        
        # Vertex Shader e Fragment Shader
        vsCode = """
        in vec3 position;
        uniform mat4 modelMatrix;
        void main()
        {
            gl_Position = modelMatrix * vec4(position, 1.0);
        }
        """
        fsCode = """
        out vec4 fragColor;
        void main()
        {
            fragColor = vec4(1.0, 0.0, 0.0, 1.0); // cor laranja para a hélice
        }
        """
        self.programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)
        
        # Configurações de renderização
        glClearColor(1.0, 1.0, 1.0, 1.0)
        glEnable(GL_DEPTH_TEST)
        
        # Array de vértices (4 triângulos formando a hélice)
        positionData = [
            [0.0, 0.7, 0.0], [0.2, 0.0, 0.0], [-0.2, 0.0, 0.0],  # 1ª ponta
            [0.0, -0.7, 0.0], [0.2, 0.0, 0.0], [-0.2, 0.0, 0.0], # 2ª ponta
            [0.7, 0.0, 0.0], [0.0, 0.2, 0.0], [0.0, -0.2, 0.0], # 3ª ponta
            [-0.7, 0.0, 0.0], [0.0, 0.2, 0.0], [0.0, -0.2, 0.0]  # 4ª ponta
        ]
        self.vertexCount = len(positionData)
        positionAttribute = Attribute("vec3", positionData)
        positionAttribute.associateVariable(self.programRef, "position")
        
        # Matriz do modelo
        self.modelMatrix = Uniform("mat4", Matrix.makeIdentity())
        self.modelMatrix.locateVariable(self.programRef, "modelMatrix")
        
        # Velocidade de rotação e estado de rotação
        self.rotationSpeed = 0.0  # inicializa com rotação parada
        
    def update(self):
        # Atualiza a rotação da hélice
        rotationAmount = self.rotationSpeed * self.deltaTime
        
        if self.input.isKeyPressed("j"):
            self.rotationSpeed = 2.0  # rotação anti-horária
        if self.input.isKeyPressed("l"):
            self.rotationSpeed = -2.0  # rotação horária
        if self.input.isKeyPressed("k"):
            self.rotationSpeed = 0.0  # parar rotação
        
        # Aplica a rotação
        m = Matrix.makeRotationZ(rotationAmount)
        self.modelMatrix.data = self.modelMatrix.data @ m
        
        # Renderiza a hélice
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.programRef)
        self.modelMatrix.uploadData()
        glDrawArrays(GL_TRIANGLES, 0, self.vertexCount)

# Instancia a classe e roda o programa
Helice().run()
