import re

text = 'an example word:cat!!!'
match = re.search(r'word:\w\w\w', text)

if match:
    print 'found', match.group()
else:
    print 'did not find'
