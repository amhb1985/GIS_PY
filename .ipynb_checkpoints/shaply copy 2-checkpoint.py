

import pygeos
polygon = pygeos.box(0, 0, 2, 2)
points = pygeos.points(...)
pygeos.contains(polygon, points)

