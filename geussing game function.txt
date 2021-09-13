import random


# creating a welcome function
def usern_name():
    userName = input("what is your name ? \n====>  ")
    userName = userName.upper()
    print(" welcome ", userName, "to our guessing game\n\n", userName, "you have to guess a number from 1 to 50")


# Creating a function that takes two arguments the number of tries and the highest number in the range

def guessing_number(number_of_tries, high_number_range):
    generate_random_number = random.randint(1, high_number_range)
    print("enable this comment if you want to see the random number for testing :", generate_random_number)

    # try exception to catch unwanted user input
    try:
        while number_of_tries > 0:
            user_number_guess = int(input("\nGuess a number:\n"))
            number_of_tries -= 1

            if generate_random_number == user_number_guess:
                print("\nWELL DONE\n it took you", number_of_tries, "try to guess the right number")
                break

            elif user_number_guess > high_number_range or user_number_guess < 1:
                print("number is not in range \n", "You have", number_of_tries, "tries left")
                pass

            elif user_number_guess > generate_random_number:
                print("\nYou guessed too high  and you have\n ", number_of_tries, "tries left\n")

            elif user_number_guess < generate_random_number:
                print("\nYou guessed too low and you have \n ", number_of_tries, "tries left\n")
        else:
            print("Game over\n ", "the random number was ", generate_random_number, "\n")

    except ValueError:
        print("\nplease type a number\n")


# creating the main Function

def guessing_game():
    print(
        '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n welcome to the guessing game \n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    userName = input("what is your name ? \n====>  ")
    userName = userName.upper()
    print(" welcome ", userName, "to our guessing game\n\n", userName, "you have to guess a number from 1 to 100")

    continue_play = True

    while continue_play is True:

        """
        passing value to the arguments of guessing_game function which can be any values
        ( I chose 9 tries and a range from 1 to 100 )   guessing_number(9, 101)
        """
        generate_random_number = random.randint(1, 101)
        #print("enable this comment if you want to see the random number for testing :", generate_random_number)

        # try exception to catch unwanted user input
        try:

            number_of_tries = 9
            while number_of_tries > 0:
                user_number_guess = int(input("\nGuess a number:\n"))
                number_of_tries -= 1
                """
                creating guess_it_right variable (to create highscore txt file) which
                """
                guess_it_right = 9 - number_of_tries
                if generate_random_number == user_number_guess:
                    print("\nWELL DONE\n it took you", guess_it_right, "try to guess the right number")
                    win = " winner ==>>   name:", userName, "   Number of guesses: ", guess_it_right
                    print(win)
                    break

                    
                    """
                    creating a .txt stored file (as data in adictionaries) to
                     track the score of every player has plyed the game
                    """
                    dict_win = {"name": userName, "Number of guesses": guess_it_right}
                    # open the txt file for appending or creating it if it does not exist
                    with open("highscore.txt", "a") as f:
                        print(dict_win, file=f)
                        continue

                elif user_number_guess > 101 or user_number_guess < 1:
                    print("number is not in range \n", "You have", number_of_tries, "tries left")
                    pass

                elif user_number_guess > generate_random_number:
                    print("\nYou guessed too high  and you have\n ", number_of_tries, "tries left\n")

                elif user_number_guess < generate_random_number:
                    print("\nYou guessed too low and you have \n ", number_of_tries, "tries left\n")
            else:
                print("Game over\n ", "the random number was ", generate_random_number, "\n")

        except ValueError:
            print("\nplease type a number\n")
            continue
        """
         creating a block of code to to give the user the chance to choose 
         between keep playing the game and quitting the game.
        """
        keep_playing = input("\n type ` NO ` to EXIT THE GAME or click any key to START THE GAME: \n")

        if keep_playing.upper() == "NO":
            continue_play = False

            input("<<<<<<<<<<<<<<<<<<<<<<<<<     thank you for playing the game         >>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            quit()

        else:
            print("\n continue playing \n ")
            continue


guessing_game()
