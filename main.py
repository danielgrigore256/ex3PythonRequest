import requests
from Jokes import Jokes


# function menu to generate 10 jokes
def ten_joke_menu():
    while True:
        ten_check = input("""What random jokes u want?
                        (1) Random
                        (2) By type
                        """)
        if ten_check == "1":
            generate_ten_random()
            break

        if ten_check == "2":

            while True:
                ten_by_type_check = input("""What type you want ?
                                    (1) Programming
                                    (2) General""")
                if ten_by_type_check == "1":
                    generate_ten_by_type("programming")
                    break

                if ten_by_type_check == "2":
                    generate_ten_by_type("general")
                    break
            break
# function menu to generate 10 random jokes
def generate_ten_random():
    ten_random_jokes = Jokes("ten")
    while True:
        display_check = input("""How do you like to display them?
                   (1) ALL 
                   (2) Only ones with even ID
                   (3) Only ones with odd ID """)

        if display_check == "1":
            for ten_check_index in range(len(ten_random_jokes.joke)):
                ten_random_jokes.print_jokes(ten_check_index)
            break
        if display_check == "2":
            ten_random_jokes.display_jokes_by_id_parity("even")
            break
        if display_check == "3":
            ten_random_jokes.display_jokes_by_id_parity("odd")
            break


# function to generate Ten random jokes by type
def generate_ten_by_type(type):
    ten_random_jokes_type = Jokes(f"{type}/ten")
    while True:
        type_check = input("""Do you want them ?
                                        (1)printed
                                        (2) checked if same type""")
        if type_check == "1":
            for ten_check_index in range(len(ten_random_jokes_type.joke)):
                ten_random_jokes_type.print_jokes(ten_check_index)
            break
        if type_check == "2":
            ten_random_jokes_type.check_if_same_type(type)
            break


# this is when Main input interface starts
while True:
    check = input(""" Hello, what joke do you want ? 
                    (1) Single joke
                    (2) Ten Random Jokes""")
    if check == "1":
        single_joke = Jokes("random")
        print("Here is your joke:")
        single_joke.print_joke()
        break
    elif check == "2":
        ten_joke_menu()
        break


