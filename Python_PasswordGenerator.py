import random

def is_valid_include(answer):
    if answer.upper() == 'Y' or answer.upper() == 'N':
        return True
    else:
        return False

def is_valid_number(number):
    if number.isdigit():
        return True
    else:
        return False

def is_include(const):
    answer = input(f"Include {const}? (Y/N): ")
    while not is_valid_include(answer):
        answer = input('Wrong answer. Enter Y or N: ')
    if answer.upper() == 'Y':
        return True
    else:
        return False

def set_count_passwords():
    count_passwords = input('How many passwords to genereate: ')
    while not is_valid_number(count_passwords):
        count_passwords = input('Enter number: ')
    return int(count_passwords)

def set_password_length():
    password_length = input("Password length: ")
    while not is_valid_number(password_length):
        password_length = input('Enter number: ')
    return int(password_length)

def set_options():
    const_digits = '0123456789'
    const_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    const_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    const_symbols = '!#$%&*+-=?@^_'
    const_ambiguous = 'il1Lo0O'
    selected_symbols = ''

    count_passwords = set_count_passwords()
    password_length = set_password_length()

    if is_include(const_digits):
        selected_symbols += const_digits
    if is_include(const_lowercase):
        selected_symbols += const_lowercase
    if is_include(const_uppercase):
        selected_symbols += const_uppercase
    if is_include(const_symbols):
        selected_symbols += const_symbols
    if not is_include(const_ambiguous):
        for symbol in const_ambiguous:
            selected_symbols = selected_symbols.replace(symbol, '')

    return selected_symbols, count_passwords, password_length

def password_generator():
    selected_symbols, count_passwords, password_length = set_options()
    for i in range(count_passwords):
        password = ''
        for j in range(password_length):
            password += random.choice(selected_symbols)
        print(password)

password_generator()
