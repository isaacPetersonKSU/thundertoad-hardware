#!/usr/bin/python3
import argparse, subprocess, os

freecad_extention = '.FCStd'
ascii_stl_extention = '.ast'

def export(input, output):
    if not output.endswith(ascii_stl_extention): 
        output = output.split('.')[0] + ascii_stl_extention

    if args.verbose: print("exporting " + input + " as " + output)
    freecad_args = ["/home/ijp/thundertoad/hardware/src/freecad_export_stl.py", input, output]
    result = subprocess.run(freecad_args, stdout=subprocess.PIPE)
    if args.verbose:
        print(result.stdout.decode())


def find_em(source, dest):
    if source.endswith(freecad_extention): export(source, dest)
    elif os.path.isdir(source):
        if args.recursive:
            for child in os.listdir(source): 
                find_em(os.path.join(source, child), os.path.join(dest, child))
        else: print(source, "is a directory. Use -r")
    elif args.verbose: print(source + " is not a freecad file or directory")


parser = argparse.ArgumentParser(description='creates STLs from freecad files')
parser.add_argument('source', type=str, help='input file or dir')
parser.add_argument('dest', type=str, nargs='?', help='output dir')
parser.add_argument('-v', '--verbose', help='more output', action='store_true')
parser.add_argument('-r', '--recursive', help='export children', action='store_true')
args = parser.parse_args()

if args.dest == None : args.dest = os.getcwd()

args.source = os.path.abspath(args.source)
args.dest = os.path.abspath(args.dest)


if(args.source.endswith(freecad_extention)): 
    export(args.source, os.path.join(args.dest, os.path.basename(args.source)))

else: find_em(args.source, args.dest)
