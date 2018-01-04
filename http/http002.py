## Version that uses try/except to print an error message if the
## urlopen() fails.

import urllib
import sys

def wget(url):
    try:
        ufile = urllib.urlopen(url)  # get file-like object for url
        info = ufile.info()  # meta-info about the url content
        if info.gettype() == 'text/html':
            print 'base url:' + ufile.geturl()
            text = ufile.read()  # read all its text
            print text
    except IOError:
        print 'problem reading url:', url


def main():
    args = sys.argv[1:]
    if not args:
        print 'usage: url'
        sys.exit(1)

    wget(args[0])


if __name__ == '__main__':
    main()
