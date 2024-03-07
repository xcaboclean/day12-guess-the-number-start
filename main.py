#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


from random import randint
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  elif level == "hard":
    return HARD_LEVEL_TURNS
  else:
    print("Difficulty level not available")
    return 0

def number_guesing_game():
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  number = randint(0,100)
  maximum_attempts = 0
  print(f"Pssst, the correct answer is {number}")
  maximum_attempts=set_difficulty()  
  print(f"You have {maximum_attempts} attempts remaining to guess the number.") 
  guess = -1
  while (guess != number) and (turns > 0):
    guess = int(input("Make a guess: "))  
        
    if guess != number:
      turns -=1
      if guess<number:
        print("Too low")
      elif guess > number:
        print("Too high")
      print("Guess again.")
    else:
      print(f"You got it! The answer was {number}.")
      
  if turns == 0:
    print("You've run out of guesses, you lose.")

number_guesing_game()
