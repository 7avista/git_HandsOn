d#!/usr/bin/env python

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
    if re.search('T+U+', args.seq) or re.search('U+T+',args.seq) or re.search('T+(.)*U+',args.seq) or re.search('U+(.)*T+',args.seq):
        print ('The sequence is inconsistent')
    elif re.search('T', args.seq):            #  looks for T in var to diff to DNA
        print ('The sequence is DNA')
	for i in  len(args.seq):
		t = 0
		c = 0
		g = 0
		a = 0
		if re.search('T'):
			t =  1 + t
		elif re.search('C'):
                        c =  1 + c
		elif re.search('G'):
                        g =  1 + g
		else:
			a = 1 + a 
	print ('The total content of each base is: '\n + 'T' + t/len(args.seq)+100 + '%') 
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
