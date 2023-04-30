#!/bin/bash

cad_path='../drawings'
mesh_path='../stl'
img_path='../img'

# generate STLs
./fcexport.py ${cad_path} ${mesh_path}
echo # freecad fucks up the text buffer, so we gotta insert a blank line

# generate PNGs
./stlcapture.py ${mesh_path} ${img_path}

# put images in the readme
