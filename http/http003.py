import urllib
import sys
import json

def wget(url, user_id):
    ufile = urllib.urlopen(url) ## get file-like object for url
    info = ufile.info() ## meta-info about the url content
    base_cdn = 'https://i.4cdn.org/soc/'
    if info.gettype() == 'application/json':
        # print 'base url:' + ufile.geturl()
        data = json.loads(ufile.read())
        # print data['posts']
        for post in data['posts']:
            if post['id'] == user_id:
                filename = str(post['tim']) + str(post['ext'])
                file_url = base_cdn + filename
                print 'downloading: ' + file_url
                
                urllib.urlretrieve(
                    file_url,
                    'images/' + filename
                )


def main():
    args = sys.argv[1:]
    if not args:
        print 'usage: url'
        sys.exit(1)

    wget(args[0], args[1])


if __name__ == '__main__':
    main()
