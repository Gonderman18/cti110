# CTI-110
# P4HW1 - Score List
# Gonderman Donovan 
# 2022-11-09


# This program gets the number of scores from the user.
# Then checks to see if the score is between 0 and 100. ( If Its Valid or Not)
# If the score is valid it will put the score into a empty list.
# The it will drop the lowest grade in the list and print the grade it droped, the new list, your average and your letter grade.

# Gets the Number of scores that the user wants as input 
num_of_scores=int(input("How many Scores do you want to enter? "))

# makes a empty list to hold the scores in
scoreslist=[]

#  The program uses a for loop to take scores as inputs
for i in range(1, num_of_scores+1):
    
    # while loop takes input until user enters the right score
    while True:
        try:
            # takes a score as input from user
            score=int(input("Enter score # {}: ".format(i)))
            
            # The program checkes to see if the score is between 0 and 100
            if score >= 0 and score <= 100:
                
                # if it is the program puts the new score in the new list
                scoreslist.append(score)
                break
            # if its not then the program  prints a message telling the usre thats not a valid score
            elif score >= 0 and score <= 100 :
                score=int(input("Enter score # {} again: ".format(i)))
            else:
                print('INVALID Score entered!!!!!')
                print('Score should be between 0 and 100')
                
                
        except:
            continue

# list of Scores the user acyually entered
print('list of entered scores: ', scoreslist)

print()
print('-' * 13, 'Results','-' * 13 )


# prints the lowest score you entered
lowest_scr = (min(scoreslist))
print('Lowest Score  : {:.1f}'.format(lowest_scr))

# Prents the modified list after getting rid of the lowest score
scoreslist.remove(lowest_scr)

#formlist = ['{:.1f}'.format(score) for score in scoreslist]
#print('Modified List :',formlist)
print('Modified List :',scoreslist)

#printing average of modified scoreslist
avg_of_scores = sum(scoreslist)/len(scoreslist)
print('Scores Average: {:.2f}'.format(avg_of_scores))

#printing letter grade

if avg_of_scores > 80 and avg_of_scores <= 100:
    print('Grade         : A')
elif avg_of_scores > 80 and avg_of_scores <= 90:
    print('Grade         : B') 
elif avg_of_scores > 70 and avg_of_scores <= 80:
    print('Grade         : C')
elif avg_of_scores > 60 and avg_of_scores >= 70:
    print('Grade         : D')
else:
    print('Grade' , ' ' * 7, ': F')

print('-' * 35)
