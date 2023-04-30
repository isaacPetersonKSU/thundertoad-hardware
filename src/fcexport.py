#!/usr/bin/freecadcmd

import os, FreeCAD, Mesh, argparse

freecad_extention = '.FCStd'
stl_extention = '.stl'
image_extention = '.jpeg'

def make_stl(cad_file, mesh_file):
    print("sendit")
    doc = FreeCAD.open(cad_file)
    print("exporting {} as {}".format(cad_file, mesh_file))
    mesh = doc.ActiveObject
    Mesh.export([mesh], mesh_file)
    FreeCAD.closeDocument(doc.Name)

def find_em(input, output):
    if input.endswith(freecad_extention):
        make_stl(input, os.path.splitext(output)[0] + stl_extention)

    elif os.path.isdir(input):
        if os.path.isdir(output):  
            for child in os.listdir(input):
                find_em(os.path.join(input, child), os.path.join(output, child))
        else: print("output cannot be a file if input is a dir")
    else: print("skipping unknown file {}".format(input))

parser = argparse.ArgumentParser(prog='fcexport', description='export as stl')
parser.add_argument('script_name') # this will always be fcad.py
parser.add_argument('source', type=str, help='input file or dir')
parser.add_argument('dest', type=str, nargs='?', help='output dir')
args = parser.parse_args()

if args.dest==None: args.dest = os.getcwd()
find_em(args.source, args.dest)

