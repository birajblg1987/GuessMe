import random
 
def guess(globalattempt,success):
    print("Welcome to number guess game. This game is created by Biraj \n")
    wildnumber = (random.randint(0, 5))
    attempt = 1
    globalattempt += 1
    
    while attempt<=3:       
        try:
            guess = int(input("Guess the random number between 0 to 5: "))
        except:
            print("It should only be an integer")
        else:
            if wildnumber == guess:
                success +=1
                print("Nice! you guessed the number ({}) correctly in {} attempt.".format(wildnumber,attempt))
                break
        finally:
            attempt += 1
            print("You have {} attempt left.".format(4-attempt))
            print('*'*80)
            if attempt == 4 and wildnumber != guess:
                print("Better Luck Next Time!")

    print("Below are your match summary:")
    print("You played: ", globalattempt, " matches")
    print("You won: ", success, " matches")

    return globalattempt, success
    
def main():
    
    globalattempt, success = guess(0,0)
    i = ""
    while i != 'n':
        i = input("Do you want to replay? (y or n): ").lower()
        if i == 'y':
            globalattempt, success = guess(globalattempt, success)

if __name__ == "__main__":
    main ()
