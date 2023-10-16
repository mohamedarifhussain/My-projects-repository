import random
print("Welcome to the game of hangman")


words = ['effect', 'act', 'pancake', 'religion', 'vest', 'noise', 'plant', 'judge', 'profit', 'guide', 'cast', 'yard', 'sail', 'shape', 'cup', 'men', 'record', 'dress', 'sense', 'statement', 'brother', 'love', 'rate', 'plane', 'horses', 'division', 'soap', 'roll', 'knee', 'idea', 'sheet', 'adjustment', 'bead', 'pull', 'seat', 'metal', 'shoe', 'monkey', 'discovery', 'sponge', 'fork', 'war', 'ocean', 'cause', 'health', 'roof', 'minute', 'cake', 'play', 'sticks']

chosen_word = random.choice(words)

life = 6


blanck = []
for i in chosen_word:
    blanck.append('_')
    print('_',end=' ')
print(f'\n\nGuess a {len(chosen_word)} letter word.')
print(f"You have {life} life for this game.")
    
game_is_on = True
while game_is_on:
    if '_' not in blanck:
        print("You win by guessing all the letters.")
        break
    guess_letter = input('\nEnter a letter to guess: ')
    if guess_letter in chosen_word:
        for i in range(len(chosen_word)):
            if guess_letter == chosen_word[i]:
                blanck[i] = guess_letter
    else:
        life-=1


    for _ in blanck:
        print(_,end=' ')
    print(f'\n\nYou have {life} chances to guess the letters.')
    
    if life == 0:
        print("\n You lose with 0 lifes.")
        guess = input("\nDo you want guess again: ")
        if guess == 'no':
            print('Game is turned off.')
            game_is_on = False
        elif guess == 'yes':
            chosen_word = random.choice(words)

            life = 6


            blanck = []
            for i in chosen_word:
                blanck.append('_')
                print('_',end=' ')
            print(f'\n\nGuess a {len(chosen_word)} letter word.')
            print(f"You have {life} life for this game.")
