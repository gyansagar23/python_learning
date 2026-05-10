#Arithematic operations with float and integer
a = 5
b = 2
print(a + b)  #addition of two integers
print(a - b)  #subtraction of two integers  
print(a * b)  #multiplication of two integers
print(a / b)  #division of two integers, it will return a float value   
print(a // b)  #floor division of two integers, it will return the quotient without the decimal part
print(a % b)  #modulus of two integers, it will return the remainder of the division of a by b  
c = 55.23
d = 12.5 
print(c + d)  #addition of two float numbers
print(c - d)  #subtraction of two float numbers 
print(c * d)  #multiplication of two float numbers
print(c / d)  #division of two float numbers, it will return a float value
print(c // d)  #floor division of two float numbers, it will return the quotient without the decimal part
print(c % d)  #modulus of two float numbers, it will return the remainder 

print(round(c % d,2))  #rounding the result of division of c by d to 2 decimal places

int_1 = "10"
int_2 = "20"

print(int_1+int_2)  #concatenation of two strings, it will return "1020" instead of 30
print(int(int_1) + int(int_2))  #converting the strings to integers using int() function and then adding them, it will return 30


int_3 = -56
int_4 = 90 
print(abs(int_3)+int_4)  #absolute value of int_3, it will return 56   
