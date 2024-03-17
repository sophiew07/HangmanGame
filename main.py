# Function that tells user if the letter is in the word
def hangman(userLetter, word):

  # List containing letters inputted by the user, and the correct letters inputted by the user
  letterList = []
  
  # Determining if the letter is in the word or not
  for letter in word:
    if letter != userLetter:
      letterInWord = "_"
      letterList.append(letterInWord)
    elif letter == userLetter:
      letterInWord = letter
      letterList.append(letterInWord)

  # Ensures the user inputs a letter
  if userLetter not in [
      "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
    ]:
      return "Please enter a real letter"

  letterList = " ".join(map(str, letterList))
  return letterList


# Dictionary of words, sorted by difficulty
wordsDict = {
  "easy": [
    'house', 'spark', 'audio', 'chair', 'movie', 'cooks', 'phone', 'purse', 'abyss', 'cough', 'fjord', 'kiosk', 'juice', 'pixel', 'unzip', 'lymph', 'swift', 'crisp', 'candy', 'knock', 'proud', 'track', 'young', 'jazzy','volts', 'waltz', 'diary', 'tough', 'polka', 'rogue', 'rebel', 'yacht', 'klutz', 'kayak', 'brown', 'night', 'cloud', 'under', 'hopes', 'fires', 'quark'
  ],
  "medium": [
    'science', 'ancient', 'coffees', 'fuchsia', 'awkward', 'sweater',
    'jackets', 'oxidize', 'keyhole', 'whiskey', 'blossom', 'sequoia',
    'context', 'absence', 'toenail', 'arsenic', 'numbers', 'hostile',
    'edition', 'hermits', 'tunnels', 'western', 'yawning', 'coupons',
    'haircut', 'pyramid', 'titanic', 'shopper', 'chinese','equator'
  ],
  "hard": [
    'pineapple', 'haphazard', 'incredible', 'espionage', 'fluffiness', 'shakespeare', 'jazziness', 'xylophone', 'copyright', 'biodegradable', 'narcissistic', 'exaggeration', 'bicarbonate', 'realistic', 'einsteinium', 'confidence', 'troublesome', 'hippopotamus', 'optometrist', 'culminating', 'technology', 'laryngoscope', 'bromothymol', 'phenolphthalein', 'presentation', 'cryptography', 'navigation'
  ]
}

# Game start and difficulty selection
print("Welcome to Hangman! Please select your difficulty. ")
userDifficulty = str(input("\nEasy\nMedium\nHard\nDifficulty: "))
userDifficulty = userDifficulty.casefold()
while userDifficulty not in ["easy", "medium", "hard"]:
  userDifficulty = str(input("Please input 'easy', 'medium', or 'hard': "))
userDifficulty = userDifficulty.casefold()
print('''You will have five lives, or "balloons". You will lose a balloon for every wrong letter.''')

play = str(input("Do you want to start the game?: "))
while play not in ["yes", "no"]:
  play = str(input("Please input 'yes' or 'no': "))

import random

# User lives
balloons = [1,2,3,4,5]

