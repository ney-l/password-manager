from random import randint, shuffle, choice, choices
import requests

URL = "https://www.mit.edu/~ecprice/wordlist.100000"


class PasswordGenerator:
    def __init__(self):
        self.word_list = []
        self.long_words = []
        self.short_words = []

    def get_random_words(self):
        if len(self.word_list) > 0:
            return self.pick_words()

        response = requests.get(URL)
        self.word_list = response.text.split("\n")
        self.short_words = [word for word in self.word_list if len(word) <= 6]
        self.long_words = [word for word in self.word_list if 6 < len(word) < 12]
        return self.pick_words()

    def pick_words(self):
        random_short_words = choices(self.short_words, k=2)
        random_long_words = choices(self.long_words, k=2)
        return random_short_words + random_long_words

    def get_random_numbers(self):
        all_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        numbers = [choice(all_numbers) for _ in range(randint(2, 4))]
        return numbers

    def generate_random_password(self):
        password_words = self.get_random_words()
        password_numbers = self.get_random_numbers()
        password_numbers_as_str = "".join(password_numbers)
        password_words.append(password_numbers_as_str)
        shuffle(password_words)
        return "-".join(password_words)



