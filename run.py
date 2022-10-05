import os
import random

def create_game_board():
    '''
        Creates empty gameboard 
    '''
    array = []
    for i in range(11):
        row = []
        if i == 0:
            input_row = ' x→ y↓    YOU        VS       COMPUTER     '
            for letter in input_row:
                row.append(letter)
        elif i == 1:
            input_row = '  1 2 3 4 5 6 7 8 9   ▌   1 2 3 4 5 6 7 8 9'
            for letter in input_row:
                row.append(letter)
        else:
            input_row = str(i-1) +'| | | | | | | | | |  ▌  | | | | | | | | | |'
            for letter in input_row:
                row.append(letter)
        
        array.append(row)
    print_table(array)
    return array

def print_table(array):
    '''
        Prints game board in terminal
    '''
    for row in array:
        string = ''
        for white_space in range(18):
                string+=' '
        for i in range(len(row)):
            if i > 24 and row[i] == '■':
                string += ' '
            else:
                string += row[i]
        print(string)

def clear():
    """
    Clears the screen 
    """
    print("\033c")

def validate_input_boat(size, input):
    '''
        Check if input has exactly 3 characters, if its a number, if has correct formating and if it fits on game table. 
    '''
    if len(input) != 3:
        message = '                 Input too long or too short. Try again'
        return False , message
    elif ',' not in input:
        message = '                 Please use a comma between numbers. Try again'
        return False , message
    elif not input.split(',')[0].isnumeric() or not input.split(',')[1].isnumeric():
        message = '                 Input needs to be a number. Try again'
        return False , message
    else:
        input_arr = input.split(',')
        if int(input_arr[0]) == 0  or int(input_arr[1]) == 0:
            message = '                 Outside of grid. Try again'
            return False , message
        if (int(input_arr[0]) + size) > 10:            
            message = '                 Boat is too long for chosen position. Try again'
            return False , message
        
    return True, ' '

def place_computer_boats(table, coords, size):
    '''
        Computer places boats
    '''
    i = 0
    print(coords)
    if (coords[0] + size) > 10: 
        return False
    xaxis = ((coords[0])*2)+24
    yaxis = (coords[1]+1)
    print(xaxis,yaxis)
  
    while i != size:
        if xaxis % 2 == 0:
            
            if table[yaxis][xaxis] == '■':
                return False
                                    
            table[yaxis][xaxis] = '■'
            i+=1
        xaxis+= 1
    
    return True

def add_boats_to_table(table, coords, size):
    '''
        User boats are added to table
    '''
    i = 0
    xaxis = (coords[0])*2
    yaxis = (coords[1]+1)
    while i != size:
        if xaxis % 2 == 0:
            
            if table[yaxis][xaxis] == '■':
                return False
                                    
            table[yaxis][xaxis] = '■'
            i+=1
        xaxis+= 1
    return True

def ask_for_cordinates(game_table, boat_size, boat_img):
    print_table(game_table)
    print()
    print('        Enter x and y coordinates of where you want head of boat to go.') 
    print('       Make sure numbers are separated by a comma. Input example ==> 5,2')
    input_val = input('                      Place your boat of size ' + boat_img + ' ' + boat_size + '\n') 
    validate = validate_input_boat(int(boat_size), input_val)
    return validate, input_val

def place_boats(game_table):
    '''
        Places boats where user chooses

    '''
    boats = [[5, '■■■■■'], [4,'■■■■'], [2, '■■'], [1, '■'], [1, '■']]
    for boat in boats:
        clear()
        validate = ask_for_cordinates(game_table, str(boat[0]), boat[1])

        while validate[0][0] == False:
            clear()
            print(validate[0][1])
            validate = ask_for_cordinates(game_table, str(boat[0]), boat[1])
            
        input_val = validate[1].split(',')
        input_val = [int(input_val[0]) , int(input_val[1])]
        space_taken = add_boats_to_table(game_table, input_val, boat[0])

        while not space_taken:
            clear()
            print('                 Boat space already taken. Try again')
            validate = ask_for_cordinates(game_table, str(boat[0]), boat[1])
            while validate[0][0] == False:
                clear()
                print(validate[0][1])
                validate = ask_for_cordinates(game_table, str(boat[0]), boat[1])

            input_val = validate[1].split(',')
            input_val = [int(input_val[0]) , int(input_val[1])]
            space_taken = add_boats_to_table(game_table, input_val, boat[0])
        
        '''
            Boats placed by computer
        '''
        xaxis = random.randint(1,9)
        yaxis = random.randint(1,9)
        coords = [xaxis, yaxis]
        space_taken =  place_computer_boats(game_table, coords, boat[0])
        while not space_taken:
            clear()
            xaxis = random.randint(1,9)
            yaxis = random.randint(1,9)
            coords = [xaxis, yaxis]
            space_taken = place_computer_boats(game_table, coords, boat[0])
        
    clear()
    print_table(game_table)
    return game_table

