#prg to simulate wordle game
import random,requests
print("Welcome to Wordle ")
raw_url="https://gist.github.com/dracos/dd0668f281e685bad51479e5acaadb93/raw"
response=requests.get(raw_url)                  # fetches data from url
if response.status_code==200:                   # check if request was successful
    word_list=response.text.splitlines()     
    correct=random.choice(word_list)            # split the text into list of words and choose a random word
    attempts=6
    bg_green="\u001b[42m"                       # ANSI code for background color
    bg_yellow="\u001b[43m"
    bg_reset="\u001b[0m"
    while attempts>0:
        guess=input(f"You got {attempts} attempts left, enter your guess: ").lower()
        if len(guess)!=5:
            print("Please enter a 5 letter word")
        else:
            attempts-=1
            for i in range(0,5):
                if guess[i]==correct[i]:               # check if letter is in correct position
                    print(f"{bg_green}{guess[i]}{bg_reset}",end="")
                elif guess[i] in correct:              # check if letter is in word but not in correct position
                    print(f"{bg_yellow}{guess[i]}{bg_reset}",end="")
                else:                                  # check if letter is not in word 
                    print(guess[i],end="")
            print()
            if guess==correct:
                print("Congrats! You guessed the word")
                exit()
    print(f"You have used all your attempts ,correct word was {correct}")
else:
    print("Error in fetching data from API")