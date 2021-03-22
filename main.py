import requests
from Jokes import Jokes

# function to generat more than one joke
def ten_joke_menu():
    ten_check = input("""What random jokes u want?
                        (1) Random
                        (2) By type
                        """)
    if ten_check == "1":
        ten_random_jokes = Jokes("ten")
        display_check = input("""How do you like to display them?
                (1) ALL 
                (2) Only ones with even ID
                (3) Only ones with odd ID """)

        if display_check == "1":
            for ten_check_index in range(len(ten_random_jokes.joke)):
                ten_random_jokes.print_jokes()
        if display_check == "2":
            ten_random_jokes.display_jokes_by_id_parity("even")
        if display_check == "3":
            ten_random_jokes.display_jokes_by_id_parity("odd")
        else:
            print("Sorry, u pressed a wrong input, re-run the code for more fun")

    if ten_check == "2":

        ten_by_type_check = input("""What type you want ?
                                    (1) Programming
                                    (2) General""")
        if ten_by_type_check == "1":
            generate_ten_by_type("programming")

        if ten_by_type_check == "2":
            generate_ten_by_type("programming")


# function to generate Ten random jokes by type
def generate_ten_by_type(type):
    ten_random_jokes_type = Jokes(f"{type}/ten")
    type_check = input("""Do you want them ?
                                        (1)printed
                                        (2) checked if same type""")
    if type_check == "1":
        for ten_check_index in range(len(ten_random_jokes_type.joke)):
            ten_random_jokes_type.print_jokes()
    if type_check == "2":
        ten_random_jokes_type.check_if_same_type(type)

# this is when Main input interface starts

check = input(""" Hello, what joke do you want ? 
                    (1) Single joke
                    (2) Ten Random Jokes""")

if check == "1":
    single_joke = Jokes("random")
    print("Here is your joke:")
    single_joke.print_joke()

elif check == "2":
    ten_joke_menu()

else:
    print("Sorry, u pressed a wrong input, re-run the code for more fun")







