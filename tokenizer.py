#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
tokenizer.py
(C) 2010-2012 by Damir Cavar <dcavar@me.com>

Simple tokenization algorithm. Feel free to expand and extend it.
Returns a list of tokens from some raw text file.
"""


import sys, os, os.path, glob, codecs


delimiterSet = ";.,?\"()':[]\n/+-—==={}><!@#$%^&*’”“|"
digits = "0123456789"
chars = "abcdefghijklmnopqrstuvwxyz"
chars = "".join( (chars, chars.upper()) )
spaces = " \t\n"
numberdelimiters = ",."


def main(fname):
   global delimiterSet

   if not os.path.isfile(fname):
      print("Error: Not a file", fname, "\n")
      usage()
      return

   try:
      inStream = open(fname,"r")
      token = ""
      ch = inStream.read(1)
      lookahead = inStream.read(1)
      while True:
         if not ch:
            if token:
               print token
            break
         if ch in delimiterSet:
            if token:
               if token[-1] in digits and lookahead in digits and ch in numberdelimiters:
                  token = "".join( (token, ch) )
               else:
                  print token
                  token = ""
                  """if ch not in spaces:
                     print ch"""
         elif ch in spaces:
            if token:
               print token
               token = ""
         else:
            token = "".join( (token, ch) )
         ch = lookahead
         lookahead = inStream.read(1)
      inStream.close()
   except IOError:
      print "Cannot read from file:"+ fname

def usage():
   print """
tokenizer.py

Usage:
python3 tokenizer.py mytext.txt myothertext.txt ...
"""


if __name__ == '__main__':
   if len(sys.argv) > 0:
      """for i in sys.argv[1:]:
         for j in glob.glob(i):
            main(os.path.expanduser(os.path.expandvars(j)))"""
      main("stream.dat")
   else:
      usage()
