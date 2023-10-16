import random
def guess_the_number():
    print("\nWelcome to number guessing game")
    while True:
        difficulty = input("\nEnter easy for 10 chances or hard for 5 chances: ")
        
        if difficulty == 'easy':
            life = 10
            break
        elif difficulty == 'hard':
            life = 5
            break
        else:
            print("Enter correctly.")
        
    random_number = random.randint(0,100)
    game_is_on = True
    while game_is_on:
        number = int(input('\nGuess a number from 0 to 100 or -1 to exit the game: '))
        
        if random_number > number and not number==-1:
            print("Guessed number is low.")
            life-=1
        elif random_number < number and not number==-1:
            print("Guessed number is high")
            life-=1
        elif random_number == number:
            print("\nYou win.")
            print(f"You guessed the number correctly with {life} chances")
            break
        print(f'You have {life} chances left.')
        if life == 0 or number == -1:
            game_is_on = False
    
    if not game_is_on:
        print(f"\nYou lose with {life} chances")

while True:
    guess_the_number()
    again = input("\nDo you want to play again: ")
    if again == 'yes':
        pass
    else:
        print("The game is turned off")
        break
