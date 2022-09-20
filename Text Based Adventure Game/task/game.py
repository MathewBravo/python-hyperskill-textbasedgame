from player import Player

player = Player()
def normalize_selection(selection: str) -> int:
    selection = str(selection).lower()
    one_value = ["1", "start", "easy"]
    two_value = ["2", "load", "medium"]
    three_value = ["3", "quit", "hard"]

    if selection in one_value:
        return 1
    elif selection in two_value:
        return 2
    elif selection in three_value:
        return 3
    else:
        print("Unknown input! Please enter a valid one.")
        return 0


def lives_from_difficulty(difficulty) -> int:
    if difficulty == 1:
        player.difficulty = "Easy"
        return 5
    elif difficulty == 2:
        player.difficulty = "Medium"
        return 3
    elif difficulty == 3:
        player.difficulty = "Hard"
        return 1


def start_new_game():
    global choice
    print("Starting a new game...")
    user_name = input("Enter a user name to save your progress or type '/b' to go back > ")
    if user_name == "/b":
        launch_game()
    else:
        player.user_name = user_name
    print("Create your character:")
    player.name = input("1- Name ").capitalize()
    player.species = input("2- Species ").capitalize()
    player.gender = input("3- Gender ").capitalize()
    print("Pack your bag for the journey:")
    player.snack = input("1- Favourite Snack ").capitalize()
    player.weapon = input("2- A weapon for the journey").capitalize()
    player.tool = input("3- A traversal tool").capitalize()
    print("Choose your difficulty:")
    print("""1- Easy
2- Medium
3- Hard""")
    difficulty_selection = input()
    if normalize_selection(difficulty_selection) == 0:
        while normalize_selection(difficulty_selection) == 0:
            difficulty_selection = input()
            choice = normalize_selection(difficulty_selection)
    else:
        choice = normalize_selection(difficulty_selection)
    player.lives = lives_from_difficulty(choice)
    start_journey()


def start_journey():
    print("Good luck on your journey!")
    print(f"Your character: {player.name}, {player.species}, {player.gender}")
    print(f"Your inventory: {player.snack}, {player.weapon}, {player.tool}")
    print(f"Difficulty: {player.difficulty}")
    print(f"Number of lives: {str(player.lives)}")


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


def launch_game():
    print("***Welcome to the Journey to Mount Qaf*** ")
    choice = main_menu()
    process_menu_selection(choice)


# write your code here
if __name__ == '__main__':
    launch_game()