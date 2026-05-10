# what  is list in python
# list is a collection of items which are ordered and changeable. It allows duplicate members.  
# how to create a list in python
my_list = [1, 2, 3, 4, 5]  #creating a list of integers
print(my_list) 

my_list_2 = ["apple", "banana", "cherry"]  #creating a list of strings
print(my_list_2)

my_list_3 = [1, "apple", 3.14, True]  #creating a list of mixed data types
print(my_list_3)

# how to access elements in a list
print(my_list[0])  #accessing the first element of the list using indexing, it will return 1
print(my_list_2[1])  #accessing the second element of the list using indexing, it will return "banana"


# how to modify elements in a list
my_list[0] = 10  #modifying the first element of the list to 10
print(my_list)

# Methods on list
my_list.append(6)  #appending the element 6 to the end of the list
print(my_list)

my_list.insert(0, 0)  #inserting the element 0 at index 0 of the list
print(my_list)

my_list.remove(3)  #removing the element 3 from the list
print(my_list)

poped = my_list.pop()  #removing the last element of the list and storing it in variable poped
print(poped)  #printing the popped element, it will return 6

my_list_4 = [4,5,6,7,9]

my_list.extend(my_list_4) #extending the list my_list with the elements of my_list_4
print(my_list)


"""Important point to note is that extend() method insterts the elements of the sceond list one by one
to first list, where as insert will insert the second list as a single element to first list at specific index."""

#How to sort any given list in ascending order
my_list.sort()  #sorting the list in ascending order
print(my_list)

#How to sort any given list in descending order
my_list.sort(reverse=True)  #sorting the list in descending order

#above all sorting methods are in place sorting.

#How to get the sorted list without modifying the original list
sorted_list = sorted(my_list)  #getting the sorted list without modifying the original list
print(sorted_list)


#How to reverse the order of the list
my_list.reverse()  #reversing the order of the list
print(my_list)

#above is the inplace reversing of list.

#How to get the reversed list without modifying the original list
reversed_list = list(reversed(my_list))  #getting the reversed list without modifying the original list
print(reversed_list)


#how to do slice operation on list
my_list_5 = [1,2,3,4,5,6,7,8,9]
print(my_list_5[0:5])  #accessing the first 5 elements of the list using slicing
print(my_list_5[5:])  #accessing the last 4 elements of the list using slicing
print(my_list_5[:5])  #accessing the first 5 elements of the list using slicing




# tuple is a collection of items which are ordered and unchangeable. It allows duplicate members.
# how to create a tuple in python
my_tuple = (1, 2, 3, 4, 5)  #creating a tuple of integers
print(my_tuple)

my_tuple_2 = ("apple", "banana", "cherry")  #creating a tuple of strings
print(my_tuple_2)

my_tuple_3 = (1, "apple", 3.14, True)  #creating a tuple of mixed data types
print(my_tuple_3)

# how to access elements in a tuple
print(my_tuple[0])  #accessing the first element of the tuple using indexing,



# set is a collection of items which are unordered and unindexed. It does not allow duplicate members.
# how to create a set in python
my_set = {1, 2, 3, 4, 5}  #creating a set of integers
print(my_set)

my_set_2 = {"apple", "banana", "cherry"}  #creating a set of strings
print(my_set_2)

my_set_3 = {1, "apple", 3.14, True}  #creating a set of mixed data types
print(my_set_3)

# how to access elements in a set
# we cannot access elements in a set using indexing as sets are unordered and unindexed, but we can check if an element is present in the set using in keyword
print(3 in my_set)  #checking if 3 is present in the set my_set, it will return True
print("banana" in my_set_2)  #checking if "banana" is present in the set my_set_2, it will return True

