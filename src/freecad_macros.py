#!/usr/bin/freecadcmd

import FreeCAD, Mesh, FreeCADGui, os

def make_stl(input, output):
    print("{} >>---> {}".format(input, output))
    doc = FreeCAD.open(input)
    mesh = doc.ActiveObject
    Mesh.export([mesh], output)
    FreeCAD.closeDocument(doc.Name)

def make_screenshot(input, output):
    print("{} >>---> {}".format(input, output))

    FreeCADGui.runCommand("Std_Open", input)
    Gui = FreeCADGui.getMainWindow()
    screen = Gui.getScreen()
    img = screen.grabWindow()

    img.save(output, "PNG")
    os.system("xdg-open " + output)