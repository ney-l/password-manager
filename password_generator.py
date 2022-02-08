from random import randint, shuffle, choice, choices
import requests

word_list = []
long_words = []
short_words = []


def get_random_words():
    global word_list
    global short_words
    global long_words

    if len(word_list) > 0:
        return pick_words()

    URL = "https://www.mit.edu/~ecprice/wordlist.100000"
    response = requests.get(URL)
    word_list = response.text.split("\n")
    short_words = [word for word in word_list if len(word_list) > 0 and len(word) <= 4]
    long_words = [word for word in word_list if len(word_list) > 0 and 4 < len(word) < 9]
    return pick_words()


def pick_words():
    random_long_words = choices(long_words, k=2)
    random_short_words = choices(short_words, k=2)
    return random_long_words + random_short_words


def get_random_numbers():
    all_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    numbers = [choice(all_numbers) for _ in range(randint(2, 4))]
    return numbers


def generate_random_password():
    password_words = get_random_words()
    password_numbers = get_random_numbers()
    password_numbers_as_str = "".join(password_numbers)
    password_words.append(password_numbers_as_str)
    shuffle(password_words)
    return "-".join(password_words)