while play == 'yes':
  # Hangman word randomizer
  easyWord = random.choice(wordsDict["easy"])
  mediumWord = random.choice(wordsDict["medium"])
  hardWord = random.choice(wordsDict["hard"])

  # Easy word used as mystery word and game begins by collecting user inputs and returning an appropriate response
  if userDifficulty == "easy":
    while len(balloons) >= 1:
      userLetter = str(input("Letter: "))
      while len(userLetter) > 1:
        userLetter = str(input("Only input one letter: "))
      else:
        print(hangman(userLetter, easyWord))
        # Counting balloons (user's lives left)
        if userLetter not in easyWord:
          del balloons [-1]
        if len(balloons) <= 0:
          print("You have no more balloons!")
        else:
          print("You have " + str(len(balloons)) + " balloons left.")
      userAnswer = str(input("Do you think you know the answer?: "))
      while userAnswer not in ["yes", "no"]:
        userAnswer = str(input("Please input 'yes' or 'no': "))
      if userAnswer in "yes":
        userWord = str(input("Answer: "))
        if userWord == easyWord:
          print("Congrats, you got it!")
          play = str(input("Do you want to play again? "))
          play = play.casefold()
          if play == "yes":
            easyWord = random.choice(wordsDict["easy"])
          if play == "no":
            print("Thanks for playing.")
            break
        elif userWord != easyWord:
          print("Sorry, that was not correct. You have " + str(len(balloons)) + " balloons left.")
      if userAnswer in "no" and len(balloons) <= 0:
        print("The answer was " + str(easyWord) + ". Well played.")
      elif userAnswer in "no":
        pass
      elif len(balloons) <= 0:
        print("The answer was: " + str(easyWord) + ". Well played.")

# Medium word used as mystery word and game begins by collecting user inputs and returning an appropriate response
  elif userDifficulty == "medium":
    while len(balloons) >= 1:
      userLetter = str(input("Letter: "))
      while len(userLetter) > 1:
        userLetter = str(input("Only input one letter: "))
      else:
        print(hangman(userLetter, mediumWord))
        # Counting balloons (user's lives left)
        if userLetter not in mediumWord:
          del balloons [-1]
        if len(balloons) <= 0:
          print("You have no more balloons!")
        else:
          print("You have " + str(len(balloons)) + " balloons left.")
      userAnswer = str(input("Do you think you know the answer?: "))
      while userAnswer not in ["yes", "no"]:
        userAnswer = str(input("Please input 'yes' or 'no': "))
      if userAnswer in "yes":
        userWord = str(input("Answer: "))
        if userWord == mediumWord:
          print("Congrats, you got it!")
          play = str(input("Do you want to play again? "))
          play = play.casefold()
          if play == "yes":
            mediumWord = random.choice(wordsDict["medium"])
          if play == "no":
            print("Thanks for playing.")
            break
        elif userWord != mediumWord:
          print("Sorry, that was not correct. You have " + str(len(balloons)) + " balloons left.")
      if userAnswer in "no" and len(balloons) <= 0:
        print("The answer was " + str(mediumWord) + ". Well played.")
      elif userAnswer in "no":
        pass
      elif len(balloons) <= 0:
        print("The answer was: " + str(mediumWord) + ". Well played.")
        
  # Hard word used as mystery word and game begins by collecting user inputs and returning an appropriate response
  elif userDifficulty == "hard":
    while len(balloons) >= 1:
      userLetter = str(input("Letter: "))
      while len(userLetter) > 1:
        userLetter = str(input("Only input one letter: "))
      else:
        print(hangman(userLetter, hardWord))
        # Counting balloons (user's lives left)
        if userLetter not in hardWord:
          del balloons [-1]
        if len(balloons) <= 0:
          print("You have no more balloons!")
        else:
          print("You have " + str(len(balloons)) + " balloons left.")
      userAnswer = str(input("Do you think you know the answer?: "))
      while userAnswer not in ["yes", "no"]:
        userAnswer = str(input("Please input 'yes' or 'no': "))
      if userAnswer in "yes":
        userWord = str(input("Answer: "))
        if userWord == hardWord:
          print("Congrats, you got it!")
          play = str(input("Do you want to play again? "))
          play = play.casefold()
          if play == "yes":
            hardWord = random.choice(wordsDict["hard"])
          if play == "no":
            print("Thanks for playing.")
            break
        elif userWord != hardWord:
          print("Sorry, that was not correct. You have " + str(len(balloons)) + " balloons left.")
      if userAnswer in "no" and len(balloons) <= 0:
        print("The answer was " + str(hardWord) + ". Well played.")
      elif userAnswer in "no":
        pass
      elif len(balloons) <= 0:
        print("The answer was: " + str(hardWord) + ". Well played.")