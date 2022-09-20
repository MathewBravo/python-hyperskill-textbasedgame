def normalize_selection(selection: str) -> int:
    selection = str(selection).lower()
    if selection == "1" or selection == "start":
        return 1
    elif selection == "2" or selection == "load":
        return 2
    elif selection == "3" or selection == "quit":
        return 3
    else:
        print("Unknown input! Please enter a valid one.")
        return 0


def start_new_game():
    print("Starting a new game...")

def load_game():
    print("No save data found!")

def quit_game():
    print("Goodbye!")

def process_menu_selection(selection: int):
    if selection == 1:
        start_new_game()
    if selection == 2:
        load_game()
    if selection == 3:
        quit_game()


def main_menu() -> int:
    print("""
1- Press key '1' or type 'start' to start a new game
2- Press key '2' or type 'load' to load your progress
3- Press key '3' or type 'quit' to quit the game""")
    menu_selection = input()
    if normalize_selection(menu_selection) == 0:
        while normalize_selection(menu_selection) == 0:
            menu_selection = input()
            choice = normalize_selection(menu_selection)
    else:
        choice = normalize_selection(menu_selection)
    return choice


# write your code here
if __name__ == '__main__':
    print("***Welcome to the Journey to Mount Qaf*** ")
    choice = main_menu()
    process_menu_selection(choice)