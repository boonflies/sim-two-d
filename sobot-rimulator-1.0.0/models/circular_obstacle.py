# Sobot Rimulator - A Robot Programming Tool
# Copyright (C) 2013-2014 Nicholas S. D. McCrea
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Email mccrea.engineering@gmail.com for questions, comments, or to report bugs.





from math import *
from polygon import *
from pose import *

class CircularObstacle:

  def __init__( self, radius, x, y, pose ):
    self.pose = pose
    self.x = x
    self.y = y
    self.radius = radius/2

    # define the geometry
    vertexes = []
    x_ver = []
    y_ver = []
    for degree in range(0, 360, 10):
        x = self.x + (self.radius * cos(degree * (3.14/180)) )
        y = self.y + (self.radius * sin(degree * (3.14/180)) )
        x_ver.append(x)
        y_ver.append(y)
        points = [x_ver[-1], y_ver[-1]]
        vertexes.append(points)

    self.geometry = Polygon( vertexes )
    self.global_geometry = Polygon( vertexes )
