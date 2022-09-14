import os

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

    'CHECK FOR 0'
    if len(input) != 3:
        message = 'Input too long or too short'
        return False , message
    elif ',' not in input:
        message = 'Please use a comma between numbers'
        return False , message
    elif not input.split(',')[0].isnumeric() or not input.split(',')[1].isnumeric():
        message = 'Input needs to be a number'
        return False , message
    else:
        input_arr = input.split(',')
        if (int(input_arr[1]) + size) >= 9:            
            message = 'Boat is too long for chosen position'
            return False , message
    
    return True, ' '

def place_computer_boats():
    print('hi')

def add_boats_to_table(table, coords, size):
    
    i = 0
    while i != size:
        xaxis = coords[0]+1+i
        yaxis = coords[1]+1
        if xaxis % 2 == 0:
            table[yaxis][xaxis] = '■'
            i+=1
        else:
            i+=1
            size+=1
        

def place_boats(game_table):
    '''
        Places boats where user chooses
    '''
    boats = [[5, '■■■■■'], [4,'■■■■'], [2, '■■'], [1, '■'], [1, '■'] ]
    for boat in boats:
        #os.system('cls||clear')
        #
        print_table(game_table)
        print()
        print('Enter x and y coordinates of where you want head of boat to go.') 
        print('Make sure numbers are separated by a comma. Input example ==> 5,2') 
        input_val = input('Place your boat of size ' + str(boat[0]) + ' ' + boat[1] + '\n')
        
        validate = validate_input_boat(boat[0], input_val)
        while validate[0] == False:
            os.system('cls||clear')
            print_table(game_table)
            print()
            print('Enter x and y coordinates of where you want head of boat to go.') 
            print('Make sure numbers are separated by a comma. Input example ==> 5,2')
            print(validate[1])
            input_val = input('Place your boat of size ' + str(boat[0]) + ' ' + boat[1] + '\n')
            validate = validate_input_boat(boat[0], input_val)

        input_val = input_val.split(',')
        input_val = [int(input_val[0]) , int(input_val[1])]
        add_boats_to_table(game_table, input_val, boat[0])
        
    
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