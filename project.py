import json
from colorama import init, Fore, Style

init(autoreset=True)

def load_story(filename):
    """Loads the story JSON file and returns a dictionary."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Story file not found.")
        exit(1)
    except json.JSONDecodeError:
        print("Story file is not a valid JSON.")
        exit(1)

def display_scene(scene, player_name):
    """Prints the scene's text and choices to the user, with name injection."""
    text = scene["text"].replace("{name}", player_name)
    print("\n" + text)
    for key, choice in scene.get("choices", {}).items():
        print(f"{key}: {choice['desc']}")

def get_next_scene(scene, choice):
    """Returns the next scene ID based on user choice."""
    if choice in scene.get("choices", {}):
        return scene["choices"][choice]["next"]
    else:
        print(Fore.RED + "Invalid choice.")
        return None

def show_menu():
    print(Fore.MAGENTA + "\n=== GALACTIC HITCHHIKER ===")
    print("1. Start Adventure")
    print("2. How to Play")
    print("3. Quit")

def how_to_play():
    print(Fore.CYAN + """
Welcome to the Galactic Hitchhiker!

Make choices by typing the letter shown (e.g., 'a', 'b') to advance the story.
Each choice leads to a new situation, some better than others.
Good luck... or not.

Press Enter to return to menu.
""")
    input()

def main():
    story = load_story("story.json")
    player_name = input("What is your name, traveler? ").strip()

    while True:
        show_menu()
        choice = input(Fore.YELLOW + "\nChoose an option: ").strip()

        if choice == "1":
            current_scene = "start"
            while True:
                scene = story[current_scene]
                display_scene(scene, player_name)

                if not scene.get("choices"):
                    print(Fore.GREEN + "\nThe End.")
                    break

                user_choice = input(Fore.YELLOW + "\nWhat do you do? ").strip()
                next_scene = get_next_scene(scene, user_choice)
                if next_scene:
                    current_scene = next_scene
        elif choice == "2":
            how_to_play()
        elif choice == "3":
            print(Fore.MAGENTA + "Goodbye, traveler.")
            break
        else:
            print(Fore.RED + "Invalid menu option.")

if __name__ == "__main__":
    main()
