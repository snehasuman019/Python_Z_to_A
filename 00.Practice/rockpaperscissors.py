"""
Workflow of project
1. input from user(Rock Paper Scissors)
2. Computer choice (computer will choose randomly from Rock Paper Scissors)
3. result print

Cases:
A- Rock
Rock - Rock = tie
Rock - Paper = Paper wins
Rock - Scissors = Rock wins

B- Paper
Paper - Rock = Paper wins
Paper - Paper = tie
Paper - Scissors = Scissors wins

C- Scissors
Scissors - Rock = Rock wins
Scissors - Paper = Scissors wins
Scissors - Scissors = tie

"""

import random
item_list = ['Rock', 'Paper', 'Scissors']
user_choice = input("Enter your move = Rock, Paper, Scissors = ")
computer_choice = random.choice(item_list)
print(f"User choice : {user_choice}, computer choice : {computer_choice}")

if computer_choice == user_choice:
    print("Both chooses same : It's a tie")
elif user_choice == 'Rock':
    if computer_choice == 'Paper':
        print("Paper covers rock , So Computer wins")
    else:
        print("Rock smashes Scissor = You win")
elif user_choice == 'Paper':
    if computer_choice == 'Scissors':
        print("Scissors cuts Paper , So Computer wins")
    else:
        print("Paper covers Rock = You win")
elif user_choice == 'Scissors':
    if computer_choice == 'Rock':
        print("Rock smashes Scissors , So Computer wins")
    else:
        print("Scissors cuts Paper = You win")
else:
    print("Invalid input from user , Please choose from Rock, Paper, Scissors")
    