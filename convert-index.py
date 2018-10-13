#!/usr/bin/env python

import sys
import re

with open(sys.argv[1], 'rb') as fh:
    data = fh.read()

for line in data.split("\n"):
    x = re.match("^(\s*)1\. (.*)", line)
    if x:
        x = list(x.groups())
        print '%s#. %s' % (x[0], x[1])
    else:
        print line
