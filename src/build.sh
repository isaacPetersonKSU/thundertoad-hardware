#!/bin/bash

cad_path='../drawings'
mesh_path='../stl'
img_path='../img'
read_me='../readme.md'

./fcexport.py ${cad_path} ${mesh_path} > /dev/null \
    && echo 'meshes exported' || echo 'error exporting meshes'

./stlcapture.py ${mesh_path} ${img_path} > /dev/null \
    && echo 'images rendered' || echo 'error rendering images'

./update_readme.py ${read_me} ${img_path} > /dev/null \
    && echo 'images embedded' || echo 'error embedding images'


git add --a
