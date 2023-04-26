#!/usr/bin/freecadcmd

import argparse, os

# parse arguments
parser = argparse.ArgumentParser(description='Process a .FCStd file.')
parser.add_argument('file', help='the path to the .FCStd file')
args = parser.parse_args()

if args.file == None:
    print(f'Error: no input file provided')
    exit(1)

# obtain path and extention
split_path = os.path.splitext(args.file)
path = split_path[0]
extn = split_path[1]

# check for correct filetype
if extn != '.FCStd':
    print(f'Error: Invalid file extension. Expected .FCStd extension.')
    exit(1)



import FreeCAD, Mesh, sys, time

# export stl
doc = FreeCAD.open(path + '.FCStd')
Mesh.export([doc.ActiveObject], path + '.stl')
FreeCAD.closeDocument(doc.Name)
