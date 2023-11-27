#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
print("Welcome to the Number Guessing Name.\n")
game_level = input("You will have 5 chances for easy and 10 chances for hard.\nChoose a level: 'easy' or 'hard': ")
random_number = random.randint(1, 100)

def level():
    guess = int(input("Guess a number: "))
    if guess == random_number:
      print("You Got it.")
    elif guess > random_number:
      print("Too High")
    elif guess < random_number:
      print("Too Low")
    else:
      print("Number not in range.")
    
if game_level == 'easy':
  for i in range(1, 11):
    level()
    print(f"You still have {10-i} chances left.")

elif game_level == 'hard':
  for i in range(1, 6):
    level()
    print(f"You still have {5 - i} chances left.")
  