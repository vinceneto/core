from base import Base
from openGLUtils import OpenGLUtils
from attribute import Attribute
from uniform import Uniform
from math import sin, cos
from OpenGL.GL import *

# animate triangle moving across screen
class Test(Base):

    def initialize(self):
        print("Initializing program...")
        
        ### initialize program ###
        vsCode = """
        in vec3 position;
        uniform vec3 translation;
        void main()
        {
            vec3 pos = position + translation;
            gl_Position = vec4(pos.x, pos.y, pos.z, 1.0);
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
        ### render settings (optional) ###
        # specify color used when clearly
        glClearColor(0.0, 0.0, 0.0, 1.0)
        
        ### set up vertex array object ###
        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef)
        
        ## set up vertex attribute ###
        positionData = [[0.0, 0.2, 0.0], [0.2, -0.2, 0.0], [-0.2, -0.2, 0.0] ]
        self.vertexCount = len(positionData)
        positionAttribute = Attribute("vec3", positionData)
        positionAttribute.associateVariable(self.programRef, "position" )
        
        ### set up uniforms ###
        self.translation = Uniform("vec3", [-0.5, 0.0, 0.0])
        self.translation.locateVariable(self.programRef, "translation" )
        self.baseColor = Uniform("vec3", [1.0, 0.0, 0.0])
        self.baseColor.locateVariable( self.programRef, "baseColor" )
    
    def update(self):
        ### update data ###
        # self.baseColor.data[0] = (sin(3 * (self.time)) + 1) / 2
        self.baseColor.data[0] = (sin(self.time) + 1) / 2
        self.baseColor.data[1] = (sin(self.time + 2.1) + 1) / 2
        self.baseColor.data[2] = (sin(self.time + 4.2) + 1) / 2

        ### render scene ###
        # reset color buffer with specified color
        glClear(GL_COLOR_BUFFER_BIT)
        glUseProgram( self.programRef )
        self.translation.uploadData()
        self.baseColor.uploadData()
        glDrawArrays( GL_TRIANGLE_STRIP , 0 , self.vertexCount )

# instantiate this class and run the program
Test().run()