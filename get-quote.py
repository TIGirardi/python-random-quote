#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse, io, random, sys

# "import this" prints the zen to stdout at first import
_, sys.stdout = sys.stdout, io.StringIO()
import this
_, sys.stdout = sys.stdout, _
_.close()


def parse_args():
  parser = argparse.ArgumentParser(description='Print a random quote')
  parser.add_argument('n', nargs='?', type=int, default=1,
                      help='number of quotes, negatives are treated as 0')
  parser.add_argument('-q', help='add quote to database')
  return parser.parse_args()


def primary():
  args = parse_args()

  new_quote = args.q
  if new_quote:
    with open('quotes.txt', mode='a') as f:
      f.write(new_quote + '\n')

  n = get_number()
  if n <= 0:
    return

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

  print('', *random.sample(quotes, n), sep='\n> ')

if __name__== "__main__":
  primary()
