#!/usr/bin/env python3

"""
mens	large	heather purple
mens	small	heather seafoam
womens	medium	Heather Purple
womens	medium	berry
mens 	medium 	heather coral silk
womens	Small	Kiwi
mens	large	Graphite Heather
mens	large	sport grey
"""

import os
import sys


def usage(message=None, exitcode=1, stream=sys.stderr):
  message = '' if message is None else f'\n\nERROR: {message}\n\n'

  stream.write("\n")
  stream.write("Usage: %s <input.tsv>\n\n" % os.path.basename(sys.argv[0]))
  stream.write(
    "Notes:\n"
    " - input.tsv is a TSV file containing three columns (additional\n"
    "   columns are ignored) in the format: <mens|womens>\\t<size>\\t<color>\n"
  )
  stream.write(message)
  
  sys.exit(exitcode)


  
def main(argv):
  if len(argv) != 1:
    usage('Unexpected number of arguments')
  
  shirts = {}
  with open(argv[0], "r") as file_object: 
    for line in file_object:
      if line.lstrip().startswith("#"):
        continue
      
      fields = line.strip().split("\t")
      
      style = fields[0].strip().lower().replace("'","")  # men's | women's
      size = fields[1].strip().lower()
      color = fields[2].strip().lower()

      # normalize sizes of form large, xlarge, xl, xxl, 2xl, etc.
      for s in ('small','medium','large'):
        if size.endswith(s):
          size = size[:size.index(s)] + s[0]

      if 'x' in size:
        if size[0] in set(map(str, range(10))):
          pass
        else:
          xcount = size.count('x')
          size = 'x' + size[-1]
          if xcount > 1:
            size = str(xcount) + size
          
      size = size.upper()
        
      if style not in shirts:
          shirts[style] = {}
      if size not in shirts[style]:
          shirts[style][size] = {}
      if color not in shirts[style][size]:
          shirts[style][size][color] = 0
      shirts[style][size][color] += 1

  for style in shirts:
    for size in shirts[style]:
      for color in shirts[style][size]:
        count = shirts[style][size][color]
        print(style,size,color,count,sep="\t")
      
  # print(shirts, file=sys.stderr)


    
main(sys.argv[1:])
