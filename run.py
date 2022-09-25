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
        for i in row:
            string += i
        print(string)

def validate_input_boat(size, input):
    '''
        Check if inpit has exactly 3 characters, if its a number, if has correct formating and if it fits on game table. 
    '''

    '-------------------------------------- CHECK FOR 0 --------------------------------------------------------------'
    if len(input) != 3:
        message = 'Input too long or too short. Try again'
        return False , message
    elif ',' not in input:
        message = 'Please use a comma between numbers. Try again'
        return False , message
    elif not input.split(',')[0].isnumeric() or not input.split(',')[1].isnumeric():
        message = 'Input needs to be a number. Try again'
        return False , message
    else:
        input_arr = input.split(',')
        print(input_arr[0], size)
        if (int(input_arr[0]) + size) > 10:            
            message = 'Boat is too long for chosen position. Try again'
            return False , message
        
    return True, ' '

def place_computer_boats(table, coords, size):
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
    #
    print_table(game_table)
    print()
    print('Enter x and y coordinates of where you want head of boat to go.') 
    print('Make sure numbers are separated by a comma. Input example ==> 5,2')
    input_val = input('Place your boat of size ' + boat_img + ' ' + boat_size + '\n') 
    validate = validate_input_boat(int(boat_size), input_val)

    return validate, input_val


def place_boats(game_table):
    '''
        Places boats where user chooses
    '''
    boats = [[5, '■■■■■'], [4,'■■■■'], [2, '■■'], [1, '■'], [1, '■'] ]
    for boat in boats:
        #os.system('cls||clear')
        validate = ask_for_cordinates(game_table, str(boat[0]), boat[1])

        while validate[0][0] == False:
            #os.system('cls||clear')
            print(validate[0][1])
            validate = ask_for_cordinates(game_table, str(boat[0]), boat[1])
            
        input_val = validate[1].split(',')
        input_val = [int(input_val[0]) , int(input_val[1])]
        space_taken = add_boats_to_table(game_table, input_val, boat[0])

        while not space_taken:
            #os.system('cls||clear')
            print('Boat space already taken. Try again')
            validate = ask_for_cordinates(game_table, str(boat[0]), boat[1])
            while validate[0][0] == False:
                #os.system('cls||clear')
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
            #os.system('cls||clear')
            xaxis = random.randint(1,9)
            yaxis = random.randint(1,9)
            coords = [xaxis, yaxis]
            space_taken = place_computer_boats(game_table, coords, boat[0])
        
    '''os.system('cls||clear')  '''
    print_table(game_table)

def start_game():
    '''print()
    print(' y↓ x→    YOU        VS       COMPUTER     ')
    print('  1 2 3 4 5 6 7 8 9   ▌   1 2 3 4 5 6 7 8 9')
    print('1| | | | | | | | | |  ▌  | | | | | | | | | |')
    print('2| | | | | | | | | |  ▌  | | | | | | | | | |')
    print('3| | | | | | | | | |  ▌  | | | | | | | | | |')
    print('4| | | | | | | | | |  ▌  | | | | | | | | | |')
    print('5|■|■|▢| | | | | | |  ▌  | | | | | | | | | |')
    print('6| | | | | | | | | |  ▌  | | | | | | | | | |')
    print('7| | | | | | | | | |  ▌  | | | | | | | | | |')
    print('8| | | | | | | | | |  ▌  | | | | | | | | | |')
    print('9| | | | | | | | | |  ▌  | | | | | | | | | |')
    print()'''

    game_table = create_game_board()
    game_table = place_boats(game_table)

start_game()