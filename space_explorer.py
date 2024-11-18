import random
import time

def print_pause(message, delay=1):
    """Prints a message with a delay for immersive storytelling."""
    print(message)
    time.sleep(delay)

def intro():
    print_pause("You are Captain Nova, leader of the spaceship *Star Voyager*.")
    print_pause("Your mission: explore the uncharted sector of the galaxy.")
    print_pause("Rumors speak of hostile aliens, mysterious planets, and hidden treasures.")
    print_pause("Your crew depends on you to make the right choices. Let's begin!\n")

def choose_planet():
    print_pause("\nYour ship encounters three mysterious planets.")
    print_pause("Planet A glows with a strange green light.")
    print_pause("Planet B is a dark, rocky world emitting faint energy signals.")
    print_pause("Planet C appears golden and lush, covered in thick clouds.")
    choice = input("Which planet will you explore? (A, B, or C): ").strip().upper()

    if choice == "A":
        green_planet()
    elif choice == "B":
        rocky_planet()
    elif choice == "C":
        golden_planet()
    else:
        print_pause("Invalid choice! Please select A, B, or C.")
        choose_planet()

def green_planet():
    print_pause("\nYou land on the green planet and find a massive alien relic.")
    print_pause("The relic starts glowing as you approach...")
    choice = input("Do you (1) touch the relic or (2) retreat to the ship? ")

    if choice == "1":
        if random.choice([True, False]):
            print_pause("\nThe relic bestows incredible knowledge to you!")
            print_pause("Your crew celebrates as you return with the secret to interstellar travel.")
            end_game("Victory! You’ve advanced the future of humanity.")
        else:
            print_pause("\nThe relic emits a blast of energy, disabling your ship.")
            print_pause("Your mission ends here.")
            end_game("Mission failed.")
    elif choice == "2":
        print_pause("\nYou retreat safely to your ship and leave the planet.")
        print_pause("Better safe than sorry!")
        choose_planet()
    else:
        print_pause("Invalid choice. Try again.")
        green_planet()

def rocky_planet():
    print_pause("\nYou land on the dark, rocky world.")
    print_pause("Your scanners detect faint energy signals from a cave nearby.")
    choice = input("Do you (1) investigate the cave or (2) scan from orbit? ")

    if choice == "1":
        if random.choice([True, False]):
            print_pause("\nInside the cave, you find an ancient alien energy source.")
            print_pause("Your crew is thrilled as it powers your ship with unlimited energy!")
            end_game("Victory! Your ship becomes the ultimate explorer.")
        else:
            print_pause("\nThe cave collapses, and your ship barely escapes.")
            print_pause("You leave the planet empty-handed.")
            choose_planet()
    elif choice == "2":
        print_pause("\nYou scan the planet but find nothing of interest.")
        print_pause("Perhaps another world holds the key to your success.")
        choose_planet()
    else:
        print_pause("Invalid choice. Try again.")
        rocky_planet()

def golden_planet():
    print_pause("\nThe golden planet is lush and beautiful.")
    print_pause("Your crew sets foot on its surface, but the clouds swirl ominously.")
    choice = input("Do you (1) explore further or (2) leave the planet immediately? ")

    if choice == "1":
        print_pause("\nYou discover a peaceful alien civilization living in harmony.")
        print_pause("They share advanced technology and knowledge with you.")
        end_game("Victory! You’ve made first contact and forged an alliance.")
    elif choice == "2":
        print_pause("\nYou leave the planet without exploring.")
        print_pause("Perhaps you missed an incredible opportunity.")
        choose_planet()
    else:
        print_pause("Invalid choice. Try again.")
        golden_planet()

def end_game(message):
    print_pause(f"\n{message}")
    print_pause("Thank you for playing *Space Explorer Adventure*!")
    play_again = input("Would you like to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        play_game()
    else:
        print_pause("Goodbye, Captain!")

def play_game():
    intro()
    choose_planet()

# Start the game
if __name__ == "__main__":
    play_game()
