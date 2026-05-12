#what is for loop in python
#A for loop is a control flow statement that allows you to iterate over a sequence (such as a list, tuple, string, etc.) and execute a block of code for each item in the sequence.
#how to use for loop in python
fruits = ["apple", "banana", "cherry"]  #creating a list of fruits
for fruit in fruits:  #iterating over the list of fruits using a for loop
    print(fruit)  #printing each fruit in the list

#how to use for loop with range function in python
for i in range(5):  #iterating over a sequence of numbers from 0 to 4 using the range function
    print(i)  #printing each number in the sequence

#how to use for loop with else statement in python
for i in range(5):  #iterating over a sequence of numbers from 0 to 4 using the range function
    print(i)  #printing each number in the sequence
else:
    print("Loop completed successfully")  #this block of code will be executed after the loop completes normally  

#how to use for loop with break statement in python
# the break statement is used to exit the loop prematurely when a certain condition is met.
# when the break statement is executed, the loop will be terminated immediately and the program will continue with the next statement after the loop.
for i in range(5):  #iterating over a sequence of numbers from 0 to 4 using the range function
    if i == 3:  #checking if the value of i is equal to 3
        break  #if the condition is true, the loop will be terminated immediately
    print(i)  #printing each number in the sequence until the break statement is executed   

#how to use for loop with continue statement in python
# the continue statement is used to skip the current iteration of the loop and move on to the next iteration when a certain condition is met.
# when the continue statement is executed, the rest of the code inside the loop for the current iteration will be skipped and the loop will move on to the next iteration.
for i in range(5):  #iterating over a sequence of numbers from 0 to 4 using the range function
    if i == 3:  #checking if the value of i is equal to 3
        continue  #if the condition is true, the rest of the code inside the loop for the current iteration will be skipped and the loop will move on to the next iteration
    print(i)  #printing each number in the sequence except for 3, which is skipped due to the continue statement


#how to use nested for loop in python
# a nested for loop is a for loop inside another for loop. The inner loop will be executed for each iteration of the outer loop.
for i in range(3):  #outer loop iterating over a sequence of numbers from 0 to 2 using the range function
    for j in range(2):  #inner loop iterating over a sequence of numbers from 0 to 1 using the range function
        print(f"i: {i}, j: {j}")  #printing the values of i and j for each iteration of the inner loop      


#what is while loop in python
#A while loop is a control flow statement that allows you to execute a block of code repeatedly as long as a certain condition is true.
#how to use while loop in python            
i = 0
while i < 5:  #executing the loop as long as the condition (i < 5) is true
    print(i)  #printing the value of i for each iteration of the loop
    i += 1  #incrementing the value of i by 1 for each iteration of the loop                        