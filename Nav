# Jumble game nav menu enabling the user to navigate across various options

import Main

# Welcome the user to the interface

print('''
                +---------------------------------------------------+
                |            Welcome to the Jumble Game             |
                |            Please select your Options.            |
                |            To begin jumble game please add        |
                |            New word set                           |
                |                                                   |
                +---------------------------------------------------+

''')

# Main menu to select different options

def mainmenu():

    b = 1 # While b=1 the following loop wil take place
    while b == 1:

        b1 = 1
        while b1 == 1:

            try:
                chosen_opt = int(input('''
    Select an Option:

    1-Add New word set

    2-Browse a word set

    3-Delete Word set

    4-Play Game

    5-My sorted scores

    6-Exit

    -->> Please select an option:'''))

                b1 = 2

            except ValueError:

                print('Please select an available option by number') #Will display if option chosen not available



# We Begin calling out different functions from the Main Module below which make up our options

# We use an if statement for selecting different function

        if chosen_opt == 1:#Else if for options
            Main.addwords() #To add words


        elif chosen_opt == 2:
            Main.browseoptions() # To browse words


        elif chosen_opt == 3:
            Main.deleteoptions() # To delete words


        elif chosen_opt == 4:
            Main.game() # For the word jumble game



        elif chosen_opt == 5:
            Main.scores()

        elif chosen_opt == 6:
            input("Press ENTER to Exit!") #To exit
            b = 2

        else:
            print('Please select an Available option!!') # If other option is chosen


mainmenu()

