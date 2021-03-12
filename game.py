import math 
import sys

digits = []
current_index = 0
game_state = True

with open('digits_of_pi.txt') as f:
    # Read all digits into list without decimal.
    digits = [int(digit) for digit in f.read() if digit != '.']

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
    msg = 'Thank you for playing.'
    if current_index == len(digits):
        msg += ' You correctly guessed all digits.'
    elif current_index > 0:
        msg += f' You correctly guessed {current_index} digits.'
        
    print(msg)
    sys.exit(0)
    
print("Type 'exit' to quit.")
while(game_state):
    if current_index == len(digits):
        end_game()
    try:
        user_guess = input(f'what is the {make_ordinal(current_index+1)} digit of PI: ')
        if user_guess == 'exit':
            end_game()
        print(check_guess(int(user_guess)))
    except ValueError:
        # User did not enter a valid integer.
        print('Please enter a valid integer')
