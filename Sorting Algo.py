#Importing required modules
import math 
from functools import reduce
import time
from itertools import chain, repeat
import os

#Defining different functions for different operations
#Function to sort a list in increasing order
def num_sort():
    
    #To enter the elements in the list as user input
    lst = []

    try:
        n = int(input("Enter number of elements: "))
        
    except ValueError:
        print("Please enter Integer value.")
        n = int(input("Enter number of elements: "))

    for i in range(0,n):
        
        try:
            ele = int(input("Enter the element: "))
            
        except ValueError:
            print("Please enter Integer value.")
            ele = int(input("Enter the element: "))
    
        lst.append(ele)
    
    print("Your given list is: ",lst)
    lst.sort()
    
    print("The list in Sorted way is: ",lst)
    
#Function to sort a list with string elements in increasing order
def alphabet_sort():
    
    lst = []
    
    try:
        n = int(input("Enter number of elements: "))
        
    except ValueError:
        print("Please enter Integer value.")
        n = int(input("Enter number of elements: "))

    for i in range(0,n):
        
        ele = input("Enter the element: ")
    
        lst.append(ele)
        
    print("Your given list is: ",lst)
    
    lst.sort()
    
    print("The list in Sorted way is: ",lst)

#Function to give the square the elements of list
def square_list():

    lst = []

    try:
        n = int(input("Enter number of elements: "))
        
    except ValueError:
        print("Please enter Integer value.")
        n = int(input("Enter number of elements: "))

    for i in range(0,n):
        
        try:
            ele = int(input("Enter the element: "))
            
        except ValueError:
            print("Please enter Integer value.")
            ele = int(input("Enter the element: "))
    
        lst.append(ele)
    
    print('Your list is: ',lst)
    
    sort_lst = input("Do you want to sort the list first? Please enter 'Yes' or 'No': ")
    
    if sort_lst == 'yes' or sort_lst == 'Yes' or sort_lst == 'YES':
        
        lst.sort()
        print("Sorted list is: ",lst)
        square = list(map(lambda x: x*x, lst))
        print("The squared list will be: ",square)
        
    elif sort_lst == "no" or sort_lst == "NO" or sort_lst == "No":
    
        square = list(map(lambda x: x*x, lst))
    
        print("The squared list will be: ",square)
        
    else:
        print("Wrong Input\nTry again...")

#Function to find the power of elements of list
def power_list():

    lst = []

    try:
        num = int(input("Enter number of elements: "))
        n = int(input("Enter the value of the power of the number: "))
        
    except ValueError:
        print("Please enter Integer value.")
        num = int(input("Enter number of elements: "))
        n = int(input("Enter the value of the power of the number: "))

    for i in range(0,num):
        
        try:
            ele = int(input("Enter the element: "))
            
        except ValueError:
            print("Please enter Integer value.")
            ele = int(input("Enter the element: "))
    
        lst.append(ele)
        
    print("Your given list is: ",lst)
    
    sort_lst = input("Do you want to sort the list first? Please enter 'Yes' or 'No': ")
    
    if sort_lst == 'yes' or sort_lst == 'Yes' or sort_lst == 'YES':
        
        lst.sort()
        print("Sorted list is: ",lst)
        
        power = list(map(lambda x: x**n, lst))
        print("The required list is: ",power)
        
    elif sort_lst == "no" or sort_lst == "NO" or sort_lst == "No":
    
        power = list(map(lambda x: x**n, lst))
        print("The required list is: ",power)
        
    else:
        print("Wrong Input\nTry again...")
        
#Function to find the sum of elements of list
def sum_list():
    
    lst = []
    
    try:
        num = int(input("Enter number of elements: "))
        
    except ValueError:
        print("Please enter Integer value.")
        num = int(input("Enter number of elements: "))
    
    for i in range(0,num):
        
        try:
            ele = int(input("Enter the element: "))
            
        except ValueError:
            print("Please enter Integer value.")
            ele = int(input("Enter the element: "))
    
        lst.append(ele)
        
    print("The given list is: ",lst)
        
    sort_lst = input("Do you want to sort the list? Please enter 'Yes' or 'No': ")
    
    if sort_lst == 'yes' or sort_lst == 'Yes' or sort_lst == 'YES':
        
        lst.sort()
        print("Sorted list is: ",lst)
        
        Sum = reduce(lambda x,y:x+y, lst)
        print("The sum of the elements of the given list is: ",Sum)
        
    elif sort_lst == "no" or sort_lst == "NO" or sort_lst == "No":
    
        Sum = reduce(lambda x,y:x+y, lst)
        print("The sum of the elements of the given list is: ",Sum)
        
    else:
        print("Wrong Input\nTry again...")
    
