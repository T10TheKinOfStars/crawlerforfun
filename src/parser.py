#!/usr/bin/env python

#html parser

import fileworker                   #when import other file will generate .pyc file
from pyquery import PyQuery

def getResTb():
    html = fileworker.getHTML()
    pq = PyQuery(html)
    result = dict()
    blocks = list()
    for i in pq.items('.row.result'):
        list.append(i)
    #scan blocks to store related companys into result dictionary

getResTb()
