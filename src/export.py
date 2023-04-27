#!/usr/bin/freecadcmd

import argparse
parser = argparse.ArgumentParser(description='creates STLs from freecad files')
#1parser.add_argument("file", type="str", help="FILE.FCStd")
#parser.add_argument("dest", type="str", help="output directory")
parser.parse_args()


file = '/home/ijp/thundertoad/hardware/freecad/unibody.FCStd'
output = '/home/ijp/thundertoad/hardware/stl/output.stl'







# import subprocess
# print("invokeing freecad")
# args = ["./fcdexp_freecad.py", file, output]
# result = subprocess.run(args, stdout=subprocess.PIPE)
# if verbose=True:
#    print(result.stdout.decode())
