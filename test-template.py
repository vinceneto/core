from base import Base
from renderer import Renderer
from scene import Scene
from camera import Camera
from mesh import Mesh
from boxGeometry import BoxGeometry
from surfaceMaterial import SurfaceMaterial

# render a basic scene
class Test(Base):
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera( aspectRatio=800/600 )
        self.camera.setPosition( [0, 0, 0.5] )
        geometry = BoxGeometry()
        material = SurfaceMaterial({
            "useVertexColors": True,
            # "wireframe": True,
            # "lineWidth": 8
            })
        
        self.mesh = Mesh( geometry, material )
        self.scene.add( self.mesh )
    
    def update(self):
        self.renderer.render( self.scene, self.camera)

# instantiate this class and run the program
Test( screenSize=[800,600] ).run()