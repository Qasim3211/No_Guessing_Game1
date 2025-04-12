import random
guess_range = 50
answer = random.randint(1, guess_range)
print("welcome to the numbre guessing game")
print("")
userInput = input("Guess a number between 1 and " + str(guess_range) + ": ")
guess = int(userInput)
guess = ""
while guess != answer:
  userInput = input("Guess a number between 1 and " + str(guess_range) + ": ")
  guess = int(userInput)
  print("Congratulations! You guessed the correct number. You win!")
  guesses_allowed = 10
  for i in range(guesses_allowed):
   userInput = input("Guess a number between 1 and " + str(guess_range) + ": ")
   guess = int(userInput)
   if guess == answer:
    print("Congratulations! You guessed the correct number. You win!")
    break
   if (i == guesses_allowed - 1):
    print("Sorry, you have run out of guesses. You lose!")
if guess == answer:
  print("Congratulations! You guessed the correct number. You win!")
elif guess < answer:
  print("The number is higher.")
else:
  print("The number is lower.")
if abs(guess - answer) <= 10:
  print("You're warm!")
elif abs(guess - answer) <= 20:
  print("You're getting warmer.")
elif abs(guess - answer) <= 30:
  print("You're cold.")
else:
  print("You're freezing.")
