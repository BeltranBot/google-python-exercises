import re

text = 'purple alice-b@google.com monkey dishwasher'
match = re.search('([\w.-]+)@([\w.-]+)', text)

if match:
    print match.group()
    print match.group(1)
    print match.group(2)