#Function to sort a list with integer values in descending order
def reverse_sort():
    
    lst = []

    try:
        n = int(input("Enter number of elements: "))
        
    except ValueError:
        print("Please enter Integer value.")
        n = int(input("Enter number of elements: "))

    for i in range(0,n):
        
        try:
            ele = int(input("Enter the element: "))
            
        except ValueError:
            print("Please enter Integer value.")
            ele = int(input("Enter the element: "))
    
        lst.append(ele)
    
    print('The given list is: ',lst)
    
    lst.sort()
    
    print('Sortes list is: ',lst)
    
    lst.sort(reverse = True)
    
    print("Now the sorted list in reverse order is: ",lst)
    
#Function to sort a list with string values in descending order
def reverse_alphabet_sort():
    
    lst = []
    
    try:
        n = int(input("Enter number of elements: "))
        
    except ValueError:
        print("Please enter Integer value.")
        n = int(input("Enter number of elements: "))

    for i in range(0,n):
        
        ele = input("Enter the element: ")
    
        lst.append(ele)
        
    print("Your given list is: ",lst)
    
    lst.sort()
    
    print("Sorted list is: ",lst)
    
    lst.sort(reverse = True)
    
    print("The list in reverse Sorted way is: ",lst)
    
#To clear the terminal
if __name__ == '__main__':
	clear = lambda: os.system('cls')

	clear()

print("The operations are as follows: ")

#Function to print the operations which we can perform
def commands():
    commands = ["1. Sort a list with integer values in increasing order.", "2. Sort a list with string values in increasing order.",
                    "3. Sort a list with integer values in descending order.", "4. Sort a list with string values in decreasing order.",
                        "5. Print the sum of elements of given list.", "6. To square the elements of a list and then print the new list.",
                            "7. To find the power(user input) of the elements of given list and then print the new list."]
    
    for i in chain.from_iterable(repeat(commands, 1)):
        time.sleep(2)
        print(i)
        time.sleep(0.3)
    
    print("\n*Important Note!*\nYou can enter integer values in string values sort.\nAnd in that case the preference will be given to integer values first and then to string values.\n")
    
commands()

while True:
    
    #To select from the given operations
    time.sleep(3)
    try:
        select = int(input("Enter the operation which you want to perform: "))
        
    except ValueError:
        print("Please enter an Integer value.")
        select = int(input("Enter the operation which you want to perform: "))
        
    
    if select == 1:
        num_sort()
        
    elif select == 2:
        alphabet_sort()
        
    elif select == 3:
        reverse_sort()
        
    elif select == 4:
        reverse_alphabet_sort()
        
    elif select == 5:
        sum_list()
        
    elif select == 6:
        square_list()
        
    elif select == 7:
        power_list()
        
    else:
        print("Invalid Input.\nPlease try again...")
        continue
    
    #To end the while loop
    End = input("To Exit Please enter 'yes' else enter 'no': ")

    if End == 'yes' or End == 'Yes' or End == 'YES':
        print("Thank you.")
        time.sleep(0.3)
        exit()
        
    elif End == 'No' or End == 'NO' or End == 'no':
        pass
    
    else:
        print("Invalid Input.\nPlease try again.")
        End = input("To Exit Please enter 'yes' else enter 'no': ")
    
    #To read the commands again
    read_command = input("Do you want to read the commands again? Please enter 'yes' or 'no': ")
    
    if read_command == 'yes' or read_command == 'YES' or read_command == 'Yes':
        commands()
        
    elif read_command == 'no' or read_command == 'NO' or read_command == 'No':
        continue
    
    else:
        print("Invalid Input.\nPlease try again...")
        read_command = input("Do you want to read the commands again? Please enter 'yes' or 'no': ")