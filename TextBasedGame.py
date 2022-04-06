                                    # Jovi Billiot

import sys, time  # import sys and time to add some output effects


def intro():  # define function to output introduction message
    time.sleep(1)  # delay intro by one second
    intro_message = 'It\'s time for bed, but you have a cranky baby at home.'\
                    '\nYou are at risk of staying up all night if you don\'t retrieve all the items around the house'\
                    ' to calm the baby.' \
                    '\nYou are going to move through various rooms around the house while picking up items before ' \
                    'you go into the baby\'s room to calm him down and put him to sleep.' \
                    '\nYou must be careful' \
                    ' because if you arrive in the baby\'s room before you retrieve all SIX items you will have a very'\
                    ' VERY long night.' \
                    '\nYou will move from room to room through EIGHT rooms by saying \'Go North, Go South, Go East,' \
                    ' and Go West.\n'
    for char in intro_message: # loops each word in intro message
        sys.stdout.write(char)  # prints each word one at a time
        sys.stdout.flush()    # runs words through buffer
        if char == '\n':
            time.sleep(1)   # Prints new line after one second
        else:
            time.sleep(0.05)  # prints each word .05 seconds apart


def invalid():  # define function to print error statement when invalid input
    if player_input == 'Go North' or player_input == 'Go South' or player_input == 'Go East' or player_input == \
            'Go West':
        print()
    else:
        print('\nError! Invalid input! \nPleas say, \" Go North, Go South, Go East, or Go West.\"')


def bye(): # define function to quit game if player inputs 'Exit'
    if player_input == 'Exit':
        if input('Are you sure you want to quit? (Yes/No)\n') == 'Yes':  # asks player if they really want to quit
            print('Thanks for playing. \n    GOODBYE!')
            exit()  # If player selects 'Yes' then game exits program with a message. if 'No' the game continues
        return player_input


def comeback():  # define function for when player declines to pick up item to same time and cleaner code.
    print('You\'ll have to come back for it.')


def update(location, inventory):  # define function to return the current location and items in the inventory
    for char in '\nYou are in the {}.\n'.format(location):
        sys.stdout.write(char)  # prints each word .1 seconds apart
        sys.stdout.flush()
        time.sleep(.1)
    time.sleep(.5)    # .5 second delay between printing location and inventory
    print('Inventory : {}'.format(inventory))
    print('-' * 160)   # prints '_' 160 times to make output neater and easier to read
    return location, inventory


def welcome():  # Define output to welcome player and ask if they want to play. Display text graphic if 'Yes'
    welcome_message = 'Welcome, Would you like to play? (Yes/No)\n'
    for i in welcome_message:
        sys.stdout.write(i)  # prints each word .025 seconds apart
        sys.stdout.flush()
        time.sleep(.025)
    if input() == 'Yes':
        print(' ' * 5, '*' * 24)
        print(' ' * 5, '*', ' ' * 20, '*')
        print(' ' * 5, '*', ' ' * 20, '*')
        print(' ' * 5, '*', 'WELCOME TO THE GAME!', '*')    # print welcoming text graphic
        print(' ' * 5, '*', ' ' * 20, '*')
        print(' ' * 5, '*', ' ' * 20, '*')
        print(' ' * 5, '*' * 24)
        print('-' * 160)
        print()
        intro()  # calls intro function if player inputs 'Yes'
    elif input() == 'No':
        print('Too Bad...')
        time.sleep(1)
        exit()    # ends program if player inputs 'No'


def lose():  # define function for if player loses the game
    for char in 'You don\'t have all the items to calm the baby. You\'re in for a very VERY long night!' \
                '\nGAME OVER!\n':
        sys.stdout.write(char)
        sys.stdout.flush()   # prints each word .1 seconds at a time
        time.sleep(.1)
    exit()     # exit program


def win():  # define function for if player wins the game
    for char in 'CONGRATULATIONS, YOU DID IT! \nYou retrieved all the items to calm the baby! \n' \
                'Now that he\'s fast asleep, get a some rest. \nYOU EARNED IT!':
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.1)   # prints each word .1 seconds at a time.
    exit()

