#!/usr/bin/env python

import sys
import re

with open(sys.argv[1], 'r') as fh:
    lines = fh.readlines()

lines = [x.rstrip() for x in lines]

output = []
count = 0
funky_list = False
funky_state = 0
next_line = ''

for line in lines:
    line = line.replace('\xc2', '')
    line = line.replace('\xa0', ' ')

    if re.match(r'^\s*[-]*\s*$', line):
        continue
    z = re.match(r'\[\]\{\#\d+\}(.*)', line)
    if z:
        line = z.groups()[0]
    line = line.rstrip('\\')
    line = line.rstrip()

    x = re.match(r"^\s*\*\*(\d+(?:\.\d+)*)\s+(.*?)\*\*(.*)", line)
    y = re.match(r'^[a-zA-Z\(]{2,}.*', line)
    z = re.match(r'^\*\*([\w\s]+)[:]?\*\*(.*)$', line)
    w = re.match(r'^\d+[\.\)] (.*)', line)

    odd_hex = line
    line = line.replace('e280a2'.decode('hex'), '*')
    line = line.replace('\xe2\x80\xc2', '*')
    line = line.replace('\xe2', '*')
    if odd_hex != line:
        line.strip()

    if w:
        w = list(w.groups())
        line = '* ' + w[0]

    if x:
        x = list(x.groups())
        count = 0
        while '.' in x[0]:
            x[0] = x[0].replace('.', ' ', 1)
            count += 1
        msg = '%s %s' % (x[1].strip(), x[2].strip())
        msg = msg.replace('  ', ' ')
        while '**' in msg:
            msg = msg.replace("**", "")
        output.append('    ' * count + '1. ' + msg)
    elif y:
        while '**' in line:
            line = line.replace("**", "")
        if funky_state == 2:
            output.append("")
            output.append('    ' * (count + 1) + line)
            funky_state = 0
        else:
            output[-1] += ' ' + line
    elif z:
        x = list(z.groups())
        # print 'WTF' + repr(x)
        line = '    ' * (count + 1) + '* ' + x[0]
        if len(x[1]):
            line += ': ' + x[1]
            output.append(line)
        funky_state = 1
    elif line.lstrip().startswith('*'):
        while '  ' in line:
            line = line.replace("  ", " ")
        line.strip()
        line.replace("**", "")
        output.append("    " * (count + 1) + line)
    elif len(line):
        output.append(line)
    else:
        if funky_state == 1:
            funky_state = 2

output = [x.rstrip() for x in output]
output = '\n'.join(output)
output.replace("**", "")
print output