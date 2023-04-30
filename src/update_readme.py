#!/usr/bin/python3

import argparse
import os.path as path
import datetime


# if trigger_string is in file_path, everthing after will be chopped of
def chop(file_path, trigger_string):
    f = open(file_path, 'r+')
    content = f.read()
    index = content.find(trigger_string)
    if index != -1:
        f.seek(index)
        f.truncate()
    f.close()

def append_img(doc_path, image_path):
    name = path.basename(path.splitext(image_path)[0])
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    f = open(doc_path, 'a')

    f.write('![{}]({})\n'.format(name, image_path))
    f.close()



parser = argparse.ArgumentParser(prog='updatereadme', 
                                 description='puts images in a markdown file')
parser.add_argument('doc', type=str, help='markdown file to edit')
parser.add_argument('img', type=str, help='file to put in readme')
args = parser.parse_args()

args.img = path.join(args.img, "unibody.png")

append_img(args.doc, args.img)

