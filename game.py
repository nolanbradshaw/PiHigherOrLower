import math 

digits = []
current_index = 0
game_state = True

with open('digits_of_pi.txt') as f:
    # Read all digits into list without decimal
    digits = [int(x) for x in f.read() if x != '.']

def make_ordinal(n):
    suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    return str(n) + suffix

def check_guess(guess):
    global current_index
    if guess < int(digits[current_index]):
        return 'Higher'
    elif guess > int(digits[current_index]):
        return 'Lower'
    else:
        current_index += 1
        return 'Correct!'

while(game_state):
    try:
        user_guess = int(input(f'what is the {make_ordinal(current_index+1)} digit of PI: '))
        print(check_guess(user_guess))
    except ValueError:
        # User did not enter a valid integer
        print('failed')