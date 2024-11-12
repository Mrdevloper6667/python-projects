# Casino type Rock Paper Scissors
import random

print("Welcome Note")
print("Rules and Regulations")

Account_balance = 20000
print("Balance information")
print(Account_balance)

Rock = 0
paper = 1
scissor = 2

# Game loop to stop at 30,000 or 0 balance
while 0 < Account_balance < 30000:
    print("\nRound start")
    
    Player_input = int(input("Rock-0; Paper-1; Scissor-2: "))
    system_input = random.randint(0, 2)
    
    # Tie conditions
    if (Player_input == Rock and system_input == Rock):
        print("You ---Rock")
        print("      ----vs----")
        print("System ---Rock")
        print("Tie")
        print("Try again")
        Account_balance += 0
        print("Account balance:", Account_balance)
        
    elif (Player_input == paper and system_input == paper):
        print("You ---Paper")
        print("      ----vs----")
        print("System ---Paper")
        print("Tie")
        print("Try again")
        Account_balance += 0
        print("Account balance:", Account_balance)
        
    elif (Player_input == scissor and system_input == scissor):
        print("You ---Scissor")
        print("      ----vs----")
        print("System ---Scissor")
        print("Tie")
        print("Try again")
        Account_balance += 0
        print("Account balance:", Account_balance)
        
    # Player win conditions
    elif (Player_input == Rock and system_input == scissor):
        print("You ---Rock")
        print("      ----vs----")
        print("System ---Scissor")
        print("Win")
        Account_balance += 995
        print("Account balance:", Account_balance)
        
    elif (Player_input == paper and system_input == Rock):
        print("You ---Paper")
        print("      ----vs----")
        print("System ---Rock")
        print("Win")
        Account_balance += 995
        print("Account balance:", Account_balance)
        
    elif (Player_input == scissor and system_input == paper):
        print("You ---Scissor")
        print("      ----vs----")
        print("System ---Paper")
        print("Win")
        Account_balance += 995
        print("Account balance:", Account_balance)
        
    # System win conditions
    elif (Player_input == Rock and system_input == paper):
        print("You ---Rock")
        print("      ----vs----")
        print("System ---Paper")
        print("Lose")
        Account_balance -= 1000
        print("Account balance:", Account_balance)
        
    elif (Player_input == paper and system_input == scissor):
        print("You ---Paper")
        print("      ----vs----")
        print("System ---Scissor")
        print("Lose")
        Account_balance -= 1000
        print("Account balance:", Account_balance)
        
    elif (Player_input == scissor and system_input == Rock):
        print("You ---Scissor")
        print("      ----vs----")
        print("System ---Rock")
        print("Lose")
        Account_balance -= 1000
        print("Account balance:", Account_balance)
        
    else:
        print("Wrong input, please try again")
        print("Account balance:", Account_balance)

# Ending condition message
if Account_balance >= 30000:
    print("\nCongratulations! You've reached the goal with a balance of 30,000.")
elif Account_balance <= 0:
    print("\nGame over! Your account balance is zero.")

print("Thanks for playing!")
