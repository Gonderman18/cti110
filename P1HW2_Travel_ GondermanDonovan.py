import math

    # Travel Expense for vacation
    # 2022-08-30
    # CTI-110 P1HW2 - Travel Expense
    # Donovan Gonderman

print('This program calculates and displays travel expenses to include a 6% tax ')
print()
budget = int(input('Enter Budget: '))
print()
destination = input('Enter your travel destination: ')
print()
gas = int(input('How much do you think you will spend on gas? '))
print()
accommodation = int(input('Approximately, how much will you need for accommodation/hotel? '))
print()
food = int(input('Last, how much do you need for food? '))
print()
gas_tax = gas + (gas * .06)
accommodation_tax = accommodation + (accommodation * .06)
food_tax = food + (food * .06)
taxes = (gas * .06) + (accommodation * .06) + (food * .06)


print('-----------Travel Expenses------------')
print('Location: ' ,destination)
print('Initial Budget: ' , budget * 1.00)
print()
print('Fuel:', gas_tax)
print('Accommodation:', accommodation_tax )
print('Food:', food_tax)
print()
print('Your taxes on gas, accommodations, and food total up to be: ' , taxes)
print()
reman_balance= int( budget - (gas_tax + accommodation_tax + food_tax))
print('Remaining Balance: ',reman_balance * 1.00 )
print()
print('Your initial budget' , budget)
print('Where you are planning on going' , destination)
print('What you plan to spend on gas' ,  gas)
print('What you plan to spend on accommodations' , accommodation)
print('What you plan to spend on food' , food)
print('Gas after a 6% tax' , gas_tax)
print('Accommodation after 6% tax' , accommodation_tax)
print('Food after a 6% tax' , food_tax)
# put in your budget and where you are going then the program takes away the gas accommodations and food plus tax from your budget.
# budget = first int input
# destination = only string input
# gas = seconde int input
# accomodation = third int input 
# food = fourth int input
# gas_tax = gas + (gas * .06)
# accommodation_tax = accommodation + (accommodation * .06)
# food_tax = food + (food * .06)
# reman_balace = an int of the budget minus the sum of gas food and accommodation plus taxes.
input('Press ENTER to exit')
# input('Press ENTER to exit')was the only way I could get the program to show the results after the final input. 
