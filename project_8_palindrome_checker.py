print("Welcome to palindrome checker!")

def palindrome_checker(element):
    return True if (element==element[::-1]) else False


while True:
    word = input("\nEnter the word or number (tap off for quit): ")

    if word == 'off':
        print("\nThe palindrome checker is turned off.")
        break
    elif palindrome_checker(element=word):
        print(f"\nThe given input {word} is a palindrome.")
    elif not palindrome_checker(element=word):
        print(f"\nThe given input {word} is not a palindrome.")
    
    
