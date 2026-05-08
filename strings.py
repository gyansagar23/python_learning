# In python Textual data is represnted as string.
# String is sequence of characters.

message_1 = "Hello World"
print(message_1)  #To print the value of variable message_1
print(type(message_1))  # what type of data is stored inside variable message_1


#How to include ' inside the string
message_2 = "This is Gyan's House" 
print(message_2) 

message_3 = 'This is Gyan\'s House'  #another way to include ' inside the string using escape character \
print(message_3)

#How to write a string in multiple lines
message_4 = """Python is a high level programming
language. It is used for machine learning, web development
and many more applications"""
print(message_4)

#How to access individual characters in a string
message_5 = "Python"
print(message_5[0])  #accessing the first character of the string via indexing and its start from 0
print(message_5[1])  #accessing the second character of the string
print(message_5[5])  #accessing the last character of the string using negative indexing


#How to access a range of characters in a string
message_6 = "Hello World"
print(message_6[0:5])  #accessing the first 5 characters of the string using slicing
print(message_6[6:11])  #accessing the last 5 characters of the string using slicing
print(message_6[:5])  #accessing the first 5 characters of the string       
print(message_6[6:])  #accessing the last 5 characters of the string


#Methods on strings
message_7 = "Hello World"
print(message_7.upper())  #converting the string to uppercase
print(message_7.lower())  #converting the string to lowercase
message_8 = message_7.replace("World","Gyan") #replacing the word "World" with "Gyan" in the string and storing the new string in variable message_8
print(message_8)

print(message_8.count("Hello"))  #counting the number of times "Hello" appears in the string message_8
print(message_8.count("G"))  #counting the number of times "G

print(message_8.find("K"))  #finding the index of the first occurrence of "K" in the string message_8, if not found it will return -1


#How to concatenate strings
greetings = "Hello"
first_name = "Gyan"
last_name = "Sagar"

message_9 = greetings + " " + first_name + " " + last_name  #concatenating the strings using + operator and adding space between them
print(message_9) 

#In earlier way of concatenating strings, there is problem if there are multiple variables to concatenate, it can be difficult to read and maintain the code.
#In python 3.6 and above, we can use f-strings to concatenate strings in a more readable and maintainable way.
message_10 = f"{greetings} {first_name} {last_name}"  #using f-strings to concatenate the strings, it is more readable and maintainable than using + operator
print(message_10)



#How to check what all atributes and methods are available for string data type
print(dir(str))  #dir() function is used to get the list of all attributes and methods available for the string data type


#How to check the documentation of a method
print(help(str.upper))  #help() function is used to get the documentation of a method, it will show the description of the method and how to use it