## Given a url, try to retrieve it. If it's text/html,
## print its base url and it text. 

import urllib
import sys

def wget(url):
    ufile = urllib.urlopen(url) ## get file-like object for url
    info = ufile.info() ## meta-info about the url content
    if info.gettype() == 'text/html':
        print 'base url:' + ufile.geturl()
        text = ufile.read() ## read all its text
        print text

def main():
    args = sys.argv[1:]
    if not args:
        print 'usage: url'
        sys.exit(1)

    wget(args[0])


if __name__ == '__main__':
    main()
