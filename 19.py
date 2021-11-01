# https://www.hackerrank.com/challenges/text-wrap/problem

import textwrap

def wrap(st, w, s=""):
    while(len(st)>=w): s,st=s+st[:w]+"\n",st[w:]
    return s+st

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)