import requests

# getting 10 radom jokes by type
ten_random_by_type = requests.get("https://official-joke-api.appspot.com/jokes/programming/ten")
json_ten_random_by_type = ten_random_by_type.json()
j = json_ten_random_by_type[0]["type"]

# how to print the jokes content
for i in json_ten_random_by_type:
    print(i["setup"])
    print(i['punchline'])


# how to test if 10 random jokes are same type
for i in json_ten_random_by_type:
    if i["type"] != j:
        print("Error")
else:
    print("all jokes are same type")


#  Retrieve 10 random jokes and display only the ones that have an odd/even ID.

ten_random_jokes = requests.get("https://official-joke-api.appspot.com/jokes/programming/ten")
json_ten_random_jokes = ten_random_jokes.json()
#even id jokes :
for i in json_ten_random_jokes:
    if int(i["id"]) % 2:
        print(i["setup"])
        print(i['punchline'])


