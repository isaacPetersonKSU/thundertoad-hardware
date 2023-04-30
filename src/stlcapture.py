#!/usr/bin/python3

mesh_extention = '.stl'
image_extention = '.png'

import argparse
import os
import os.path as path

import numpy
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot
from matplotlib.colors import LightSource

def plotSTL(mesh_file, image_file):
    # Create a new plot
    figure = pyplot.figure(figsize=(20,20))
    axes = figure.add_subplot(111, projection='3d')

    # remove nerdy stuff from background
    axes.set_axis_off()
    axes.set_facecolor('none')

    # Load the STL mesh
    stlmesh = mesh.Mesh.from_file(mesh_file)
    polymesh = mplot3d.art3d.Poly3DCollection(stlmesh.vectors)

    # Create light source
    ls = LightSource(azdeg=225, altdeg=45)

    # Darkest shadowed surface, in rgba
    dk = numpy.array([0.2, 0.0, 0.0, 1])
    # Brightest lit surface, in rgba
    lt = numpy.array([0.7, 0.7, 1.0, 1])
    # Interpolate between the two, based on face normal
    shade = lambda s: (lt-dk) * s + dk

    # Set face colors 
    sns = ls.shade_normals(stlmesh.get_unit_normals(), fraction=1.0)
    rgba = numpy.array([shade(s) for s in sns])
    polymesh.set_facecolor(rgba)

    axes.add_collection3d(polymesh)

    # Adjust limits of axes to fill the mesh, but keep 1:1:1 aspect ratio
    pts = stlmesh.points.reshape(-1,3)
    ptp = max(numpy.ptp(pts, 0))/2
    ctrs = [(min(pts[:,i]) + max(pts[:,i]))/2 for i in range(3)]
    lims = [[ctrs[i] - ptp, ctrs[i] + ptp] for i in range(3)]
    axes.auto_scale_xyz(*lims)

    pyplot.savefig(image_file)

def find_em(input, output):
    if input.endswith(mesh_extention):
        print("exporting {} as {}".format(input, output))
        plotSTL(input, path.splitext(output)[0] + image_extention)
    elif path.isdir(input):
        if path.isdir(output):
            for child in os.listdir(input):
                find_em(os.path.join(input, child), os.path.join(output, child))
        else: print("output cannot be a file if input is a dir")
    else: print("skipping unknown file {}".format(input))


parser = argparse.ArgumentParser(prog='fcexport', description='export as stl')
parser.add_argument('mesh_file', type=str, help='stl file to capture')
parser.add_argument('img', type=str, nargs='?', help='output')
args = parser.parse_args()


if args.img == None: args.img = os.getcwd()


find_em(args.mesh_file, args.img)
