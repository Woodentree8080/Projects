#Different times
#Different Seats
#Different Classes

import nltk #Imports a package that enables me to tokenize a sentence
nltk.download('punkt') #This downloads punctutaion that can be used in the code

import time
import random

def OG():
  end = 0
  q = "What would you like to do today? "
  def choice():
    choice1 = input(q).lower() #Changes everything inputted into it to lower case
    choice1 = nltk.word_tokenize(choice1)  #This uses a function of the nltk package, tokenizing, to seperate the different words I
    return choice1
  def place():
    if 'adelaide' in choice2 or 'melbourne' in choice2 or 'hobart' in choice2 or 'canberra' in choice2 or 'sydney' in choice2 or 'brisbane' in choice2 or 'darwin' in choice2 or 'perth' in choice2:
      return 1
    else:
      return 2
  def cancel():
    if 'cancel' in choice2 or 'refund' in choice2 or 'end' in choice2:
      return 1
    else:
      return 2
  def rich():
    if 'first' in choice2:
      return 1
    elif 'business' in choice2:
      return 2
    elif 'economy' in choice2:
      return 3
    else:
      return 4
  def space():
    print('\n---------------------------------------------------------\n ')
  while end == 0:
    space()
    choice2 = choice()
    if 'flight' in choice2 or 'fly' in choice2 or 'travel' in choice2 or 'go' in choice2 or 'plane' in choice2 or 'hire' in choice2 or 'trip' in choice2 or 'book' in choice2 or 'booking' in choice2:
      c = cancel()
      class1 = rich()
      if c == 1:
        if place() == 1:
          space()
          if rich() in range (0,4):
            print('Your flight has been cancelled')
            end = 1
          else:
            print(('I would love to cancel your flight, but first I must know what class you were in'))
        else:
          print('I would love to cancel your flight, but first I must know where you were heading')
      if place() == 2:
        q = "Where were you going? "
        space()
        choice2 = choice()
        while place() != 1:
          print("Sorry, we don't have flights available to there. ")
          print("Please pick one of the capital cities in Australaia instead")
          choice2 = choice()
        if c == 1:
          space()
          if class1 in range (0,4):
            print('Your flight has been cancelled')
            end = 1
          else:
            print(('I would love to cancel your flight, but first I must know what class you were in'))
        else:
          space()
          if class1 in range (0,4):
            print('Your flight has been booked')
            end = 1
          else:
            print(('I would love to book your flight, but first I must know what class you were in'))
      if class1 not in range (0,4):
        print('We offer seats in First Class, Business Class and Economy')
        q = "What class were you in? "
        space()
        choice2 = choice()
        while rich() not in range (0,4):
          print("Sorry, we don't have flights available to there. ")
          print("Please pick one of the capital cities in Australia instead")
          choice2 = choice()
        if c == 1:
          space()
          print('Your flight has been cancelled')
          end = 1
        else:
          space()
          print('Your flight has been booked')
          end = 1
    else:
      print('Sorry, but I am a Flightbot, please ask me to do something flight related')


def rate():
  r = int(input('How would you rate my service out of 10? '))
  if r >= 9:
    sug = input('What do you think was the part of my service? ').lower()
    print('Thank you!, I will try and bring the other parts of my interface to the same standard as my ', sug, 'next time')
  elif r >= 4:
    if r <= 7:
      sug = input('I hope to do better next time! How do you think I can improve my service? ').lower()
      print('I will try to', sug, 'next time')
  else:
    sug = input('I am really sorry, please tell me how to improve my service! ').lower()
    print('I will try to', sug, 'next time')

exit = 'yes'

print("Welcome to Flightbot, the Chatbot!")
while exit != 'no':
  OG()
  time.sleep(0.5)
  exit = input('Would you like me to do anything else for you today?, (yes/no) ').lower()
  time.sleep(0.5)
rate()