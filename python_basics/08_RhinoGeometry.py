#import for using rhinoscriptsyntax
import rhinoscriptsyntax as rs
#imports for using Rhino.Geometry
import scriptcontext
import Rhino.Geometry as rg
import Rhino.Input.RhinoGet as get

###################### rhinoscriptsyntax ################
#ptA = rs.AddPoint(0, 0, 0)
#ptA = rs.AddPoint(0, 0, 0)
#ptB = rs.AddPoint(10, 10, 10)
#
#lineA = rs.AddLine(ptA, ptB)
#circle = rs.AddCircle(ptA, 8)
#
#grid of points
#for i in range(10):
#    for j in range(10):
#        x_coord = i
#        y_coord = j
#        rs.AddPoint(x_coord, y_coord, 0)
#        rs.Sleep(500)
#
##find rule to connect points diagonally
#
##deform grid of points


########### import objects from Rhino ####################
#ptC = rs.GetObject("pick point", 0)
#print type(ptC)
#print rs.PointCoordinates(ptC)


####################### rhinocommon ####################### 

#ptA = rg.Point3d(0, 0, 0)
#ptB = rg.Point3d(10, 10, 10)
#
#lineA = rg.Line(ptA, ptB)
#circle = rg.Circle(ptA, 8)
#
#scriptcontext.doc.Objects.AddLine(lineA)
#scriptcontext.doc.Objects.AddCircle(circle)


#ptC = get.GetPoint("pick point", True)
#print ptC
crvC = get.getC

####### extra exercise: find rule to connect points diagonally #########

####### extra exercise: deform grid of points ##########################