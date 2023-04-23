import random




choices = ['rock','paper','scissord']
game_role = {
    "rock" : "scissord" , #rock is win 
    "Paper" : "rock", #Paper is win 
    "scissors" : "rock" #scissord is win 
}
computer_score_coefficient = 0
user_score_coefficient = 0


#at the first set 0 to scores of players 
computer_score = 0
user_score = 0

# append winer of each turn to win_history for record 
win_history=[]

finish=False


# the while loop for sequential execution
while True:

    #set the user choice from input 
    user_choice=input("""
-rock 
-paper
-scissors
pleae write your choice : """)
    print('\n///////////////////////////////\n')

    #set computer choice by random function
    computer_choice = random.choice(choices)
    print('computer choice : ' + computer_choice)


    # check game role and increase score of winner 
    if user_choice == computer_choice :
        print('both player selected same choice')
        

    elif computer_choice is game_role[user_choice]:
        print("you win !")
        user_score = user_score  + (2 ** user_score_coefficient)
        user_score_coefficient += 1
        
        #set 0 to coefficient for calculate
        #without coefficient in another user next turn 
        computer_score_coefficient = 0
        win_history.append("user")

    
    else :
        print("you lose !")
        computer_score = computer_score + (2 ** computer_score_coefficient)
        user_score_coefficient = 0
        win_history.append("computer")
        

    # show game detail in 
    print("your score : " + str(user_score))
    print("computer score : " + str(computer_score))
    print('win history : ' , win_history)


    #check winner and break the loop
    #winner who is have over 50 point or win 5 time 
    if computer_score >= 50 or computer_score_coefficient == 5:
        print("computer Win !!!!")
        finish=True
    if user_score >= 50 or user_score_coefficient == 5:
        print('user Win *********!')
        finish=True



    if finish :

        start_again = input("do you want play again (t/f) ?")

        if start_again == "t":
            computer_score_coefficient = 0
            user_score_coefficient = 0
            computer_score = 0
            user_score = 0
            win_history.clear()
            finish=False
            print("\n game is startind ... \n \n")

        else:
            print('---------')
            print("game is finished !")
            break

    print("\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")