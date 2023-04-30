#!/bin/bash

drawing='../drawings'
mesh='../stl'
photo='../image/sensor_housing.png'

./fcexport.py ${drawing} ${mesh}
echo # freecad fucks up the text buffer, so we gotta insert a blank line

# vtk render -E 0.1 -S 600,600 -F example.png ../stl/sensor_housing.FCStd
