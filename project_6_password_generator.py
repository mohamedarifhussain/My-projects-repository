import random

print('Welcome to password generator')
list_of_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
list_of_numbers = '1234567890'
list_of_symbols = '!@#$%^&*'
generator_is_on = True
while generator_is_on:

    generator = input('\nDo you want to generate a password: ')
    password = []
    if generator == 'yes':
        letters = int(input("\nHow many letters do you need in the password: "))
        numbers = int(input("How many numbers do you need in the password: "))
        symbols = int(input("How many symbols do you need in the password: "))
        for i in range(letters):
            let = random.choice(list_of_letters)
            password.append(let)
        for i in range(numbers):
            num = random.choice(list_of_numbers)
            password.append(num)
        for i in range(symbols):
            sym = random.choice(list_of_symbols)
            password.append(sym)
        random.shuffle(password)
        
        print(f"\nHere is your new password: {''.join(password)}")
        
    else:
        print("\nPassword generator is off.")
        generator_is_on = False
