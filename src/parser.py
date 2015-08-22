#!/usr/bin/env python

#html parser

import fileworker                   #when import other file will generate .pyc file
from pyquery import PyQuery

def getResTb():
    html = fileworker.getHTML()
    pq = PyQuery(html)
    tag = pq(".summary")
    fileworker.writeTest(tag)

getResTb()
