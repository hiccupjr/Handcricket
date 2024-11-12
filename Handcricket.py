# Handcricket
# This game is played by 90 kids and early 2k kids in the school and colleges.
# I create this in the CLI format. 

import pyfiglet
from random import*
from countdown import countdown


#banner 
banner = pyfiglet.figlet_format('Hand Cricket Game')
print(banner)

print('How to Play:')
print('\n\t1. First you have to chose Odd or Even for the toss. The toss will be very simple.\n\t   If you chose odd or even, then computer will be your alternate.')
print('\t2. Then you and computer have to pick a number 1 to 10. It will add and show a number is Odd or Even.\n\t\tfor examble: You chose Odd. you pick a number 8 and computer pick 7.\n\t\t8+7=15. 15 is Odd number. So you win the toss. If you chosen even ,you will loss the toss.')
print("\t3. If you win the toss you have to chose 'Batting or Bowling'. If you loss the toss then wait for the computer choice." )
print('\t4. Batting:\n\t\tBatting is very simple. First you have to chose a number 1 to 6 and computer guess what you chose.\n\t\tIf computer didn\'t guess your number again and again, it will added your score.\n\t\tIf computer guess your number, you are out. And ready beat computer  ')
print('\t5. Bowling:\n\t\tIt is alternate for batting. You have to guess what the computer chose.\n\t\tIf you guess correctly then computer will be out.')
print('\t6. After completing batting and bowling your score and computer score will be published.\n\t   If your score is higher than computer you win the match.\n')

user_name = input('Enter your name: ') 

while True:
    print ('\n1. Odd\t\t2. Even')
    toss = input('\nChoose 1 or 2 :').lower()
    while toss not in ['1','2','odd','even']:
        toss = input('\nInvalid option. Choose again 1 or 2 :').lower()
    if toss in ['1','odd']:
        print(f'\n{user_name} chose Odd')
        print('Then computer will be Even')
        
    else:
        print(f'\n{user_name} chose Even')
        print('Then computer will be Odd')
        
    num =['1','2','3','4','5','6','7','8','9','10']  
    user = input('\nPick a number 1 to 10: ')
    while user not in num:
        if user =='0':
            print('\nZero is not acceptable. Please try again')
            user = input('Pick a number 1 to 10: ')
        else:
            user = input('Invalid number. Please try again: ')
    computer = choice(num)      
    print('Computer pick number ' , computer)
    ans = int(user)+int(computer)
    print(f'\n{user}+{computer} = {ans}')

    if ans%2 != 0:
        print(f'\n{ans} is Odd Number.')
        if toss in ['1','odd']:
            print(f'{user_name} win the Toss')
            users ='win'
        else :
            print('Computer win the Toss')
            users ='loss'
    else:
        print(f'\n{ans} is Even Number.')
        if toss in ['2','even']:          
            print(f'{user_name} win the Toss')
            users ='win'
        else:
            print('Computer win the Toss')
            users ='loss'
            

    #Game function will be start there
    choices=['1','2','3','4','5','6']

    def batting() :
        print('\nReady To Batting')
        countdown(mins=0, secs=5)
        global user_score
        user_score = 0
        print('Choose a number 1 to 6. It will add your score if computer didn\'t defeat you. ')
        while True:
            playershot = input('Give Number : ')
            while playershot not in choices:
                playershot=input('Invalid number .Please try again:')
            
            print(f'\n{user_name} = {playershot}')
            computershot = choice(choices)
            print('Computer = ',computershot )
            
            if playershot == computershot:
                print(f'\n{user_name}, you are defeated by Compuer.')
                print(f'{user_name} Score is {user_score}')
                
                break
            else:
                user_score += int(playershot) # userscore = userscore + playershot
                print(f'\t\t\t\t\t{user_name} Score ={user_score}')

    def bowling():#When the user choose bowling 
        print('\nReady For Bowling!')
        countdown(mins=0, secs=5)    
        global computer_score
        computer_score = 0
        print ('Guss the number 1 to 6  to defeat Computer.')
        while True:
            computershot = choice(choices)
            playershot = input('Guess Number: ')
            while playershot not in choices:
                playershot=input('Invalid option.Please try again :')
        
            print('\nComputer = ',computershot)
            print(f'{user_name} = {playershot}') 
            
            if playershot == computershot:
                print(f'\n{user_name}, you defeat a computer.')
                print(f'Computer score is {computer_score} ')
                break
            else:
                computer_score += int(computershot)
                print(f'\t\t\t\t\tComputer Score ={computer_score}')
        
    def result(userscore,comscore):
        print('\nWait a second for the Result.')
        countdown(mins=0, secs=5)    
        if userscore == comscore:
            print(f'\n{user_name} score and computer score is equal.\nThen match will be tie.')
        elif userscore > comscore:
            print(f'\n{user_name} score is {userscore}.\ncomputer score is {comscore}.')
            print(f'\nCongratulation! {user_name} You win the match. :)')
        else:
            print(f'\n{user_name} score is {userscore}.\ncomputer score is {comscore}.')
            print(f'\nSorry {user_name}, You loss the match. :(')

    
    field_choice = ['Batting','Bowling']
    
    if users == 'win':
        print('\n1. Batting\t\t2. Bowling')
        user_choice = input('Chose 1 or 2 : ')
        while user_choice not in ['1' ,'2']:
            user_choice = input('Invalid Option. Please choose again: ')
        if user_choice=='1':
            print(f'\n{user_name} chose Batting.')
            batting() #if user chose batting , computer will be play first bowling.
            bowling()
            result(user_score,computer_score)

        elif user_choice == '2':
            print(f'\n{user_name} chose Bowling.')
            bowling() #if user chose bowling, we will be play first bowling.
            batting()
            result(user_score,computer_score)
    else:
        com_choice = choice(field_choice)
        if com_choice == 'Batting':
            print('\nComputer chose Batting.')
            bowling() #if computer chose batting, user will be bowling.
            batting()
            result(user_score,computer_score)
        else :
            print('\nComputer chose Bowling.')
            batting() #if computr chose batting , user will be play first bowling.
            bowling()
            result(user_score,computer_score)
            

    play_again = input('\nDo you want play again (y/n) : ').lower()

    if play_again not in ['y','yes']:
        break
