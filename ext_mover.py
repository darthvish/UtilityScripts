#!/usr/bin/env python
import shutil 
import sys
import os


def validate_args(ext, source_dir, dest_dir):
    ''' check user given args for their validity  '''
    if os.path.isdir(source_dir) and os.access(source_dir, os.W_OK) and os.path.isdir(dest_dir) and os.access(dest_dir, os.W_OK):
        return True
    else:
        return False


def print_help():
    ''' print help message '''
    print "Usage: python <file_ext> <source_dir> <dest_dir>"
    print "file_ext:  file-extensions of files which you wanted to move to another directory"
    print "source_dir: directory-path from which you want to move files to another directory"
    print "dest_dir: directory-path to you want to copy given extension files"


def move_files(ext, source_dir, dest_dir):
    ''' move files to their specified location by using user specified args '''
    for item in os.listdir(source_dir):
        if item.endswith(ext) and os.path.isfile( os.path.join(source_dir, item) ):
            shutil.move( os.path.join(source_dir, item),  os.path.join(dest_dir, item) )


def main():
    ''' starts programs and handle basic stuff '''
    if len(sys.argv) != 4:
        print_help()
    else:
        if validate_args(sys.argv[1], sys.argv[2], sys.argv[3]):
            move_files(sys.argv[1], sys.argv[2], sys.argv[3])
            print "operation completed"
        else:
            print "given arguments are not valid"
            print "for help run script without any args"


if __name__ == "__main__":
    main()