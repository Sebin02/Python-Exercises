#prg to implement hangman game 
import random,requests
response=requests.get('https://random-word-api.herokuapp.com/word')     # fetches data from url
if response.status_code==200:                                           # check if request was successful
    word_list=response.json()                                           # convert the response to json
    chosen_word=random.choice(word_list)                                # choose a random word from the list
    print('Welcome to Hangman Game , you have 6 attempts to guess the word, GOOD LUCK...')
    guessed_letters=[]                                                  # list to store guessed letters
    display=[]                                                          # list to store the display of letters
    attempts=6
    for i in range(len(chosen_word)):
        display+=['_']                                                  # fill the display list with underscores
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
                letter=chosen_word[position]             # letter from chosen word is stored in letter                                         
                if letter==guess:                        
                    display[position]=guess    # if letter is in chosen word, replace the underscore with the letter
            print(display)
            if guess not in chosen_word:
                attempts-=1
                print(f"Wrong letter, Attempts left: {attempts}")   #if letter is not in chosen word, reduce attempts
                if attempts==0:
                    game_over=True
                    print(f'You Lose,correct word was:{chosen_word}') #make game_over True if attempts are 0
            if '_' not in display:                  #check if any '_' are left in display
                game_over=True
                print('Congrats, You win')          # if all letters are guessed
else:
    print("Error in fetching data from API")