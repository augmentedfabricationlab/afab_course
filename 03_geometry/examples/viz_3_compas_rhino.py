from random import random
from compas.geometry import pointcloud_xy
from compas.utilities import i_to_green
from compas.utilities import i_to_red
import compas_rhino

cloud = pointcloud_xy(200, (0, 10), (0, 5))

points = []
circles = []
for xyz in cloud:
    n = random()
    points.append({'pos': xyz, 'color': i_to_red(n)})
    circles.append({'plane': [xyz, [0,0,1]], 'color': i_to_red(n), 'radius':n})

layerp = "points"
layerc = "circles"

compas_rhino.draw_points(points, layer=layerp, clear=True)
compas_rhino.draw_circles(circles, layer=layerp, clear=False)