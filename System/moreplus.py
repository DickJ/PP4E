#!/usr/bin/env python3
"""
split and interactively page a string, file, or stream of
text to stdout; when run as a script, page stdin or file
whose name is passed on cmdline; if input is stdin, can't
use it for user reply--use plateform-specific tools or GUI;
"""

import sys

def getreply():
    """
    read a reply key from an interative user
    even if stdin redirected to a file or pipe
    """
    if sys.stdin.isatty():
        return input('??')
    else:
        if sys.platform[:3] == 'win':
            import msvcrt
            msvcrt.putch(b'?')
            key = msvcrt.getche()
            msvcrt.putch(b'\n')
            return key
        else:
            #assert False, 'platform not supported'
            print('???')
            key = open('/dev/tty').readline()[:-1]
            print(key)
            return key

def more(text, numlines=10):
    """
    page multiline string to stdout
    """
    lines = text.splitlines()
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk: print(line)
        if lines and getreply() not in [b'y', b'Y', 'y', 'Y']: break

if __name__ == '__main__':
    print(sys.platform)
    if len(sys.argv) == 1:
        more(sys.stdin.read())
    else:
        more(open(sys.argv[1]).read())
            