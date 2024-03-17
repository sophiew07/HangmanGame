
userLetter = "e"
word = "house"
letterList = []

for letter in word:
  if letter == userLetter:
    letterInWord = letter
    letterList.append(letterInWord)
  elif letter != userLetter:
    letterInWord = "_"
    letterList.append(letterInWord)
letterList = " ".join(map(str,letterList))  
print(letterList)

