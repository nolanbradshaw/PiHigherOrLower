import math 
import sys

digits = []
current_index = 0
game_state = True

with open('digits_of_pi.txt') as f:
    # Read all digits into list without decimal.
    digits = [int(x) for x in f.read() if x != '.']

def get_current_pi():
    # Read current correctly guessed digits into str.
    pi_str = ''.join([str(digits[x]) for x in range(0, current_index)])
    pi_str = pi_str[0] + '.' + pi_str[1:]  
    return pi_str

def make_ordinal(n):
    # Add suffixes to numbers
    suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    return str(n) + suffix

def check_guess(guess):
    global current_index
    if guess < int(digits[current_index]):
        return 'HIGHER'
    elif guess > int(digits[current_index]):
        return 'LOWER'
    else:
        current_index += 1
        current_pi = get_current_pi()
        return f'CORRECT! {current_pi}'

def end_game():
    if current_index == 0:
        msg = 'Thank you for playing.'
    else:
        msg = 'Thank you for playing. You correctly guessed {current_index+1} digits.'
        
    print(msg)
    sys.exit(0)
    
print("Type 'cancel' to exit.")
while(game_state):
    try:
        user_guess = input(f'what is the {make_ordinal(current_index+1)} digit of PI: ')
        if user_guess == 'cancel':
            end_game()
        print(check_guess(int(user_guess)))
    except ValueError:
        # User did not enter a valid integer.
        print('Please enter a valid integer')