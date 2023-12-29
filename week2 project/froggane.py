import random

def display_game(frog_positions):
    print("Current Display:")
    print("[ 0 ,  1 ,  2 ,  3 ,  4 ,  5 ,  6 ]")
    print(frog_positions)

def initial_setup():
    frogs = ['G', 'G', 'G', '-', 'B', 'B', 'B']
    random.shuffle(frogs)
    return frogs

def make_move(frog_positions, position):
    frog = frog_positions[position]

    if frog == '-':
        print("Invalid move! Please select a frog.")
        return False

    if position < 0 or position > 6:
        print("Invalid move! Position should be between 0 and 6.")
        return False

    if position == 0 and frog == 'B':
        print("Invalid move! Brown frogs cannot move left.")
        return False

    if position == 6 and frog == 'G':
        print("Invalid move! Green frogs cannot move right.")
        return False

    if frog == 'G':
        if frog_positions[position + 1] == 'B' and frog_positions[position + 2] == '-':
            frog_positions[position], frog_positions[position + 2] = frog_positions[position + 2], frog_positions[position]
            return True
    elif frog == 'B':
        if frog_positions[position - 1] == 'G' and frog_positions[position - 2] == '-':
            frog_positions[position], frog_positions[position - 2] = frog_positions[position - 2], frog_positions[position]
            return True

    print("Invalid move! Check the rules.")
    return False

def is_game_solved(frog_positions):
    return frog_positions == ['B', 'B', 'B', '-', 'G', 'G', 'G']

def frog_leap_game():
    frog_positions = initial_setup()

    while not is_game_solved(frog_positions):
        display_game(frog_positions)

        move = input("Enter the position of the frog you want to move (0-6, q to quit): ")
        
        if move.lower() == 'q':
            print("Quitting the game.")
            break

        try:
            move = int(move)
            if 0 <= move <= 6:
                if make_move(frog_positions, move):
                    print("Move successful!")
                else:
                    print("Try again.")
            else:
                print("Invalid move! Position should be between 0 and 6.")
        except ValueError:
            print("Invalid input! Please enter a valid position or 'q' to quit.")

    if is_game_solved(frog_positions):
        print("Congratulations! You solved the puzzle.")

if __name__ == "_main_":
    frog_leap_game()