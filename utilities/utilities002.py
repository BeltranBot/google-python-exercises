## Given a dir path, run an external 'le -l on it--
## shows how to call an external program

import subprocess
import sys

def listdir(dir):
    cmd = 'ls -l ' + dir
    print "Command to run:", cmd
    # status = subprocess.call(cmd.split())
    output = subprocess.check_output(cmd.split())
    print output
    # if status: # Error case, print the command's output to stderr and exit
        # sys.exit(status)
    # print output ## Otherwise do something with the command0's output

def main():
    args = sys.argv[1:]

    if not args:
        print 'usage: dir'
        sys.exit(1)

    listdir(args[0])

if __name__ == '__main__':
    main()
