#what is dictionary in python?
#A dictionary is a collection of key-value pairs which are unordered, changeable and indexed. It allows duplicate members. The keys must be unique and immutable, while the values can be of any data type.
#how to create a dictionary in python

my_dict = {"name": "Gyan", "age": 25, "city": "Hyderabad"}  #creating a dictionary with string keys and values of different data types
print(my_dict)

my_dict_2 = {1: "apple", 2: "banana", 3: "cherry"}  #creating a dictionary with integer keys and string values
print(my_dict_2)    

#how to access values in a dictionary
print(my_dict["name"])  #accessing the value of the key "name" in the dictionary my_dict
print(my_dict["age"])  #accessing the value of the key "age" in the dictionary my_dict
print(my_dict["city"])  #accessing the value of the key "city" in the dictionary my_dict


#how to add a new key-value pair to a dictionary
my_dict["country"] = "India"  #adding a new key-value pair to the dictionary my_dict
print(my_dict)

#how to update the value of an existing key in a dictionary
my_dict["age"] = 26  #updating the value of the key "age" in the dictionary my_dict
print(my_dict)

#how to get all the keys in a dictionary
print(my_dict.keys())  #getting all the keys in the dictionary my_dict

#how to get all the values in a dictionary
print(my_dict.values())  #getting all the values in the dictionary my_dict

#how to get all the key-value pairs in a dictionary
print(my_dict.items())  #getting all the key-value pairs in the dictionary my_dict

#how to remove a key-value pair from a dictionary
del my_dict["city"]  #removing the key-value pair with key "city" from the dictionary my_dict
print(my_dict)

