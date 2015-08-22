#!/usr/bin/env python

def getHTML():
    f = open('../resource/1.html','r')
    ret = f.read()
    f.close()

    return ret

def writeTest(content):
    f = open('htmlparseresult','w')
    f.write(str(content))
    f.close()
