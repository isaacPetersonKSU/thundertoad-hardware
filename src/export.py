#!/usr/bin/python3
import argparse, subprocess, os

freecad_extention = '.FCStd'
stl_extention = '.stl'
image_extention = '.jpeg'

def run_macro(macro, arguments):
    arg_string = '"' + '","'.join(arguments) + '"'
    arg_string = 'from freecad_macros import {}; {}({})'.format(macro, macro, arg_string)
    result = subprocess.run(['freecadcmd', '-c', arg_string], stdout=subprocess.PIPE)
    if args.verbose: print(result.stdout.decode())


def export(input, mesh):
    mesh = mesh.split('.')[0] + stl_extention
    try: open(mesh, "w").close() #freecad needs her files already created
    except Exception as e: print("Error:", e)
    run_macro('make_stl', [input, mesh])


def screenshot(input, image):
    image = image.split('.')[0] + image_extention
    run_macro('make_screenshot', [input, image])


def find_em(source, dest):
    if source.endswith(freecad_extention): 
        export(source, dest)
        screenshot(source, dest)
    elif os.path.isdir(source):
        if args.recursive:
            for child in os.listdir(source): 
                find_em(os.path.join(source, child), os.path.join(dest, child))
        else: print("{} is a directory. Use -r".format(source))
    elif args.verbose: print("{} is not a freecad file or dir".format(source))


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
