This python script is able to differentiate if a sequence is made of DNA or RNA, or even if it does not match any of them.
It can also check if one predefined motif is also present in the sequence.

First of all we need to import both objects to be tested by the script, but first we defined the sys variables and the use of RegEx expressions.

```
import sys, re                             #  add sys var and access to re module (R>from argparse import ArgumentParser
```
Next we create ArgumentParser objects as strings and fill them

```
parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequen>parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")
''' 

Also prints a help message if no arguments are supplied on the command line.
```
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)
```
Then the script calls for the arguments to be evaluated.

```
args = parser.parse_args()                  # calls  parse_args()
```

Then any argument i considered as uppercase string and after that it is evaluated.

```
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
'''

The sript returns the results of the kind of sequence evaluated.
And then it calls to the motif variable to be searched for which was already stored to be evaluated whether present or not in the sequence.
Again it cares of converting to uppercase in case it wasn't in this format.

```
if args.motif:                             # calls for motif var
  args.motif = args.motif.upper()          # converts to lower case
  print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.>  if re.match(args.motif, args.seq):       # looks for matches into seq var to T
    print("MOTIF IS FOUND")
  else:                                    #  match isn't found F
    print("MOTIF IS NOT FOUND")
 ```
 Once evaluated the output is printed.
