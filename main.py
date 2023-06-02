import random
import sys
from termcolor import colored


def print_menu():
  print("To begin, start by guessing a 5 letter word")
  print("Guess 1:")



privwordbank = [
  "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
  "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]


def read_random_word():
  with open("words.txt") as f:
    words = f.read().splitlines()
    return random.choice(words)


print_menu()
answer = False
word = read_random_word()
attempt = 0
#print(word)
while attempt < 5:
  attempt = attempt +1
  guess = input().lower()
  if len(guess) == 5:
    for i in range(5):
      if guess == word:
        print(f"Congrats, you got the answer in, {attempt+1}")
        answer = True
        break
        attempt = 6
      if guess[i] == word[i]:
        # print("1" + privwordbank[privwordbank.index(guess[i])])
        #print(guess[i] + " and " + word[i])
        # privwordbank[privwordbank.index(guess[i])] = "G: " + privwordbank[privwordbank.index(guess[i])]
        print(colored(guess[i], 'green'), end="")
      elif guess[i] in word:
        # print("2" + privwordbank[privwordbank.index(guess[i])])
        #  privwordbank[privwordbank.index(guess[i])] = "Y: " + privwordbank[privwordbank.index(guess[i])]
        print(colored(guess[i], 'yellow'), end="")
      else:

        print(colored(guess[i], 'grey'), end="")
        del privwordbank[privwordbank.index(guess[i])]

  else:
    print("guess a word with 5 letters")
    attempt = attempt - 1
  
  if answer == True:
    break
  print("")
  print("Letter bank: ", privwordbank)
  print(f"Guess {attempt+1}", ":")

print("You didnt get it!")