def validate_input_shoot(input):
    '''
        Check if input has correct format. 
    '''
    if len(input) != 3:
        message = '                 Input too long or too short. Try again'
        return False , message
    elif ',' not in input:
        message = '                 Please use a comma between numbers. Try again'
        return False , message
    elif not input.split(',')[0].isnumeric() or not input.split(',')[1].isnumeric():
        message = '                 Input needs to be a number. Try again'
        return False , message
    else:
        input_arr = input.split(',')
        if int(input_arr[0]) == 0  or int(input_arr[1]) == 0:
            message = '                 Outside of grid. Try again'
            return False , message
        if int(input_arr[0]) > 10  and int(input_arr[1]) > 10:            
            message = '                 Outside of grid. Try again'
            return False , message
        
    return True, ' '

def check_if_user_won(game_table):
    for row in game_table:
        for i in row[24:len(row)]:
            if i == '■':
                return False
        
    return True

def check_if_pc_won(game_table):
    for row in game_table:    
        for i in row[0:23]:
            if i == '■':
                return False
    return True

def shooting_boats(game_table):
    ''' 
        Computer shooting at enemy 
    '''
    xaxis = random.randint(1,9)
    yaxis = random.randint(1,9)
    xaxis = (xaxis)*2
    yaxis = (yaxis+1) 
    if game_table[yaxis][xaxis] == '■':
        game_table[yaxis][xaxis] = '▢'
    elif game_table[yaxis][xaxis] == '▢' :
        game_table[yaxis][xaxis] =='▢'   
    else:                  
        game_table[yaxis][xaxis] = 'x'

    check_pc = check_if_pc_won(game_table)
    
    if check_pc:
        endScreen(False)

    ''' 
        Asking user to shoot at enemy 
    '''
    clear()
    print_table(game_table)
    print()
    print('        Enter x and y coordinates of where you want to shoot at enemy.') 
    print('       Make sure numbers are separated by a comma. Input example ==> 5,2')
    input_val = input('                          Enter coordinates: ') 
    validate = validate_input_shoot(input_val)

    while validate[0] == False:
        clear()
        print(validate[1])
        print_table(game_table)
        print('        Enter x and y coordinates of where you want to shoot at enemy.') 
        print('       Make sure numbers are separated by a comma. Input example ==> 5,2')
        input_val = input('                          Enter coordinates: ') 
        validate = validate_input_shoot(input_val)

           
    input_val = input_val.split(',')
    input_val = [int(input_val[0]) , int(input_val[1])]
    xaxis = ((input_val[0])*2)+24
    yaxis = (input_val[1]+1) 
    if game_table[yaxis][xaxis] == '■':
        game_table[yaxis][xaxis] = '▢'
    elif game_table[yaxis][xaxis] == '▢' :
        game_table[yaxis][xaxis] =='▢'  
    else:                  
        game_table[yaxis][xaxis] = 'x'
    check = check_if_user_won(game_table)
    
    if check:
        endScreen(True) 
    else:
        print_table(game_table)
        shooting_boats(game_table)
        
    
def endScreen(who_won):
    if who_won:
        clear()
        print(' ')
        print(' ')
        print(' ')
        print(' ')
        print('                     __ __ _____ _____    _ _ _ _____ _____ ')
        print('                    |  |  |     |  |  |  | | | |     |   | |')
        print('                    |_   _|  |  |  |  |  | | | |  |  | | | |')
        print('                      |_| |_____|_____|  |_____|_____|_|___|')
        print(' ')
        print(' ')
        print(' ')
        print(' ')
        print(' ')
        print(' ')
        print(' ')
        print(' ')
        print('Press enter to restart')
        input_val = input(' ') 
    else:
        clear()
        print(' ')
        print(' ')
        print(' ')
        print(' ')
        print('                  __ __ _____ _____    __    _____ _____ _____ ')
        print('                 |  |  |     |  |  |  |  |  |     |   __|_   _|')
        print('                 |_   _|  |  |  |  |  |  |__|  |  |__   | | |  ')
        print('                   |_| |_____|_____|  |_____|_____|_____| |_|  ')
        print(' ')
        print(' ')
        print(' ')
        print(' ')
        print(' ')
        print(' ')
        print(' ')
        print(' ')
        print('Press enter to restart')
        input_val = input(' ') 
    start_game()

def start_screen():
    clear()
    print(' ')
    print(' ')
    print(' ')
    print('                                                                                ')
    print('       __      __       .__                                   __          ')
    print('      /  \    /  \ ____ |  |   ____  ____   _____   ____    _/  |_  ____  ')
    print("      \   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \   \   __\/  _ \ ")
    print('       \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/    |  | (  <_> )')
    print('        \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >   |__|  \____/ ')
    print(' ')
    print('          ______                          _       _     _            ')
    print('         (____  \         _     _        | |     | |   (_)           ')
    print("          ____)  )_____ _| |_ _| |_ _____| |  ___| |__  _ ____   ___ ")
    print("         |  __  ((____ (_   _|_   _) ___ | | /___)  _ \| |  _ \ /___)")
    print("         | |__)  ) ___ | | |_  | |_| ____| ||___ | | | | | |_| |___ |")
    print('         |______/\_____|  \__)  \__)_____)\_|___/|_| |_|_|  __/(___/ ')
    print('                                                         |_|         ')
    print(' ')
    print(' ')
    print('Press enter to start')
    print(' ')
    input_val = input(' ') 


def start_game():

    start_screen()
    game_table = create_game_board()
    game_table = place_boats(game_table)
    winner = shooting_boats(game_table)
start_game()