#!/usr/bin/python3

import argparse
parser = argparse.ArgumentParser(description='creates STLs from freecad files')
parser.add_argument("dest", type=str, help="FILE.FCStd")
parser.add_argument("source", type=str, help="output directory")
args = parser.parse_args()

# file = '/home/ijp/thundertoad/hardware/freecad/unibody.FCStd'
# output = '/home/ijp/thundertoad/hardware/stl/output.stl'
file = args.source
output = args.dest


import subprocess
print("invokeing freecad")
args = ["./freecad_export_stl.py", file, output]
result = subprocess.run(args, stdout=subprocess.PIPE)
# if verbose=True:
#    print(result.stdout.decode())
