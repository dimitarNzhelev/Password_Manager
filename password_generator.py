import random
from secrets import choice

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def password_generator():
    n_letters = random.randint(8,12)
    n_numbers = random.randint(2,6)
    n_symbols = random.randint(2,4)

    password = [ random.choice(letters) for i in range (n_letters)]
    password = password + [ random.choice(symbols) for i in range (n_symbols)]
    password = password + [ random.choice(numbers) for i in range (n_numbers)]

    random.shuffle(password)
    
    password = "".join(password)
    return password