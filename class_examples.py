# Mesal 1 :
# Print Hello World in python
print("Hello, World!")


# ----------------------
# Mesal 2 :
# Check if Five greater than Two 
if 5 > 2:
# print the result   
    print("Five greater than Two")


# ----------------------
# Mesal 3 :
# x is type of int
x = 3    
# y is type of str
y = "Saba"  
# Display x 
print(x)
# Display y 
print(y)  


# ----------------------
# Mesal 4 : 
# x is type of int
x = 7  
# x is now type of str
x = "Teacher"
# Display x :
print(x)


# ----------------------
# Mesal 5 :
# x is type of int
x = 2
# y is type of str
y = "Saba"
# Display x 
print(x)
# Display y
print(y)
# Display the data type of x 
print(type(x))
# Display the data type of y 
print(type(y))


# ----------------------
# Mesal 6 :
# x is type of str
x = "Saba"
#You can use double or single quotes
x = 'Saba'
# Display x
print(x)


# ----------------------
# Mesal 7 :
A = 8
a = "Saba"
 #A will not overwrite a
# Display A
print(A)
# Display a
print(a)


# -----------------------
# Mesal 8 : 
# x, y, z are type of str
x, y, z = "Rose", "Sunflower", "lilium"
# Display x
print(x)
# Display y
print(y)
# Display z
print(z)


# -----------------------
# Mesal 9 : 
# X = y = z = are same type of str
x = y = z = "Rose"
# Display x
print(x)
# Display y
print(y)
# Display z
print(z)


# -----------------------
# Mesal 10 : 
# list of the flower names
Flowers = ["Rose", "Sunflower", "Lilium"]
# unpack the list to x, y, z:
x, y, z = Flowers
# Display x
print(x)
# Display y
print(y)
# Display z
print(z)


# -----------------------
# Mesal 11 : 
# x is type of str
x = "Python"
# y is type of str
y = "is"
# z is type of str
z = "awesome"
# Display x, y, z separated by spaces
print(x, y, z)
# Concatenate x, y, z and display the result without spaces
print(x + y + z)


# -----------------------
# Mesal 12 : 
# x is type of int
x = 3
# y is type of int
y = 9
# Display the result of x + y
print(x + y)


# ------------------------
# Mesal 13 : 
# x is type of int
x = 5
# y is type of str
y = "Saba"
# Display x and y togheter
print(x, y)


# ------------------------
# Mesal 14 :
# x is type of str
x = "awesome"
def myfunc():
  x = "fantastic"
  # x inside the function
  print("Python is " + x)  # display x inside the function
myfunc() #call the function
print("Python is " + x)  # display x outside the function 



# ------------------------
# mesal 15 :
x = "awesome"  # x is global
def myfunc():
  global x   # tell python to use global
  x = "fantastic"   # change the global variable
myfunc()  # call the function
# print the update global variable
print("Python is " + x)


# ------------------اتمام فصل اول--------------------

# Mesal 1 :
x = 5
# Display the data type of x
print(type(x))


# ------------------------
# Mesal 2 :
x = "Hello World"
#display x:
print(x)
#display the data type of x:
print(type(x))


# ------------------------
# Mesal 3 :
x = 10
#display x:
print(x)
#display the data type of x:
print(type(x))


# ------------------------
# Mesal 4 :
x = ["Rose", "Sunflower", "Lilium"]
 #display x:
print(x)
 #display the data type of x:
print(type(x))


# --------------------------
# Mesal 5 :
x = frozenset({"Rose", "Sunflower", "Lilium"})
#display x:
print(x)
#display the data type of x:
print(type(x))


# --------------------------
# Mesal 6 :
x = str("Hello World")
#display x:
print(x)
#display the data type of x:
print(type(x))


# ---------------------------
# Mesal 7 :
x = int(20)
#display x:
print(x)
#display the data type of x:
print(type(x))


# ---------------------------
# Mesal 8 :
x = list(("Rose", "Sunflower", "Lilium"))
#display x:
print(x)
#display the data type of x:
print(type(x))


# ----------------------------
# Mesal 9 :
x = bool(7)
#display x:
print(x)
#display the data type of x:
print(type(x))


# -----------------------------
# Mesal 10 :
x = 6  #int
y = 5.5  #float
z = 7j  #complex
print(type(x))  #display the data type of x:
print(type(y))  #display the data type of y:
print(type(z))  #display the data type of x:


# ------------------------------
# Mesal 11 :
#convert from int to float:
x = float(8)
#convert from float to int:
y = int(2.5)
#convert from int to complex:
z = complex(6)
print(x)  #display x:
print(y)  #display y:
print(z)  #display z:
print(type(x))  #display the data type of x:
print(type(y))  #display the data type of y:
print(type(z))  #display the data type of z:


# ------------------------------
# Mesal 12 :
#convert x, y, z to int:
x = int(3)
y = int(7.89)
z = int("7")
print(x)  #display x:
print(y)  #display y:
print(z)  #display z:


# ------------------------------
# Mesal 13 :
#convert x, y, z to float:
x = float(3)
y = float(7.89)
z = float("7")
print(x)  #display x:
print(y)  #display y:
print(z)  #display z:


