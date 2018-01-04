import re

text = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)

for email in emails:
    print email
