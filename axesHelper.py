from mesh import Mesh
from geometry import Geometry
from lineMaterial import LineMaterial

class AxesHelper(Mesh):
    def __init__(self,
                 axisLength = 1,
                 lineWidth = 4,
                 axisColor = [[1, 0, 0], 
                              [0, 1, 0], 
                              [0, 0, 1]]):
        
        geo = Geometry()

        positionData = [[0, 0, 0], [axisLength, 0, 0],
                        [0, 0, 0], [0, axisLength, 0],
                        [0, 0, 0], [0, 0, axisLength]]
        
        colorData = [axisColor[0], axisColor[0],
                     axisColor[1], axisColor[1],
                     axisColor[2], axisColor[2]]
        
        geo.addAttribute("vec3", "vertexPosition", positionData)
        geo.addAttribute("vec3", "vertexColor", colorData)
        geo.countVertices()

        mat = LineMaterial({
            "useVertexColors": True,
            "lineWidth": lineWidth,
            "lineType": "segments"
        })

        # initialize the mesh
        super().__init__(geo, mat)