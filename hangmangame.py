import random
import hangmanstages
import words
lives=6
print("WELCOME TO HANGMAN GAME 🙂")
print("All the BEST !!🚀")
chosen_word=random.choice(words.word)
display=[]
for letter in chosen_word:
    display+='_'
game_over=False
while not game_over:
    print(display)
    guessed_letter = input("Guess a letter :").lower()
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guessed_letter:
            display[position]=guessed_letter
    if guessed_letter not in chosen_word:
        lives -=1
        if lives==0:
            game_over=True
            print("You lose !!")
            print("Correct Answer is :",chosen_word)
    if '_' not in display:
        game_over=True
        print("You Win :)")
    print(hangmanstages.stages[lives])

