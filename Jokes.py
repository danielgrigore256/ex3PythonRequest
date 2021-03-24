import requests


class Jokes:
    """
    Class that creates json file from jokepage
    """
    def __init__(self, endpoint):
        """
        creates a json file from 10 random jokes
        :param endpoint: type of joke wanted (single joke/ 10 random jokes)
        :return a json dictionary with jokes
        """
        link = f"https://official-joke-api.appspot.com/jokes/{endpoint}"
        joke_response = requests.get(link)
        self.joke = joke_response.json()

    def print_jokes(self, index):
        """
        Prints the contents of the jokes from the json file
        :param index: the position of joke ( we got 10 jokes in each json)
        :return: print of the joke
        """
        if isinstance(self.joke, dict):
            print("""
                    JokeID : {}
                    Intro: {} 
                    Punch line : {}""".format(self.joke["id"],
                                              self.joke["setup"],
                                              self.joke['punchline']))
        else:
            print("""
                  JokeID : {}
                  Intro: {} 
                  Punch line : {}""".format(self.joke[index]["id"],
                                            self.joke[index]["setup"],
                                            self.joke[index]['punchline']))

    def check_if_same_type(self, joke_type):
        """
        checking if the jokes are same type (programming , general )
        :param joke_type: the type you need to be compared to
        :return: error message if not same type
        """
        for i in self.joke:
            if i["type"] != joke_type:
                print(f"Error, not same type as {joke_type} ")
                break
        else:
            print(f"All ten random jokes are same type, {joke_type} !")

    def display_jokes_by_id_parity(self, parity):
        """
        function to display jokes by the parity of the id field
        :return: printing the coresponding jokes
        """
        pun_index = 0
        if parity == "even":
            for pun in self.joke:
                if int(pun["id"]) % 2 == 0:
                    self.print_jokes(pun_index)
                pun_index += 1
        elif parity == "odd":
            for pun in self.joke:
                if int(pun["id"]) % 2 != 0:
                    self.print_jokes(pun_index)
                pun_index += 1
