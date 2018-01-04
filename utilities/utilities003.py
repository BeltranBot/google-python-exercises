 ## Example pulls filenames from a dir, 
 ## prints their relative and absolute paths

import os
import sys

def open_file(filename):
    try:
        f = open(filename, 'rU')
        text = f.read()
        f.close()
    except IOError:
        ## Control jumps directly to here if any of the above lines
        ## thros IOError
        sys.stderr.write('problem reading: ' + filename)
    ## In any case, the code then continues with the line after
    ## the try/except

def main():
    args = sys.argv[1:]

    if not args:
        print 'usage: file'
        sys.exit(1)

    open_file(args[0])

if __name__ == '__main__':
    main()
