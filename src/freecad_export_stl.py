#!/usr/bin/freecadcmd

import sys, FreeCAD, Mesh, Path
tolerance_millimeters = 1

if len(sys.argv) < 4:
     print("Usage: {} [input.FCStd] [output.stl]".format(sys.argv[1]))
     exit(1)




doc = FreeCAD.open(sys.argv[2])
mesh = doc.ActiveObject
Mesh.export([mesh], sys.argv[3])
FreeCAD.closeDocument(doc.Name)









# doc = FreeCAD.open(sys.argv[2])
# obj = doc.ActiveObject
# mesh = Mesh.Mesh(obj.Mesh.copy())
# mesh.simplify(.5)

# mesh.simplify(tolerance_millimeters)
# Mesh.export([doc.ActiveObject], sys.argv[3])
# FreeCAD.closeDocument(doc.Name)


# Mesh.export([mesh], "/path/to/myfile.stl")