# nest dictionary of rooms, directions, and their items
rooms = {

        'Foyer': {'West': 'Library'},
        'Library': {'East': 'Foyer', 'South': 'Living Room', 'item': 'Book'},
        'Living Room': {'North': 'Library', 'West': 'Nursery', 'East': 'Kitchen', 'South': 'Master Bedroom',
                        'item': 'Pacifier'},
        'Nursery': {'East': 'Living Room', 'item': 'BABY'},
        'Kitchen': {'West': 'Living Room', 'North': 'Pantry', 'item': 'Bottle'},
        'Pantry': {'South': 'Kitchen', 'item': 'Formula'},
        'Master Bedroom': {'North': 'Living Room', 'East': 'Bathroom', 'item': 'Diaper'},
        'Bathroom': {'West': 'Master Bedroom', 'item': 'Baby Wipes'}

    }

welcome()  # calls welcome function to ask player if they want to play
location = 'Foyer'  # starting location
inventory = []  # inventory starts as an empty list
# start a loop that will be infinite as long as the location can be found in the dict rooms' keys
while location in rooms.keys():
    print('_' * 160)  # print '_' 160 times for more cleaner output
    time.sleep(1)  # one second delay
    update(location, inventory)  # prints current location and current inventory
    time.sleep(.5)  # .5 second delay

    for char in '\nWhich direction would you like to go?\n':
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    player_input = input()  # player input inside loop for new input in each room

    bye()   # calls bye function for if played inputs 'Exit' at any point during game to quit game
    invalid()  # Calls in invalid function for when player inputs invalid direction

    if location == 'Foyer':   # nested if statements fpr when the player is in given location
        if player_input == 'Go West':   # Nested if statements when player inputs valid location
            if 'Book' not in inventory:  # if statements to allow player to add the item if they want to.
                if input('You found the Book in the Library. \nDo you want to pick it up? (Yes/No) \n') == 'Yes':
                    print('The Book was added to your inventory.')
                    inventory.append('Book') # adds item to inventory
                else:
                    comeback()  # if player declines item player is notified to come back by calling comeback() function
            location = 'Library'  # changes location to another room
            # locations that go nowhere are placed in an if/elif line together. player notified no place to go and retry
        elif player_input == 'Go North' or player_input == 'Go East' or player_input == 'Go South':
            print('There is nothing but a wall there.\nChoose another direction.')
        continue  # continue to beginning of loop to avoid new location to run a another if statement
    if location == 'Library':
        if player_input == 'Go North' or player_input == 'Go West':
            print('There is nothing but a wall there.\nChoose another direction.')
        if player_input == 'Go East':
            print('You\'re back in the Foyer.')
            location = 'Foyer'
        elif player_input == 'Go South':
            if 'Pacifier' not in inventory:
                if input('You found the Pacifier in the Living Room. \nDo you want to pick it up?(Yes/No)\n') == 'Yes':
                    print('The Pacifier has been added to your inventory.')
                    inventory.append('Pacifier')
                else:
                    comeback()
            location = 'Living Room'
        continue
    if location == 'Living Room':
        if player_input == 'Go North':
            print('You\'re back in the Library.')
            if 'Book' not in inventory:
                if input('Do you want to retrieve the book now?(Yes/No)\n') == 'Yes':
                    print('The Book has been added to your inventory.')
                    inventory.append('Book')
                else:
                    comeback()
            location = 'Library'
            continue
        if player_input == 'Go East':
            if 'Bottle' not in inventory:
                if input('You found the Bottle in the Kitchen. \nDo you want to pick it up?(Yes/No)\n') == 'Yes':
                    print('The Bottle has been added to your inventory.')
                    inventory.append('Bottle')
                else:
                    comeback()
            location = 'Kitchen'
            continue
        if player_input == 'Go South':
            if 'Diaper' not in inventory:
                if input('You found the Diaper in the Master Bedroom \nDo you want to pick it up?(Yes/No)\n') == 'Yes':
                    print('The Diaper has been added to your inventory.')
                    inventory.append('Diaper')
                else:
                    comeback()
            location = 'Master Bedroom'
            continue
        if player_input == 'Go West':
            print('_' * 160)
            for char in 'YOU\'RE IN THE ROOM WITH THE BABY! \nHe so upset! \nSure hope you have everything you need.\n':
                sys.stdout.write(char)
                sys.stdout.flush()  # inform player they are in the room withe the baby printing one word at a time
                time.sleep(.1)      # .1 seconds apart
            if len(inventory) != 6:  # if player does not have all 6 items when entering nursery the player loses
                print('_' * 160)
                time.sleep(2)
                lose()  # calls lose function when player has < 6 items when enters nursery; ends game with message
            if len(inventory) == 6:  # if player has all 6 items when enters the nursery then win function is called
                print('_' * 160)
                time.sleep(2)
                win()  # calls win function when player has all 6 items when enters nursery; ends game with message

    if location == 'Kitchen':
        if player_input == 'Go South' or player_input == 'Go East':
            print('There is nothing but a wall there.\nChoose another direction.')
        if player_input == 'Go West':
            print('You\'re back in the Living Room.\n')
            if 'Pacifier' not in inventory:
                if input('Do you want to retrieve the Pacifier now?(Yes/No)\n') ==  'Yes':
                    print('The Pacifier as been added to your inventory.')
                    inventory.append('Pacifier')
                else:
                    comeback()
            location = 'Living Room'
        if player_input == 'Go North':
            if 'Formula' not in inventory:
                if input('You found the Formula in the Pantry. \nDo you want to pick it up?(Yes/No)\n') == 'Yes':
                    print('The Formula has been added to your inventory.')
                    inventory.append('Formula')
                else:
                    comeback()
            location = 'Pantry'
            continue

    if location == 'Pantry':
        if player_input == 'Go East' or player_input == 'GO North' or player_input == 'Go West':
            print('There is nothing but a wall there.\nChoose another direction.')
        if player_input == 'Go South':
            print('You are back in the Kitchen.\n')
            if 'Bottle' not in inventory:
                if input('Do you want to retrieve the Bottle now?(Yes/No)\n') == 'Yes':
                    print('The Bottle has been added to your inventory.')
                    inventory.append('Bottle')
                else:
                    comeback()
            location = "Kitchen"
            continue

    if location == 'Master Bedroom':
        if player_input == 'Go West' or player_input == 'Go South':
            print('There is nothing but a wall there.\nChoose another direction.')
        if player_input == 'Go North':
            print('You\'re back in the Living Room.\n')
            if 'Pacifier' not in inventory:
                if input('Do you want to retrieve the Pacifier now?(Yes/No)\n') == 'Yes':
                    print('The Pacifier as been added to your inventory.')
                    inventory.append('Pacifier')
                else:
                    comeback()
            location = 'Living Room'
            continue

        if player_input == 'Go East':
            if 'Baby Wipes' not in inventory:
                if input('You found the Baby Wipes in the Bathroom. \nDo you want to pick them up?(Yes/No)\n') == 'Yes':
                    print('The Baby Wipes have been added to your inventory.')
                    inventory.append('Baby Wipes')
                else:
                    comeback()
            location = 'Bathroom'
        continue

    if location == 'Bathroom':
        if player_input == 'Go North' or player_input == 'Go South' or player_input == 'Go East':
            print('There is nothing but a wall there.\nChoose another direction.')
        if player_input == 'Go West':
            print('You\'re back in the Master Bedroom.')
            if 'Diaper' not in inventory:
                if input('Do you want to retrieve the Diaper now?(Yes/No)\n') == 'Yes':
                    print('The Diaper has been added to your inventory.')
                    inventory.append('Diaper')
                else:
                    comeback()
            location = 'Master Bedroom'
        continue

    





