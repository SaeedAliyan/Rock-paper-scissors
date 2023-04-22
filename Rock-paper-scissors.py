import random

#at the first set scores of players 



choices = ['rock','paper','scissord']
game_role = {
    "rock" : "scissord" , #rock is win 
    "Paper" : "rock", #Paper is win 
    "scissord" : "rock" #scissord is win 
}
computer_score_coefficient = 1
user_score_coefficient = 1


computer_score = 0
user_score = 0

win_history=[]

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
        if user_score != 0 :
            user_score *= user_score_coefficient
        else:
            user_score =1
        user_score_coefficient += 1
        computer_score_coefficient = 1
        win_history.append("user")

    
    else :
        print("you lose !")
        if computer_score != 0:
            computer_score *= computer_score_coefficient
        else :
            computer_score =1
        computer_score_coefficient += 1
        user_score_coefficient = 1
        win_history.append("computer")
        

    
    print("your score : " + str(user_score))
    print("computer score : " + str(computer_score))
    print(win_history)
    #check winner and break the loop
    #winner who is have over 50 point 
    if computer_score >= 50 or computer_score_coefficient == 6:
        print("computer Win !!!!")
        break
    if user_score >= 50 or user_score_coefficient == 6:
        print('user Win *********!')
        break
    
    print("\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")