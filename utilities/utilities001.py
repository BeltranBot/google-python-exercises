 ## Example pulls filenames from a dir, 
 ## prints their relative and absolute paths

import os
import sys

def printdir(dir):
    filenames = os.listdir(dir)
    for filename in filenames:
        print filename ## foo.txt
        print os.path.join(dir, filename)
        print os.path.abspath(os.path.join(dir, filename))

def main():
    args = sys.argv[1:]

    if not args:
        print 'usage: dir'
        sys.exit(1)

    printdir(args[0])

if __name__ == '__main__':
    main()
