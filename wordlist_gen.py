#first import all req module
import os
import sys
import time
import string
import argparse
import itertools
from subprocess import call


def wordlist(chrs, min_length, max_length, output):
    #here min_length value should be less compare to max_length
    if min_length > max_length:
        print("[+] min_length value Should be small or same as max_length")
        sys.exit()

    #check file path if it not exit then make a new dir & save
    if os.path.exists(os.path.dirname(output)) == False:
        os.makedirs(os.path.dirname(output))

    print()
    print("[+] creating a wordist at %s :\n" %output)
    print ('[+] Starting time is %s : \n' % time.strftime('%H:%M:%S'))
    output = open(output,'w')

    #now write the actual algo
    for n in range(min_length, max_length+1):
        for xs in itertools.product(chrs, repeat=n):
            chars = ''.join(xs)
            output.write("%s\n" % chars)
            sys.stdout.write('\r[+] saving character `%s`' % chars) #it's showing the current character
            sys.stdout.flush()

    output.close()

    print()
    print ('\n[+] End time: %s\n' % time.strftime('%H:%M:%S'))            

    

    
        
    

def main():
    parser = argparse.ArgumentParser(description='Python Wordlist Generator')
    parser.add_argument('-chr','--chars',default=None, help='characters to iterate')
    parser.add_argument('-min','--min_length', type=int,default=1, help='minimum length of characters')
    parser.add_argument('-max','--max_length', type=int,default=2, help='maximum length of characters')
    parser.add_argument('-out','--output',default='output/wordlist.txt', help='output of wordlist file.')
    args = parser.parse_args()
    if args.chars is None:
        os.system('python wordlist_gen.py -h')
    else:
        wordlist(args.chars, args.min_length, args.max_length, args.output)





if __name__ == "__main__":
    main()

