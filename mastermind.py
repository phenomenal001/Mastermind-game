import random

COLORS = ["R","G","B","Y","W","O"]  #list of color
Tries = 10 # number of attempt
code_length = 4

def generate_code():
    code = []
    for i in range(code_length):
        color = random.choice(COLORS)
        code.append(color)
    return code

def guess_code():

    while True:
        guess = input("Guess: ").upper().split()

        if len(guess) != code_length:
            print(f"You must guess only {code_length} color")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"Invslide color: {color}. Try again.")
                break
            
        else:
            break
    return guess

def check_code(guess,real_code):
    color_count = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_count:
            color_count[color] = 0
        color_count[color] += 1

    for guess_color, real_color in zip(guess,real_code):
        if guess_color == real_color:
            correct_pos +=1
            color_count[guess_color] -=1

    for guess_color, real_color in zip(guess,real_code):
        if guess_color in color_count and color_count[guess_color] > 0:
            incorrect_pos +=1
            color_count[guess_color] -=1

    return correct_pos, incorrect_pos

def game():
    print(f"Welcome to mastermind, you have {Tries} to guess the code...")
    print("The valid colors are",*COLORS)
    code = generate_code()
    for attempts in range(1, Tries+1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess,code)

        if correct_pos == code_length:
            print(f"You guessed the code in {attempts} tries!")
            break
        print(f"Correct positions: {correct_pos} | Incorrect postions: {incorrect_pos}")
    
    else:
        print("You ran out tries, the code was:", *code)
    
if __name__ == "__main__":
    game()