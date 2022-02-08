# Password Generator Project
from random import randint, shuffle, choice


def pick_random_items(items, num):
    random_items = [choice(items) for _ in range(num)]
    return random_items


def generate_random_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = pick_random_items(letters, randint(8, 10))
    password_symbols = pick_random_items(symbols, randint(2, 4))
    password_numbers = pick_random_items(numbers, randint(2, 4))

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    return "".join(password_list)

