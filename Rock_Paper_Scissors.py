#Rock, Paper, Scissors Game
import random, sys

print("Rock, Paper, Scissors")

wins = 0
loses = 0
ties = 0

while True: #The main game loop
    print('%s wins, %s loses, %s ties' % (wins, loses, ties))
    
    while True:
        print("Enter your Move: 'r' for Rock, 'p' for Paper, 's' for Scissors 'q' for quit.")
        userInput = input()
        if userInput == 'q':
            sys.exit() #quits the game
        if userInput == 'r' or userInput == 'p' or userInput == 's':
            break
        print("Type 'r' for Rock, 'p' for Paper, 's' for Scissors 'q' for quit.")
        
    # For Player Choice
    
    if userInput == 'r':
        print("Rock versus: ")
    elif userInput == 'p':
        print("Paper versus")
    elif userInput == 's':
        print("Scissors versus: ")
    
    #For computer choice
    
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerChoice = "r"
        print("Rock")
        
    elif randomNumber == 2:
        computerChoice = "p"
        print("Paper")
        
    elif randomNumber == 3:
        computerChoice = "s"
        print("Scissors")
        
    if userInput == computerChoice:
        print("It is a tie.")
        ties = ties + 1
        
    elif userInput == 'p' and computerChoice == 'r':
        print("You Win!")
        wins = wins + 1
    elif userInput == 'r' and computerChoice == 's':
        print("You Win!")
        wins = wins + 1
    elif userInput == 's' and computerChoice == 'p':
        print("You Win!")
        wins = wins + 1
    else:
        print("You Lose!")
        loses = loses + 1
        
        
        
    