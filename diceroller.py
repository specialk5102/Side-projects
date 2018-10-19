import random
import sys

# D4
def d4():
        print('''You have selected to roll d4('s)''')
        total_dice_roll = 0 # Setting total amt rolled to 0
        amount_to_roll = int(input('How many d4 dice would you like to roll:')) # Asks how many dice to roll
        
        while amount_to_roll < 1: # Input validation for amt of dice
                print('That is not a valid option. Please enter in a number above 0')
                amount_to_roll = int(input('How many d4 dive would you like to roll:'))
    
        for x in range(amount_to_roll): # Dice rolling loop
                dice_roll = random.randint(1,4) # Rolling dice 1-4
                total_dice_roll += dice_roll # Adding dice rolls

        print('You rolled', amount_to_roll, 'dice, which totaled out to', total_dice_roll) # Print statement with amt rolled and total amt

# D6
def d6():
        print(''''You have selected to roll d6('s)''')
        total_dice_roll = 0 # Setting total amt rolled to 0
        amount_to_roll = int(input('How many d6 would you like to roll:')) # Asks how many dice to roll
        
        while amount_to_roll < 1: # Input validation for amt of dice
                print('That is not a valid option. Please enter in a number above 0')
                amount_to_roll = int(input('How many d6 dice would you like to roll:'))

        for x in range(amount_to_roll): # Dice rolling loop
                dice_roll = random.randint(1,6) # Rolling dice 1-6
                total_dice_roll += dice_roll # Adding dice rolls for output

        print('You rolled', amount_to_roll, 'dice, which totaled out to', total_dice_roll) # Print statement with amt rolled and total amt

# D8
def d8():
        print('''You have selected to roll d8('s)''')
        total_dice_roll = 0 # setting total amt rolled to 0
        amount_to_roll = int(input('How many d8 would you like to roll:')) # Asks how many dice to roll

        while amount_to_roll < 1: # Input validation for amt of dice
                print('That is not a valid option. Please enter in a number above 0')
                amount_to_roll = int(input('How many d8 would you like to roll:'))
        
        for x in range(amount_to_roll): # Dice rolling loop
                dice_roll = random.randint(1,8) # Rolling dice 1-8
                total_dice_roll += dice_roll # Adding rice rolls for output

        print('You rolled', amount_to_roll, 'dice, which totaled out to', total_dice_roll) # Print statement with amt rolled and total amt

# D10
def d10():
        print('''You have selected to roll d10('s)''')
        total_dice_roll = 0 # setting total amt rolled to 0
        amount_to_roll = int(input('How many d10 would you like to roll:')) # Asks how many dice to roll

        while amount_to_roll < 1: # Input validation for amt of dice
                print('That is not a valid option. Please enter in a number above 0')
                amount_to_roll = int(input('How many d10 would you like to roll:'))
        
        for x in range(amount_to_roll): # Dice rolling loop
                dice_roll = random.randint(1,10) # Rolling dice 1-10
                total_dice_roll += dice_roll # Adding rice rolls for output

        print('You rolled', amount_to_roll, 'dice, which totaled out to', total_dice_roll) # Print statement with amt rolled and total amt

# D12
def d12():
        print('''You have selected to roll d12('s)''')
        total_dice_roll = 0 # setting total amt rolled to 0
        amount_to_roll = int(input('How many d12 would you like to roll:')) # Asks how many dice to roll

        while amount_to_roll < 1: # Input validation for amt of dice
                print('That is not a valid option. Please enter in a number above 0')
                amount_to_roll = int(input('How many d12 would you like to roll:'))
        
        for x in range(amount_to_roll): # Dice rolling loop
                dice_roll = random.randint(1,12) # Rolling dice 1-12
                total_dice_roll += dice_roll # Adding rice rolls for output

        print('You rolled', amount_to_roll, 'dice, which totaled out to', total_dice_roll) # Print statement with amt rolled and total amt

# D20
def d20():
        print('''You have selected to roll d20('s)''')
        total_dice_roll = 0 # setting total amt rolled to 0
        amount_to_roll = int(input('How many d20 would you like to roll:')) # Asks how many dice to roll

        while amount_to_roll < 1: # Input validation for amt of dice
                print('That is not a valid option. Please enter in a number above 0')
                amount_to_roll = int(input('How many d20 would you like to roll:'))
        
        for x in range(amount_to_roll): # Dice rolling loop
                dice_roll = random.randint(1,20) # Rolling dice 1-20
                total_dice_roll += dice_roll # Adding rice rolls for output

        print('You rolled', amount_to_roll, 'dice, which totaled out to', total_dice_roll) # Print statement with amt rolled and total amt

# D100
def d100():
        print('''You have selected to roll d100('s)''')
        total_dice_roll = 0 # setting total amt rolled to 0
        amount_to_roll = int(input('How many d100 would you like to roll:')) # Asks how many dice to roll

        while amount_to_roll < 1: # Input validation for amt of dice
                print('That is not a valid option. Please enter in a number above 0')
                amount_to_roll = int(input('How many d100 would you like to roll:'))
        
        for x in range(amount_to_roll): # Dice rolling loop
                dice_roll = random.randint(1,100) # Rolling dice 1-100
                total_dice_roll += dice_roll # Adding rice rolls for output

        print('You rolled', amount_to_roll, 'dice, which totaled out to', total_dice_roll) # Print statement with amt rolled and total amt

def main():
        while True:
                print('Hello and welcome to the Dice Roller Simulator') # Main menu of dice rolling program
                print('(1) D4')
                print('(2) D6')
                print('(3) D8')
                print('(4) D10')
                print('(5) D12')
                print('(6) D20')
                print('(7) D100')
                print('(8) Quit')
                selection = int(input('Please select which dice you would like to roll from the menu:')) # Selection

                if selection == 1: # calls D4 dice function
                        d4()

                elif selection == 2: # Calls D6 dice function
                        d6()
        
                elif selection == 3: # Calls D8 dice function
                        d8()

                elif selection == 4: # Calls D10 dice function
                        d10()

                elif selection == 5: # Calls D12 dice function
                        d12()

                elif selection == 6: # Calls D100 dice function
                        d20()

                elif selection == 7: # Calls D100 dice function
                        d100()

                elif selection == 8: # Quits program. Exits loop
                        print('Thank you for using my program')
                        print('Good-bye!')
                        sys.exit()

                else: # Input validation for menu selection
                        print('That is not a valid option. Please select an option from the menu')
                        print('(1) D4')
                        print('(2) D6')
                        print('(3) D8')
                        print('(4) D10')
                        print('(5) D12')
                        print('(6) D20')
                        print('(7) D100')
                        print('(8) Quit')
                        selection = int(input('Please select which dice you would like to roll from the menu:'))

main()