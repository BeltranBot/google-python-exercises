#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands
import re
import subprocess

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(dir):
    # get_special_paths(dir) -- 
    # returns a list of the absolute paths of the special files
    # in the given directory
    abs_paths = []
    filenames = os.listdir(dir)
    for filename in filenames:
        if re.search(r'__\w+__', filename):
            abs_paths.append(
                os.path.abspath(os.path.join(dir, filename)))
    return abs_paths


def copy_to(paths, dest):
    # copy_to(paths, dir) given a list of paths,
    # copies those files into the given directory
    if not os.path.exists(dest):
        os.makedirs(dest)

    for path in paths:
        shutil.copy(path, dest)


def zip_to(paths, zipfile):
    # cmd = 'zip -j ' + zipfile + ' ' + ' '.join(paths)
    cmd = '7z a ' + zipfile + ' ' + ' '.join(paths)
    print 'command to run: ' + cmd
    status = subprocess.call(cmd.split())



def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print "usage: [--todir dir][--tozip zipfile] dir [dir ...]"
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if len(args) == 0:
        print "error: must specify one or more dirs"
        sys.exit(1)

    # +++your code here+++
    # Call your functions
    paths = []
    for path in args:
        paths.extend(get_special_paths(path))    

    if todir:
        copy_to(paths, todir)
    elif tozip:
        zip_to(paths, tozip)
    else:
        print '\n'.join(paths)

if __name__ == "__main__":
    main()
