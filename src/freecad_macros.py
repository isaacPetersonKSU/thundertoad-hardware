#!/usr/bin/freecadcmd

import sys, FreeCAD, Mesh, Path

def make_stl(input, output):
    print("{} >>---> {}".format(input, output))
    doc = FreeCAD.open(input)
    mesh = doc.ActiveObject
    Mesh.export([mesh], output)
    FreeCAD.closeDocument(doc.Name)

def make_screenshot():
    