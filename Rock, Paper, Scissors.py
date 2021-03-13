import time
loose = ("The computer Wins")
win = ("You win")
lives = 5
score = 0
drew = 0
computer_lives = 7
password_list = []
while True:
    print("Fill in the below information")
    username = input("Please enter your username = ")
    password = input("Please enter your password = ")
    searchfile = open("accounts.txt","r")
    for line in searchfile:
        password_list.append(line.strip())
        if username and password in password_list:
            print("Access Granted")
            time.sleep(0.5)
            print("loading.")
            time.sleep(0.5)
            print("loading..")
            time.sleep(0.5)
            print("loading...")
            start_menu = """
            ------------------------------------------------
                  Welcome to Rock, Paper and Scissors      
            ------------------------------------------------
            Live Rules
            You start with ",lives,"lives.
            If you win you get an extra live.
            If you loose you loose a live.
            If you draw the lives stay the same.
            ------------------------------------------------
            ------------------------------------------------
            To see a list of rules type rules.
            ------------------------------------------------
            At any point to type exit to leave the game.
            ------------------------------------------------
            The computer has lives aswell.
            Can you beat the computer ?
            Good Luck !
            ------------------------------------------------
            """
            print(start_menu)
            while True:
                rps = input("Rock, Paper, Scissors?    ")
                rps = rps.title()
                import random
                computer = ("rock","paper","scissors")
                computer = random.choice(computer)
                #if rock
                if rps == 'Rock' and computer == 'paper':
                    print("The computer choose",computer)
                    print("")
                    print(loose)
                    print("")
                    print("")
                    lives -= 1
                if rps == 'Rock' and computer == 'scissors':
                    print("The computer choose",computer)
                    print("")
                    print(win)
                    print("")
                    print("")
                    lives += 1
                #if paper
                if rps == 'Paper' and computer == 'rock':
                    print("The computer choose",computer)
                    print("")
                    print(win)
                    print("")
                    print("")
                    lives += 1
                if rps == 'Paper' and computer == 'scissors':
                    print("The computer choose",computer)
                    print("")
                    print(loose)
                    print("")
                    print("")
                    lives -= 1
                #if scissors
                if rps == 'Scissors' and computer == 'rock':
                    print("The computer choose",computer)
                    print("")
                    print(loose)
                    print("")
                    print("")
                    lives -= 1
                if rps == 'Scissors' and computer == 'paper':
                    print("The computer choose",computer)
                    print("")
                    print(win)
                    print("")
                    print("")
                    lives += 1
                #Duplicates
                if rps == 'Scissors' and computer == 'scissors':
                    print("The computer choose",computer)
                    print("")
                    print("You Drew")
                    print("")
                    print("")
                    drew += 1    
                if rps == 'Rock' and computer == 'rock':
                    print("The computer choose",computer)
                    print("")
                    print("You Drew")
                    print("")
                    print("")
                    drew += 1    
                if rps == 'Paper' and computer == 'paper':
                    print("The computer choose",computer)
                    print("")
                    print("You Drew")
                    print("")
                    print("")
                    drew += 1
                #system
                if rps == 'Rules':
                    print("-------------------------------")
                    print("            Rules        ")
                    print("-------------------------------")
                    print("Rock looses against Paper")
                    print("Rock beats Scissors")
                    print("Paper beats Rock")
                    print("Paper looses against Scissors")
                    print("Scissors beats Paper")
                    print("Scissors looses against Rock")
                    print("-------------------------------")
                if rps == 'Display Lives':
                    print("Lives = ",lives)
                if rps == 'Display Score':
                    print("Score = ",score)        
                if rps == 'Display Drew':
                    print("Drew = ",drew)
                #lives
                if lives == 0 or rps == "Test":
                    print("Thank you for playing")
                    print("You have ran out of lives")
                    print("You got: ", score, " correct")
                    print("You drew: ",drew, " times")
                    stop = input("Press enter to exit")
                    exit()
                if computer_lives == 0:
                    print("Thanks for playing")                    
                    print("Computer ran out of lives")
                    print("You got: ", score, " correct")
                    print("You drew: ",drew, " times")
                    stop = input("Press enter to exit")
                    exit()
                #exit
                if rps == "Exit":
                    print("Exiting.")
                    import time
                    time.sleep(0.5)
                    print("Exiting..")
                    time.sleep(0.5)
                    print("Exiting...")
                    time.sleep(0.5)
                    exit()
        else:
            print("Your username or password is incorrect")
            print("--------------------------------------")
                
