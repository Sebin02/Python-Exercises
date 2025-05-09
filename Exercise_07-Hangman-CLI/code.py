#prg to implement hangman game 
import random,requests
response=requests.get('https://random-word-api.herokuapp.com/word')
if response.status_code==200:
    word_list=response.json()
    chosen_word=random.choice(word_list)
    print('Welcome to Hangman Game , you have 6 attempts to guess the word, GOOD LUCK...')
    guessed_letters=[]
    display=[]
    attempts=6
    for i in range(len(chosen_word)):
        display+=['_']
    print(display)
    game_over=False
    while not game_over:
        print("")
        print("Guessed letters: ",guessed_letters)
        guess=input("Guess a letter: ").lower()
        if guess.isalpha()==False:
            print("Please enter a valid letter")
        elif len(guess)>1:
            print("Please enter only one letter")
        elif guess in display:
            print("You have already guessed this letter")
        else:
            guessed_letters.append(guess)
            for position in range(len(chosen_word)):
                letter=chosen_word[position]
                if letter==guess:
                    display[position]=guess
            print(display)
            if guess not in chosen_word:
                attempts-=1
                print(f"Wrong letter, Attempts left: {attempts}")
                if attempts==0:
                    game_over=True
                    print(f'You Lose,correct word was:{chosen_word}')
            if '_' not in display:
                game_over=True
                print('Congrats, You win')
else:
    print("Error in fetching data from API")