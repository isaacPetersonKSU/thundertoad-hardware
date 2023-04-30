#!/usr/bin/python3

# import argparse

# parser = argparse.ArgumentParser(prog='fcexport', description='export as stl')
# parser.add_argument('mesh', type=str, help='stl file to capture')
# parser.add_argument('img', type=str, nargs='?', help='output')
# args = parser.parse_args()


# print(args.mesh, args.img)


import numpy
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot
from matplotlib.colors import LightSource

def plotSTL(filename):
    # Create a new plot
    figure = pyplot.figure(figsize=(20,20))
    axes = figure.add_subplot(111, projection='3d')

    # remove nerdy stuff from background
    axes.set_axis_off()
    axes.set_facecolor('none')

    # Load the STL mesh
    stlmesh = mesh.Mesh.from_file(filename)
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

    pyplot.savefig('foo.png')


plotSTL('../stl/sensor_housing.stl')







# from stl import mesh
# from mpl_toolkits import mplot3d
# from matplotlib import pyplot as plt
# from matplotlib.colors import LightSource
# import numpy as np

# # Create a new plot
# figure = plt.figure()
# axes = figure.add_subplot(projection='3d')

# # Load the STL files and add the vectors to the plot
# your_mesh = mesh.Mesh.from_file('../stl/sensor_housing.stl')
# axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

# # Auto scale to the mesh size
# scale = your_mesh.points.flatten()
# axes.auto_scale_xyz(scale, scale, scale)

# # remove nerdy stuff from background
# axes.set_axis_off()
# axes.set_facecolor('none')

# # color
# blue = np.array([0., 0., 1.])
# rgb = np.tile(blue, (axes.shape[0], axes.shape[1], 1))

# # lights
# light = LightSource(azdeg=225, altdeg=45)
# illuminated_surface = light.shade_rgb(rgb, axes)

# # camera
# axes.view_init(elev=66, azim=-48)
# axes.dist = 10

# # action
# plt.show()