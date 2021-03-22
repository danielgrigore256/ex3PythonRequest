import requests
from Jokes import Jokes

# 3. Retrieve 10 random jokes by type and for each joke
# verify if the type is correct. If not, raise an error.
test = Jokes("https://official-joke-api.appspot.com/jokes/programming/ten")
test.check_if_same_type()

# 4.Retrieve 10 random jokes and display only the ones that have an odd/even ID

test2 = Jokes("https://official-joke-api.appspot.com/random_ten")
test2.display_jokes_by_even_id()



