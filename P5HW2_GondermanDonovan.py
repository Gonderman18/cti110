import random


# The program outputs the main menu. Then the user choices wether they want a adition problem,
# or a subtraction problem. The program will tell the user if they wrong and if they were to high,
# or to low. When the user inputs the right answer the program will cingragulate them and tell them,
# how many guesses it took them. The the program will ask if the want to do another math quiz or quit.


# 2022-11-26
# CTI-110 P5HW2 - Math Quiz
# Donovan Gonderman
#
print('Welcome to Math Quiz\n')

def addRandom():
        num_1 = random.randint(0,1000)                                            #gets a random number between 0 and 1000.
        num_2 = random.randint(0,1000)                                            #gets a random number between 0 and 1000.
        print(f'{num_1:>6}')
        print(f"+{num_2:>5}")
        print('Enter answer.')
        ans=int(input())
        num_of_gs = 1                                                             #starts the number of guesses as 1
        while ans!= num_1 + num_2:                                                #checks the number entered against the correct answer.
                num_of_gs = num_of_gs + 1                                         #adds 1 to nuber of guesses evertime the unser enters a wrong answer.
                
                if ans<num_1+num_2:                                               #if number entered is to low. output to low.
                        print("Sorry, guess is too low.")
                        print()
                else:                                                             #if number entered is to high. output to high.
                        print("Sorry, guess is too high.")
                        print()

                ans=int(input("try again : "))                                    #ask user to enter another guess.
                
        print('Congratulations!!!! your answer is correct..')
        print('Number of guesses :', num_of_gs)                                   #tells the user the number of guesses it took to get the right answer

def subRandom():
        num_1=random.randint(0,1000)                                              #gets a random number between 0 and 1000.
        num_2=random.randint(0,1000)                                              #gets a random number between 0 and 1000.
        print(f'{num_1:>6}')
        print(f'-{num_2:>5}')
        print('Enter answer.')
        ans=int(input())
        num_of_gs = 1                                                             #starts the number of guesses as 1
        while ans != num_1 - num_2:                                               #checks the number entered against the correct answer.
                num_of_gs = num_of_gs + 1                                         #adds 1 to nuber of guesses evertime the unser enters a wrong answer.
                if ans < num_1 - num_2:                                           
                        print('Sorry, guess is too low.')                         #if number entered is to low. output to low.
                        print()
                else:
                        print('Sorry, guess is too high.')                        #if number entered is to high. output to high.
                        print()
                ans=int(input('try again : '))
        print('Congratulations!!!! your answer is correct..')
        print('Number of guesses :', num_of_gs)                                   #tells the user the number of guesses it took to get the right answer
        print()
if __name__=='__main__':

        while 1:

                print()
                print('MAIN MENU')
                print('-'*18)
                print('1. Adding Random Numbers ')
                print('2. Subtracting Random Numbers')
                print('3. Exit\n')
                num=int(input('Please choose one of the menu options: '))
                
                if num==3:                                                        #ends the program
                        print('Thank you for playing...')
                        print('Bye!!')
                        break
                if num==1:
                        addRandom()                                               #calls addition function
                if num==2:
                        subRandom()                                               #calls subtraction function
