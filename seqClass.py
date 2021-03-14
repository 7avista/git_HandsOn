#!/usr/bin/env python

import sys, re                             #  add sys var and access to re module (RegEx)
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")
# creates  an ArgumentParser objects as strings and fills  them

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()                  # calls  parse_args()

args.seq = args.seq.upper()                 #  converts to uppercase
if re.search('^[ACGTU]+$', args.seq):       # defines the re expression in var
    if re.search('T', args.seq):            #  looks for T in var to diff to DNA
        print ('The sequence is DNA')
    elif re.search('U', args.seq):          # looks for U in var to diff to RNA
        print ('The sequence is RNA')
    else:                                   # rest of cases unable to diff
        print ('The sequence can be DNA or RNA') 
else:
    print ('The sequence is not DNA nor RNA') # var doesn't fit  with ntd seqs


if args.motif:                             # calls for motif var
  args.motif = args.motif.upper()          # converts to lower case
  print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
  if re.match(args.motif, args.seq):       # looks for matches into seq var to T
    print("MOTIF IS FOUND")
  else:                                    #  match isn't found F
    print("MOTIF IS NOT FOUND")
