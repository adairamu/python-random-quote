
import random
def dude():
  #print("Keep it logically awesome.")
  #last = len(quotes) - 12
  #rnd = random.randint(0, last)

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = len(quotes) - 0
  rnd = random.randint(0, last)
  print(quotes[rnd])

if __name__== "__main__":
  dude()
