#!/usr/bin/python3
import argparse, subprocess, os

def export(input, output):
    if args.verbose: print("exporting " + input + " as " + output)
    freecad_args = ["/home/ijp/thundertoad/hardware/src/freecad_export_stl.py", input, output]
    result = subprocess.run(freecad_args, stdout=subprocess.PIPE)
    if args.verbose:
        print(result.stdout.decode())


def find_em(relative_path):
    if args.verbose: print("searching " + relative_path)
    getit = args.source + relative_path
    if '.' in relative_path: [relative_path, extention] = relative_path.split('.')
    elif '.' in args.source: [args.source, extention] = args.source.split('.')
    sndit = args.dest + relative_path + '.stl'

    if args.verbose: print('exporting' + getit + 'as' + sndit)

    if not os.path.exists(sndit): open(sndit, 'x').close()
    elif args.verbose: print("overwriting" + sndit)
    
    
    if args.verbose: print(getit + ">>>--->" + sndit)

    if extention=='FCStd': export(getit, sndit)
    elif os.path.isdir(getit):
        if args.recursive:
            for child in os.listdir(getit): find_em(relative_path + child)
        else: print(getit, "is a directory. Use -r")
    elif args.verbose:
        print(getit + " doesn't look like a freecad model")


parser = argparse.ArgumentParser(description='creates STLs from freecad files')
parser.add_argument('source', type=str, help='input file')
parser.add_argument('dest', type=str, nargs='?', help='output file or dir')
parser.add_argument('-v', '--verbose', help='more output', action='store_true')
parser.add_argument('-r', '--recursive', help='export children', action='store_true')
args = parser.parse_args()

args.source = os.path.abspath(args.source)

if args.dest==None:
    args.dest = args.source.split('.')[0]
elif os.path.isfile(args.dest):
    if args.recursive: print("-r detected " + args.dest + " must be a directory")
    elif os.path.isdir(args.source): print("cannot batch export into a single file")
    elif not args.dest.endswith('.stl'): print(args.dest + "must end with .stl")
    else: 
        export(args.source, args.dest)
        exit(0)

find_em("")
