from base import Base
from renderer import Renderer
from scene import Scene
from camera import Camera
from mesh import Mesh
from axesHelper import AxesHelper
from gridHelper import GridHelper
from movementRig import MovementRig
from math import pi

# render a basic scene
class Test(Base):
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera( aspectRatio=800/600 )
        self.rig = MovementRig()
        self.rig.add( self.camera )
        self.rig.setPosition( [0.5, 1, 5] )
        self.scene.add( self.rig )

        axes = AxesHelper(axisLength=1)
        self.scene.add(axes)

        grid = GridHelper(size=20, 
                          gridColor=[1, 1, 1], 
                          centerColor=[1, 1, 0])
        grid.rotateX(-pi / 2)
        self.scene.add(grid)
    
    def update(self):
        self.rig.update( self.input, self.deltaTime )
        
        self.renderer.render( self.scene, self.camera)

# instantiate this class and run the program
Test( screenSize=[800,600] ).run()