import random
print("Let's play Hangman!!")
print("you have only 6 lives so try to guess the word in 6 attempts! good luck!")
words_list=["rose","lilly","tulip","sunflower","lotus"]
lives=6
chosen_word=random.choice(words_list)
print("hint:it's a flower")
word_to_guess=[]
for i in range(len(chosen_word)):
    word_to_guess+='_'
print(word_to_guess)
game_over=False
while not game_over:
    guessed_letter=input("guess a letter:").lower()
    for position in range(len(chosen_word)):  #0 ,1 ,2  ,3 ,4
        letter=chosen_word[position]
        if letter==guessed_letter:
            word_to_guess[position]=guessed_letter
    print(word_to_guess)
    if guessed_letter not in chosen_word:
        lives-=1
        if lives==0:
            game_over=True
            print("You lose!!")
    if '_' not in word_to_guess:
        game_over=True
        print("You Win!!")



'''Creates a hidden word (['_', '_', '_', '_', '_'])
Player guesses letters
If correct: Updates _ with the guessed letter.
If wrong: Decreases lives.
Game continues until
All letters are guessed → "You Win!!"
Lives = 0 → "You Lose!!"'''
