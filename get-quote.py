#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse, io, random, sys

# "import this" prints the zen to stdout at first import
_, sys.stdout = sys.stdout, io.StringIO()
import this
_, sys.stdout = sys.stdout, _
_.close()

# def mk_parser():
#   parser = argparse.ArgumentParser()
#   parser.add_argument('number')


def primary():
  with open("quotes.txt") as f:
    quotes = [line.strip() for line in f.readlines()]

  zen = this.s.translate(str.maketrans(this.d)) # The Zen of Python
  zen = zen.splitlines()[2:] # strip the title
  zen_special = '\n  > '.join(zen[7:9])
  zen_errors = '\n  > '.join(zen[9:11])
  zen_obvius = '\n  > '.join(zen[12:14])
  zen_timing = '\n  > '.join(zen[14:16])

  zen[14:16] = [zen_timing]
  zen[12:14] = [zen_obvius]
  zen[9:11] = [zen_errors]
  zen[7:9] = [zen_special]

  quotes += zen
  n = len(quotes) - 1

  rnd = random.randint(0, n)
  print('>', quotes[rnd])

if __name__== "__main__":
  primary()
