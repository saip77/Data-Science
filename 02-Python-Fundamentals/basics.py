#Printing
print("Hello, world!") # Default behavior with newline
print("Hello, world!", end=" ") # Custom behavior without newline
print("This is on the same line as the previous print statement.")

#Variables & Data Types
x = 10
y = 20
z = x + y
print(z, type(z))

#Using f-strings in Python
name = "John"
print(f"Hello, {name}!")

#Using Precision
value = 3.141592653589793
print(f"Pi is approximately {value:.2f}")

#Strings and it's methods
string = " Hi how are you doing? "
print(string.upper())
print(string.lower())
print(string.title())
print(string.strip())
print(len(string))

#Lists
'''
Lists are ordered, changeable collections that can store mixed data types. 
'''
fruits = ["apple", "banana", "orange"]
print(f"Initial list: {fruits}")
fruits.append("grape") 
print(f"After append: {fruits}") #Add an element to the end of the list
fruits.insert(4, "kiwi") 
print(f"After insert: {fruits}") #Add an element at a specific index
removedFruit = fruits.pop(2)
print(f"After pop: {fruits}, and removed fruit: {removedFruit}") #Remove an element from the specific index of the list
removedFruit = fruits.remove("banana")
print(f"After remove: {fruits}, and removed fruit: {removedFruit}") #Remove an element from the list but does'nt return the removed element
fruits.sort()
print(f"After sort: {fruits}") #Sort the list
fruitIndex = fruits.index("kiwi")
print(f"Index of banana: {fruitIndex}")
fruits.extend(["mango", "pineapple"])
print(f"After extend: {fruits}") #Add multiple elements to the end of the list
fruits.clear()
print(f"After clear: {fruits}") #Remove all elements from the list

#Tuples
'''
An ordered, immutable collection of elements.
'''
marks = (10,20,30,40,50)
print(f"Initial tuple: {marks}")
marks += (60,70)
print(f"After append: {marks}") #Add an element to the end of the tuple this does'nt change the original tuple but new tuple is created and the variable now points to the new tuple

'''
Note:A tuple in Python is often called a “frozen list” 
because it's like a list, but you cannot change it once it's created.
'''
print(f"Length of tuple: {len(marks)}")
print(f"Index of 30: {marks.index(30)}")
print(f"Tuple contains 30: {30 in marks}")
print(f"Count of 30: {marks.count(30)}")


#Sets
'''
An unordered collection of unique, mutable items 
used to store multiple items in a single variable. 
'''
colors = {"red", "green", "blue"}
print(f"Initial set: {colors}")
colors.add("yellow")
print(f"After add: {colors}") #Add an element to the set
colors.remove("green")
print(f"After remove: {colors}") #Remove an element from the set but if not found it throws an error
colors.discard("pruple")
print(f"After discard: {colors}") #Remove an element from the set but doesn't throws error if not found
newColors = {"purple", "orange", "yellow"}
additionalColors = colors.union(newColors)
print(f"Union: {additionalColors}") #Union of two sets
commonColors = colors.intersection(newColors)
print(f"Intersection: {commonColors}") #Intersection of two sets
differentColors = colors.difference(newColors)
print(f"Difference: {differentColors}") #Difference of two sets
'''
Note: update() method is used to update the set with the new elements 
while union() is used to create a new set with the union of the two sets.
'''

#Dictionaries
'''
A collection of key-value pairs, where each key is unique.
'''
person = {"name": "John", "age": 30, "city": "New York"}
print(f"Initial dictionary: {person}")
person["age"] = 31
print(f"After update: {person}") #Update the value of a key
person["job"] = "Engineer"
print(f"After update: {person}") #Add a new key-value pair
del person["age"]
print(f"After delete: {person}") #Delete a key-value pair
print(f"Keys: {person.keys()}") #Get all the keys
print(f"Values: {person.values()}") #Get all the values
print(f"Items: {person.items()}") #Get all the key-value pairs

#Taking input from the user
userMarks = int(input("Enter your marks: "))
print(f"Your marks: {userMarks}")

#Conditionals
studentMarks = input("Enter your marks: ") #By default, the variable is a string
studentMarks = int(studentMarks)
if studentMarks >= 60 and studentMarks < 90:
  print("You passed!")
elif studentMarks >= 90:
  print("You are a genius")
else:
  print("You failed")

#Loops
for i in range(1,10):
  print(i)

movies = ["Inception", "Interstellar", "Dune"]
for movie in movies:
  print(movie)

counter=5
while counter > 0:
  print(counter)
  counter -= 1

#Functions
def greet(name):
  print(f"Hello, {name}!")

greetInput = input("Enter your name: ")
greet(greetInput)

def addNumbers(x,y):
  return x + y

result = addNumbers(10,20)
print(result)

#Error Handling
userNumberInput = input("Enter your numbers: ")
try:
  parts = userNumberInput.split(",")
  num1 = int(parts[0])
  num2 = int(parts[1])
  print(f"The sum of {num1} and {num2} is {num1+num2}")
except IndexError:
  print("Error: Please separate your two numbers with a comma.")
except ValueError:
  print("Error: Please enter only numbers.")
except Exception as e:
  print(f"Error: {e}")
finally:
  print("This will always be printed.")

#Maths
x = min(10,20)
y = max(10,20)
print(f"Minimum is {x} and Maximum is {y}")
z = abs(-10)
print(f"Absolute value is {z}")
power = pow(2,3)
print(f"2 to the power of 3 is {power}")

#Slicing and Unpacking
'''
A slice is a way to extract a portion of a sequence
(such as a string or a list) and return a new object.
'''
wholeNumbers = [0,1,2,3,4,5,6,7,8,9,10]
print(wholeNumbers[0:5])    #Returns elements from index 0 to index 4 exluding 5th index
print(wholeNumbers[0:])     #Returns elements from index 0 to the end of the list exluding index 10
print(wholeNumbers[:5])     #Returns elements from the beginning of the list to index 4 exluding 5th index
print(wholeNumbers[::2])    #Returns every second element from the beginning of the list to the end of the list
print(wholeNumbers[1:5:2])  #Returns every second element from index 1 to index 5 exluding 5th index
print(wholeNumbers[::-1])   #Returns the list in reverse order

'''
Unpacking is a way to assign multiple values to multiple variables at once.
'''
point = (10, 20)
x, y = point # x=10, y=20 or point[0]=10, point[1]=20

# The "Star" operator for remainder
first, *middle, last = [1, 2, 3, 4, 5]
# first = 1, middle = [2, 3, 4], last = 5

