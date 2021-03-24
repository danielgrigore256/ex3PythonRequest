import requests
from Jokes import Jokes


# function menu to generate 10 jokes
def select_type():
    while True:
        try:
            ten_by_type_check = int(input("""What type you want ?
                                        (1) Programming
                                        (2) General"""))
        except ValueError:
            print("you didnt entered a number")
        else:
            if ten_by_type_check == 1:
                generate_ten_by_type("programming")
                break

            if ten_by_type_check == 2:
                generate_ten_by_type("general")
                break
            else:
                print("Not a valid choice, please try again")
def ten_joke_menu():
    while True:
        try:
            ten_check = int(input("""What random jokes u want?
                            (1) Random
                            (2) By type
                            """))
        except ValueError:
            print("you didnt entered a number")
        else:
            if ten_check == 1:
                generate_ten_random()
                break

            elif ten_check == 2:
                select_type()
                break
            else:
                print("Not a valid choice, please try again")


# function menu to generate 10 random jokes
def generate_ten_random():
    ten_random_jokes = Jokes("ten")
    while True:
        try:
            display_check = int(input("""How do you like to display them?
                                    (1) ALL 
                                    (2) Only ones with even ID
                                    (3) Only ones with odd ID """))
        except ValueError:
            print("you didnt entered a number")
        else:
            if display_check == 1:
                for ten_check_index in range(len(ten_random_jokes.joke)):
                    ten_random_jokes.display_jokes(ten_check_index)
                break
            if display_check == 2:
                ten_random_jokes.display_jokes_by_id_parity("even")
                break
            if display_check == 3:
                ten_random_jokes.display_jokes_by_id_parity("odd")
                break
            else:
                print("Not a valid choice, please try again")


# function to generate Ten random jokes by type
def generate_ten_by_type(joke_type):
    ten_random_jokes_type = Jokes(f"{joke_type}/ten")
    while True:
        try:
            type_check = int(input("""Do you want them ?
                                        (1)printed
                                        (2) checked if same type"""))
        except ValueError:
            print("you didnt entered a number")
        else:
            if type_check == 1:
                for ten_check_index in range(len(ten_random_jokes_type.joke)):
                    ten_random_jokes_type.display_jokes(ten_check_index)
                break
            if type_check == 2:
                ten_random_jokes_type.check_if_same_type(joke_type)
                break
            else:
                print("Not a valid choice, please try again")


# this is when Main input interface starts
while True:
    try:
        check = int(input(""" Hello, what joke do you want ? 
                        (1) Single joke
                        (2) Ten Random Jokes"""))
    except ValueError:
        print("you didnt entered a number")
    else:
        if check == 1:
            single_joke = Jokes("random")
            print("Here is your joke:")
            single_joke.display_jokes(0)
            break
        elif check == 2:
            ten_joke_menu()
            break
        else:
            print("Not a valid choice, please try again")


