import random

def primary():
  with open("quotes.txt") as f:
    quotes = f.readlines()

  rnd = random.randrange(len(quotes))
  print(quotes[rnd])

if __name__== "__main__":
  primary()
