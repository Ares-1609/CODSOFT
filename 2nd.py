import random
user=0 #Score of user
com=0 #score of computer
comp=[1,2,3]
def user_input():
    choice=int(input("Please select 1 for stone, 2 for paper and 3 for scissors"))
    if choice in [1,2,3]:
        return choice
    else:
        print("Invalid input, enter 1,2 or 3")
        return user_input()
while True:
    choice=int(user_input())
    selected_choice=random.choice(comp)
    while(choice==selected_choice):
        print("Whoa! It's a tie")
        selected_choice=random.choice(comp)
    match choice:
        case 1:
            if(selected_choice==2):
                print("Opponent chose Paper , Oops ! you lost")
                com+=1
            elif(selected_choice==3):
                print("Opponent chose Scissors, Hurray ! you won")
                user+=1
        case 2:
            if(selected_choice==3):
                print("Opponent chose Scissors, Oops ! you lost")
                com+=1
            elif(selected_choice==1):
                print("Opponent chose Stone, Hurray ! you won")
                user+=1
        case 3:
            if(selected_choice==1):
                print("Opponent chose stone, Oops ! you lost")
                com+=1
            elif(selected_choice==2):
                print("Opponent chose paper, Hurray ! you won")
                user+=1
            else:
                print("Invalid Input")
    print(f"The scores are as follows\n user:{user}\tcomp:{com}")
    play_again=input("Do you wanna play again? answer in yes or no.")
    if play_again!='yes':
        print("Thanks for playing!")
        break
        
        
    
        