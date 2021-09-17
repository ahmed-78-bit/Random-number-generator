import random

def welcome():
    print(
        "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n welcome to the guessing game "
        "\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

def guessing_number(number_of_tries, high_number_range):
    """
    Creating a function that takes two arguments 
    the number of tries and the highest number range
    """
    
    user_name = input("what is your name ? \n====>  ")
    user_name = user_name.upper()
    print(" welcome ", user_name, "to our guessing game\n\n", user_name,
          "you have to guess a number from 1 to ", high_number_range,
           "and you have ", number_of_tries,
          " tries to guess it right\n only numbers are allowed",
           "otherwise game over and you have to choose to continue plying a new game or quit ")

    continue_play = True

    while continue_play is True:
        
        tries = 0
        generate_random_number = random.randint(1, high_number_range)
       
       #print("enable this comment if you want to see the random number for testing :", generate_random_number)
        
        # try exception to catch unwanted user input
        try:
            while number_of_tries > 0:
                user_number_guess = int(input("\nGuess a number:\n"))
                number_of_tries -= 1
                tries += 1
                guess_it_right = tries

                if generate_random_number == user_number_guess:
                    print("\nWELL DONE\n it took you", guess_it_right,
                     "try to guess the right number")
                    win = " winner ==>> name:", user_name, "Number of guesses:", guess_it_right 
                    print(win)
                    break
                    
                    dict_win = {"name": user_name, "Number of guesses": guess_it_right}
                    """
                    creating a .txt stored file (as data in adictionaries) to
                    track the score of every player has plyed the game
                    """
                    # open the txt file for appending or creating it if it does not exist
                    with open("highscore.txt", "a") as f:
                        print(dict_win, file=f)
                        continue
                
                elif user_number_guess > high_number_range or user_number_guess < 1:
                    print("number is not in range \n", "You have", 
                    number_of_tries, "tries left")
                    pass

                elif user_number_guess > generate_random_number:
                    print("\nYou guessed too high  and you have\n ",
                     number_of_tries, "tries left\n")

                elif user_number_guess < generate_random_number:
                    print("\nYou guessed too low and you have \n ",
                     number_of_tries, "tries left\n")
            
            else:
                print("Game over\n ", "the random number was ",
                 generate_random_number, "\n")
        
        except ValueError:
            print("Game over\n only numbers are allowed \n ",
             "the random number was ", generate_random_number, "\n")
            
        keep_playing = input("\n type ` NO ` to EXIT THE GAME or"
         "click any key to START THE GAME: \n")

        if keep_playing.upper() == "NO":
            continue_play = False

            input("<<<<<<<<<<<<<<<<<<<<<<<<<     thank you for playing the game"         
            ">>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            quit()

        else:
            print("\n continue playing \n ")

def main():

    welcome()
 
    guessing_number(9, 100)
    """ passing value to the arguments of guessing_number function which can be any values
        I choose a value of ==> 9 tries and a range from 1 to 100
    """

if __name__ == '__main__':
    main()