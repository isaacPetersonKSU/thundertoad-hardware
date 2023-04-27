#!/usr/bin/freecadcmd

import sys, FreeCAD, Mesh, Path

print(sys.argv)
if len(sys.argv) < 4:
     print("Usage: {} [input.FCStd] [output.stl]".format(sys.argv[1]))
     exit(1)

doc = FreeCAD.open(sys.argv[2])
Mesh.export([doc.ActiveObject], sys.argv[3])
FreeCAD.closeDocument(doc.Name)
