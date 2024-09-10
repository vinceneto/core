from base import Base
from openGLUtils import OpenGLUtils
from attribute import Attribute
from uniform import Uniform
from math import sin, cos, pi
from OpenGL.GL import *

class Car2D(Base):

    def initialize(self):
        print("Initializing program...")
        
        ### initialize program ###
        vsCode = """
        in vec3 position;
        void main()
        {
            gl_Position = vec4(position, 1.0);
        }
        """

        fsCode = """
        uniform vec3 baseColor;
        out vec4 fragColor;
        void main()
        {
            fragColor = vec4(baseColor.r, baseColor.g, baseColor.b, 1.0);
        }
        """

        self.programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)
        glClearColor(0.0, 0.0, 0.0, 1.0)
        
        self.baseColor = Uniform("vec3", [1.0, 0.0, 0.0])  # Initial color
        self.baseColor.locateVariable(self.programRef, "baseColor")

        # Initialize car parts
        self.pentagonVAO, self.pentagonVertexCount = self.createPentagon()
        self.wheel1VAO, self.wheelVertexCount = self.createCircle(0.1, 30, 0.2, 0.0)  # Left wheel
        self.wheel2VAO, _ = self.createCircle(0.1, 30, 0.6, 0.0)  # Right wheel
    
    def createPentagon(self):
        # Set up vertex array object for a pentagon or similar car body shape
        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef)
        
        # Pentagon vertex data (positioned at the top, resembling a car body)
        positionData = [
            [0.0, 0.4, 0.0], [0.6, 0.4, 0.0],
            [0.8, 0.2, 0.0], [0.8, 0.0, 0.0],
            [0.0, 0.0, 0.0]
        ]
        vertexCount = len(positionData)
        positionAttribute = Attribute("vec3", positionData)
        positionAttribute.associateVariable(self.programRef, "position")
        
        return vaoRef, vertexCount

    def createCircle(self, radius, segments, offsetX, offsetY):
        # Set up vertex array object for the circle (wheel)
        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef)
        
        # Generate the circle's vertex positions with offset
        positionData = []
        for i in range(segments):
            angle = 2 * pi * i / segments
            x = radius * cos(angle) + offsetX
            y = radius * sin(angle) + offsetY
            positionData.append([x, y, 0.0])

        vertexCount = len(positionData)
        positionAttribute = Attribute("vec3", positionData)
        positionAttribute.associateVariable(self.programRef, "position")
        
        return vaoRef, vertexCount
    
    def update(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glUseProgram(self.programRef)

        # Draw the car body (pentagon-like shape)
        self.baseColor.data = [0.0, 0.0, 1.0]  # Blue for the car body
        self.baseColor.uploadData()
        glBindVertexArray(self.pentagonVAO)
        glDrawArrays(GL_TRIANGLE_FAN, 0, self.pentagonVertexCount)

        # Draw the first wheel (left)
        self.baseColor.data = [0.0, 1.0, 0.0]  # Green color for the wheels
        self.baseColor.uploadData()
        glBindVertexArray(self.wheel1VAO)
        glDrawArrays(GL_TRIANGLE_FAN, 0, self.wheelVertexCount)

        # Draw the second wheel (right)
        glBindVertexArray(self.wheel2VAO)
        glDrawArrays(GL_TRIANGLE_FAN, 0, self.wheelVertexCount)

# instantiate this class and run the program
Car2D().run()
