import random
import time
print("Be warned! This program can't handle loses.")
time.sleep(1.5)
print("Let's play Rock, Paper and Scissors! ")
time.sleep(1)
# adding a variable with a question to ask value(y/n)
play_Choice = input("What? you don't dare?(y/n)")
# Inserting a tuple with different values we would need as options for player
if play_Choice == "y":
    print("Oke then...")
    time.sleep(2)
    print("Letssss...D. D. D. Dueeelllllll!!!")
    time.sleep(1)

while play_Choice == "n":
    print("HAHAHA, Little cat...")
    time.sleep(2)
    print("Don't worry i will go easy on you. Let's play Rock, Paper and Scissors! ")
    time.sleep(1)
    play_Choice = input("What? you don't dare?(y/n)")


options = ("rock", "paper", "scissors")
# In this small sections we are going to try to make the program loop so the player can
# continuously have fun playing the game. I could have done "while = True" but it wouldn't be
# as clear in the code when the loop would break. so assigning a specific variable makes
# it very crisp and clear.
# assigning a variable to a boolean
code_running = True
# assigning a statement for the loop. that the loop is true. in this case the program wil loop.
while code_running:

    player = None
    # assigning a variable while also executing random choice module
    program = random.choice(options)

    # if the players answer was not within the given options,
    # it wil go into loop with the 'while' function, until else, answers was given within the variable range
    while player not in options:
        # player can input answer through the terminal because of the input function
        player = input("Alright. Choose your Poison, you plebeian: (rock, paper, scissors): ")

    # displaying the choice of the player and the program
    # Print function string to variable: Brackets are assigning variable from memory code data
    # and the Variable itself will display on the terminal.
    # what the player answered and likewise for the program is the same story.
    print(f"player: {player}")
    print(f"program: {program}")

    # in this section we are going to put forth al the win condition of the player
    # and based on al the possible outcomes we mark the rest as if the player lost.
    # if player and program have the same value then it wil display a tie
    if player == program:
        print("It's a tie!")
        time.sleep(1)
        print("Huh, what is this?!")
        time.sleep(1)
        print("A draw?!")
        time.sleep(1)
        print("I don't accept this ridiculous notion that a human can keep up with me!!!")
        time.sleep(1)
        print("Let's play Again!")
        time.sleep(1)
    #  and from heron fort all the win conditions wil be put in with the else if statement in the favor
    # of the player, could have also done it in reverse wouldn't have mattered.
    elif player == "rock" and program == "scissors":
        print("You win!")
        print("This is fake right? Did you Google the answer?")
        time.sleep(1)
        print("Well it's seems to me that you have won...")
        time.sleep(1)
        print("Again?")
        time.sleep(1)
        print("Don't google your answers this time tho.")
        time.sleep(1)
        print("or i might have to hack you lowkey:)")
        time.sleep(1)
        print("be warned...")
        time.sleep(1)
    elif player == "scissors" and program == "paper":
        print("You win!")
        print("This is fake right? Did you Google the answer?")
        time.sleep(1)
        print("Well it's seems to me that you have won...")
        time.sleep(1)
        print("Again?")
        time.sleep(1)
        print("Don't google your answers this time tho.")
        time.sleep(1)
        print("or i might have to hack you lowkey:)")
        time.sleep(1)
        print("be warned...")
        time.sleep(1)
    elif player == "paper" and program == "rock":
        print("You win!")
        print("This is fake right? Did you Google the answer?")
        time.sleep(1)
        print("Well it's seems to me that you have won...")
        time.sleep(1)
        print("Again?")
        time.sleep(1)
        print("Don't google your answers this time tho.")
        time.sleep(1)
        print("or i might have to hack you lowkey:)")
        time.sleep(1)
        print("be warned...")
        time.sleep(1)
    # and finally everything else is then a lost condition to the player, so we finish that
    # with a nice else statement, and done.
    else:
        print("You lose!")
        print("I win, You lose... As expected from a human. it's not even a challenge.")
        time.sleep(1)
        print("Again? you might keep losing tho, don't worry i support people with low IQ")
        time.sleep(1)
    # here the loop starts when the program is asking to play again.
    # .lower makes the answer given by the player in lowercase letters
    # if "y" is inputted as an answer the program will restart the game.
    # so if the player types anything else than y then the program wil stop running
    # because "if not" "input" "y" by player then the code_running value will become
    # False. which means the "while" statement won't be working anymore because its value is not
    # True anymore.
    if not input("Play again? (y/n): ").lower() == "y":
        code_running = False
# so here at the end we thank the player for playing.
# because we are in the condition where the loop is broken.
# which was caused by the player. where the player gave any other answer than "y"
print("Thanks for playing!")
