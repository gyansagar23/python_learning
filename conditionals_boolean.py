# what is conditionals?
# conditionals are statements that allow us to execute certain blocks of code based on certain conditions.
# the most common conditional statements in python are if, elif and else.   

# how to use if statement in python
age = 18
if age >= 18:  #checking if the value of age is greater than or equal to 18
    print("You are eligible to vote")  #if the condition is true, this block of code will be executed

# how to use if-else statement in python
age = 16    
if age >= 18:  #checking if the value of age is greater than or equal to 18
    print("You are eligible to vote")  #if the condition is true, this block of code will be executed
else:  #if the condition is false, this block of code will be executed
    print("You are not eligible to vote")  #if the condition is false, this block of code will be executed


# how to use if-elif-else statement in python
age = 20
if age < 18:  #checking if the value of age is less than 18
    print("You are a minor")  #if the condition is true, this block of code will be executed
elif age >= 18 and age < 60:  #checking if the value of age is greater than or equal to 18 and less than 60
    print("You are an adult")  #if the condition is true, this block of code will be executed
else:  #if the above conditions are false, this block of code will be executed
    print("You are a senior citizen")  #if the above conditions are false, this block of code will be executed


"""what is the main difference between if and elif is that if statement is first checked if itsnot true
then elif statement will checked and if its not true then else statement will be executed.
But what if we have multiple if statements, then each if conditions will be checked independently
irrespective of whether the previous if condition is true or false."""


amount = 5000

if amount:  #checking if the value of amount is greater than 10000
    print("You are eligible for a loan")  #if the condition is true, this block of code will be executed
else:
    print("You are not eligible for a loan")  #if the condition is false, this block of code will be executed


amount = 0

if amount:  #checking if the value of amount is greater than 10000
    print("You are eligible for a loan")  #if the condition is true, this block of code will be executed
else:
    print("You are not eligible for a loan")  #if the condition is false, this block of code will be executed


"""If we use a variable in a conditional statement, it will be evaluated as a boolean value.
In python, the following values are considered as false:
    - None
    - False
    - 0
    - An empty sequence (e.g., '', (), [])
    - An empty mapping (e.g., {})
    All other values are considered as true."""

if 0:  #checking if the value of 0 is true or false 
    print("This will not be printed")  #if the condition is true, this block of code will be executed       
else:
    print("This will be printed")  #if the condition is false, this block of code will be executed

if "":  #checking if the value of empty string is true or false
    print("This will not be printed")  #if the condition is true, this block of code will be executed
else:
    print("This will be printed")  #if the condition is false, this block of code will be executed

if []:  #checking if the value of empty list is true or false
    print("This will not be printed")  #if the condition is true, this block of code will be executed
else:
    print("This will be printed")  #if the condition is false, this block of code will be executed