# ------------------------------
# Mesal 14 :
#convert x, y, z to str:
x = str(3)
y = str(7.89)
z = str("d7")
print(x)  #display x:
print(y)  #display y:
print(z)  #display z:


# --------------------------------
# Mesal 15 :
print("It's alright")   
print("she is called 'Saba' ") # quotes can be used inside strings if they don't conflict
print('she is called "Saba" ')


# ---------------------------------
# Mesal 16 :
# triple single or double quotes can be used to assign a mujti-line string to a veriable
A = """python is fun, I enjoy learning it everyday. it helps me solve problems."""
a = '''python is fun, I enjoy learning it everyday. it helps me solve problems.'''
print(A)
print(a)


# ----------------------------------
# Mesal 17 :
# a is type of str
a = "Hello, World!"
print(a[8])  # print the eighth character of the str


# -----------------------------------
# Mesal 18 :
for x in "Hello, World!":
   print(x) # loop through each character in the string and print it


#------------------------------------
# Mesal 19 :
# a is type of str
a = "Hello, World!"
print(len(a))  #print the length of the string


# ------------------------------------
# Mesal 20 :
a = "python is fun!"
print("python" in a)  # check if "python" is in the string and print True or False


# -------------------------------------
# Mesal 21 :
# b is type of str
b = "python is fun!"
print(b[4:9])  # print characters from index 4 to 8
print(b[:3])   # print characters from start to index 2
print(b[7:])   # print characters from index 7 to the end
print(b[-3:-1]) # print characters from third-last to second last


# -------------------------------------
# Mesal 22 :
# a is type of str
a = "Hello, World!"
# convert all letters to uppercase
print(a.upper())
# convert all letters ti lowercase
print(a.lower())
# remove extra spaces from the beginning and end
print(a.strip())
# replace part of string with another text
print(a.replace("W", "H"))
# split the string by spaces
b = a.split(",")
print(b)


# ---------------------------------------
# Mesal 23 :
a = "Python"   # a is type of str
b = "IS"    # b is type of str
c = "Perfect"  # c is type of str
d = a + b + c   # concatenate strings without spaces in d
print(d)  # display d :
e = a + " " + b + " " + c    # concatenate strings with spaces in e
print(e)  # display e :


# ---------------------------------------
# Mesal 24 :
name = "Saba" # name is type of str
age = 22  # age is type of int
A = f"Hello, I'm {name} and I'm {age} years old."  # use f-string to insert name and age
print(A)  # display A :


# ---------------------------------------
# Mesal 25 :
x = 5  # x is type of int
y = 9  # y is type of int
A = f"The sum of {x} and {y} is {x + y}." # use f-string to insert variables
print(A)  # display A :


# ---------------------------------------
# Mesal 26 : 
a = 'I\'m fine'    # use backslash to escape single quote
b = "I am\t fine"  # use tab space 
c = "I am \b fine" # use backspace
d = "I am \r fine" # use carriage return
e = "I am\n fine"  # use new line
f = "I am fine\\"  # use backslash character
print(a)  # display a :
print(b)  # display b :
print(c)  # display c :
print(d)  # display d :
print(e)  # display e :
print(f)  # display f :


# --------------------------------------
# Mesal 27 :
x = 150  # x is type of int
y = 250  # y is type of int
if x > y: # check if x is greater than y
  print("x is greater than y")  # print if x > y
else:  # otherwise
  print("x is not greater than y")  # print if x <= y


# ------------------------------------
# Mesal 28 :
x = 200  # x is type of int
print(isinstance(x, int))  # check if x is an int


# ------------------------------------
# Mesal 29 :
x = 15
y = 3
z = 4
a = 5
print(y + z)   # addition
print(x / y)   # division
print(x // z)  # floor division
print(x - y)   # subtraction
print(a * z)   # multiplication
print(y ** z)  # exponentiation


# -------------------------------------
# Mesal 30 :
x = 6  
print(x)  # display x :
x += 9    # add 9 to x ( x = x + 9 )
print(x)  # display updated x :


# ------------------------------------
# Mesal 31 :
x = 3
y = 2
print(x == y)  # equal
print(x != y)  # not equal
print(x >= y)  # greater than or equal


# ------------------------------------
# Mesal 32 :
x = 2
print(x > 3 and x < 10)  # and
print(x > 3 or x < 4)  # OR
print(not(x > 3 and x < 10))  #NOT


# -------------------------------------
# Mesal 33 :
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
 # returns True because z is the same object as x
print(x is y)
 # returns False because x is not the same object as y, even if they have the same content
print(x == y)
# returns True because x equals y
print(x is not z)
 # returns False because z is the same object as x
print(x is not y)
 #returns True because x is not the same object as y, even if they have the same content
print(x != y)
# returns False because x equals y


# -------------------------------------
# Mesal 34 :
x = ["apple", "banana"]  # x is list of fruits
print("banana" in x)  # chech if banana is in the list
print("cherry" in x)  # chech if cherry is in the list


# ------------------------------------
# Mesal 35 :
print(6 & 3)  # bitwise AND
print(6 | 3)  # bitwise OR


# ------------------------------------
# Mesal 36 :
print((6 + 3) - (6 + 3))  # arithmetic: addition then subtraction


# ---------------------اتمام فصل دوم --------------------------