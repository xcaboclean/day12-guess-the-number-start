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
    return 0


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = randint(0,100)
attempts = 0
print(f"Pssst, the correct answer is {number}")


if difficulty == 'easy':
  attempts = 5
elif difficulty == 'hard':
  attempts = 10
else:
  attempts = 0
  
while attempts:
  print("")

 
