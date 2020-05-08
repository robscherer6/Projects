import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro(item, scary_thing):
    print_pause("You find yourself standing in an open field, filled with "
                "grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + scary_thing + " is somewhere around "
                "here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) "
                "dagger.")


def field(item, scary_thing):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    while True:
        path_choice = input("(Please enter 1 or 2.)\n")
        if path_choice == "1":
            house(item, scary_thing)
            break
        elif path_choice == "2":
            cave(item, scary_thing)
            break


def house(item, scary_thing):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and "
                "out steps a " + scary_thing + ".")
    print_pause("Eep! This is the " + scary_thing + "'s' house!")
    print_pause("The " + scary_thing + " attacks you!")
    if "Sword" not in item:
        print_pause("You feel a bit under-prepared for this, what "
                    "with only having a tiny dagger.")
    while True:
        choice = input("Would you like to (1) fight or (2) run away?")
        if choice == "1":
            if "Sword" in item:
                print_pause("As the " + scary_thing + " moves to attack, "
                            "you unsheath your new sword.")
                print_pause("The Sword of Ogoroth shines brightly in "
                            "your hand as your brace yourself for the "
                            "attack.")
                print_pause("But the " + scary_thing + " takes on look "
                            "at your shiny new toy and runs away!")
                print_pause("You have rid the town of the "
                            "" + scary_thing + ". You are victorious!")
            else:
                print_pause("You do your best...")
                print_pause("but your dagger is no match for the "
                            "" + scary_thing + ".")
                print_pause("You have been defeated!")
            play_again()
            break
        if choice == "2":
            print_pause("You run back into the field.")
            print_pause("Luckily, you don't seem to have been followed.")
            field(item, scary_thing)
            break


def cave(item, scary_thing):
    if "Sword" in item:
        print_pause("\nYou peer cautiously into the cave.")
        print_pause("\nYou've been here before, and gotten all "
                    "the good stuff. It's just an empty cave now.")
        print_pause("\nYou walk back to the field.\n")
    else:
        print_pause("\nYou peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and "
                    "take the sword with you.")
        print_pause("You walk back out to the field.")
        item.append("Sword")
    field(item, scary_thing)


def play_again():
    again = input("Would you like to play again? (y/n)").lower()
    if again == "y":
        print_pause("\nExcellent! Restarting the game...\n")
        play_game()
    elif again == "n":
        print_pause("\nThanks for playing! See you next time.\n")
    else:
        play_again()


def play_game():
    item = []
    scary_thing = random.choice(["troll", "dragon", "pirate", "wicked fairie",
                                 "gorgon"])
    intro(item, scary_thing)
    field(item, scary_thing)


play_game()
