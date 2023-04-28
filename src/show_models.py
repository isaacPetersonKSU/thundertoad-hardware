import argparse

parser = argparse.ArgumentParser(description='creates STLs from freecad files')
parser.add_argument('target', type=str, help='markdown file to modify')
parser.add_argument('mesh', type=str, help='input file or dir')
parser.add_argument('-v', '--verbose', help='more output', action='store_true')
parser.add_argument('-r', '--recursive', help='export children', action='store_true')
args = parser.parse_args()

if args.dest == None : args.dest = os.getcwd()

args.source = os.path.abspath(args.source)
args.dest = os.path.abspath(args.dest)
