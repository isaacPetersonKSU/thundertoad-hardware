#!/usr/bin/python3

import argparse
import os
import os.path as path
import datetime

models_header = "# Models\n"


# if trigger_string is in file_path, everthing after will be chopped of
def chop(file_path, trigger_string):
    f = open(file_path, 'r+')
    content = f.read()
    index = content.find(trigger_string)
    if index != -1:
        f.seek(index)
        f.truncate()
    f.close()

def format_pic(image_path):
    name = path.basename(path.splitext(image_path)[0])
    print("relitavie path = {}".format(image_path))
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return '![{}]({} "{}")\n'.format(name, image_path, timestamp)


def update(doc_path, image_dir):
    chop(doc_path, models_header)

    print(image_dir)
    print(doc_path)
    
    file=open(doc_path, 'a')
    file.write(models_header)
    for child in os.listdir(image_dir):
        relative_path = path.relpath(path.join(image_dir, child), path.dirname(doc_path))
        print(relative_path)
        file.write(format_pic(relative_path))
    file.close


parser = argparse.ArgumentParser(prog='updatereadme', 
                                 description='puts images in a markdown file')
parser.add_argument('doc', type=str, help='markdown file to edit')
parser.add_argument('img', type=str, help='file to put in readme')
args = parser.parse_args()

update(args.doc, args.img)
