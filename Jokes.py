import requests

class Jokes():
    """
    Class that creates json file from jokepage
    """
    def __init__(self,link):
        """
        creates a json file from 10 random jokes
        :param link: the joke(s) link
        :return a json dictionary with jokes
        """

        joke_response = requests.get(link)
        self.joke = joke_response.json()

    def print_joke(self, index):
        """
        Prints the contents of the joke from the json file
        :param index: the position of joke ( we got 10 jokes in each json)
        :return: print of the joke
        """
        print("Intro : ", self.joke[index]["setup"])
        print("Punch line : ", self.joke[index]['punchline'])

    def check_if_same_type(self):
        """
        checking if the jokes are same type (programming , general )
        :return: True if same type // False + error message if not same type
        """

        j = self.joke[0]["type"]
        for i in self.joke:
            if i["type"] != j:
                return False
                print("Error, not same type")
        else:
                return True

    def display_jokes_by_even_id(self):
        """
        function to display jokes by the parity of the id field
        :return: printing the coresponding jokes
        """
        index = 0
        for i in self.joke:
            if int(i["id"]) % 2:
                self.print_joke(index)
            index += 1


