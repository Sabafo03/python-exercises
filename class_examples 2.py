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


# ---------------------اتمام فصل دوم -------------------------
# Mesal 1 :
a = ["apple", "banana", "cherry"]  # a is a list
b = ["Ford", "BMW", "Volvo"]  # b is another list
a.append(b)  # add list b as a single element to list a
print(a)  # display a :


# ------------------------------------
# Mesal 2 :
a = ['apple', 'banana', 'cherry'] # a is a list
a.append("orange")  # add orange to the end of the list
print(a)  # display a :


# -----------------------------------
# Mesal 3 :
a = ['apple', 'banana', 'cherry', 'orange']  # a is the list
a.clear() # remove all items from the list
print(a)  # display a :


# ------------------------------------
# Mesal 4 :
a = ['apple', 'banana', 'cherry', 'orange']  # a is a list
x = a.copy()  # make a copy of a and put it in x
print(x)  # display x :


# ------------------------------------
# Mesal 5 :
a = [1, 4, 2, 9, 7, 8, 9, 3, 1]  # a is a list
x = a.count(9)  # count number of 9s in list
print(x)  # display x :


# ------------------------------------
# Mesal 6 :
a = ['apple', 'banana', 'cherry']  # a is a list
b = ['Ford', 'BMW', 'Volvo']  # b is another list
a.extend(b)  # add all items of b to a
print(a)  # display a :


# ------------------------------------
# Mesal  7 :
a = ['apple', 'banana', 'cherry']  # a is a list
x = a.index("cherry")  # find the index of cherry in a
print(x)  # display x :


# ------------------------------------
# Mesal 8 :
a = ['apple', 'banana', 'cherry', 'kiwi', 'mango','orange', 'cherry']  # a is a list
x = a.index("cherry", 4)  # find the index of cherry in a starting from index 4
print(x)  # display x :


# ------------------------------------
# Mesal 9 :
a = ['apple', 'banana', 'cherry']  # a is a list
a.insert(1, "orange")  # insert orange at index 1 in the list
print(a)  # display a :


# -------------------------------------
# Mesal 10 :
a = ['apple', 'banana', 'cherry']  # a is a list
a.pop(1)  # remove and retuen the item at index 1
print(a)  # display a :


# -------------------------------------
# Mesal 11 :
my_list = [10, 20, 30]  # my_list is a list
x = my_list.pop() # remove and return the last item
print(my_list)  # display updated list  :
print(x)  # display x :


# -------------------------------------
# Mesal 12 :
fruits = ['apple','banana','cherry']  # fruits is a list
fruits=fruits.pop(1)  # remove and return item at index 1 and put it in fruits
print(fruits)  # display fruits :


# ------------------------------------
# Mesal 13 :
a = ['apple','banana','cherry','banana']  # a is a list
a.remove("banana") # remove banana from list
print(a)  # display a :


# ------------------------------------
# Mesal 14 :
a = [1, 2, 3] # a is a list
del a[1]  #del index 1  
print (a)  # display a :


# ------------------------------------
# Mesal 15 :
a = ['apple', 'banana', 'cherry']  # a is a list
a.reverse()  # reverse the list
print(a)  # display a :


# ------------------------------------
# Mesal 16 :
a = ['Ford', 'BMW', 'Volvo']  # a is a list
a.sort()  # sort the list
print(a)  # display a :


# -------------------------------------
# Mesal 17 :
a = ("apple", "banana", "cherry", "apple", "cherry")  # a is a tuple
print(a)  # display a :


# -------------------------------------
# Mesal 18 :
A = tuple(("apple", "banana", "cherry")) 
# note the double round brackets
print(A)  # display A :


# -------------------------------------
# Mesal 19 :
a = [1, 2, 3]  # a is a list
b = tuple(a)  # convert list to a tuple
print(b)  # display b :


# -------------------------------------
# Mesal 20 :
a = ("apple", "banana", "cherry")  # a is a tuple
print(a[1]) # Access tuple item by index
print(a[-1])  # Access the last item ussing negative index


# -------------------------------------
# Mesal 21 :
A = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango") # A is a tuple
print(A[2:5])  # ازاندیس شماره 2 تا 4 این تاپل رو چاپ کن.
print(A[:4])   # از ابتدا تا اندیس شماره 3 رو چاپ کن
print(A[-4:-1])  # از اندیس -4 تا اندیس -2 رو چاپ کن


# --------------------------------------
# Mesal 22 :
A = ("apple", "banana", "cherry")
if "apple" in A:
    print("Yes, 'apple' is in the fruits tuple") # بررسی کن این مقدار در تاپل وجود دارد؟


# ---------------------------------------
# Mesal 23 :
x = ("apple", "banana", "cherry")
y = list(x)  # تبدیل تاپل به لیست
y[1] = "kiwi"  # تغییر مقدار لیست
x = tuple(y)
print(x)


# ----------------------------------------
# Mesal 24 :
a = ("apple","banana", "cherry")
y =list(a)  # تبدیل تاپل به لیست
y.append("orange")  # اضافه کردن آیتم به لیست
a=tuple(y)  # تبدیل لیست به تاپل
print(a)


# ----------------------------------------
# Mesal 25 :
thistuple = ("apple", "banana", "cherry")
y = ("orange",) 
thistuple += y  # ترکیب دو تاپل و افزودن مقدار جدید به تاپل اصلی
print(thistuple)


# -----------------------------------------
# Mesal 26 :
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)  # تبدیل تاپل به لیست
y.remove("apple")  # حذف آیتم از لیست
thistuple = tuple(y)  # تبدیل لیست به تاپل
print(thistuple)  # چاپ


# ------------------------------------------
# 27 :
fruits = ("apple", "banana", "cherry")  # fruits is a tuple
print(fruits)  # تاپل را چاپ کن.


# -------------------------------------------
# 28 :
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits  # اختصاص دادن یک متغیر به هر آیتم تاپل
print(green)
print(yellow)
print(red)


# --------------------------------------------
# 29 :
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits  # با استفاده از ستاره آیتم باقی مانده به صورت لیست به یک متغیر اختصاص می یابد
print(green)
print(yellow)
print(red)


# --------------------------------------------
# 30 :
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits  # به جز آیتم های اول و آخر بقیه با استفاده از ستاره به صورت لیست به متغیر وسطی اختصاص داده میشود
print(green)
print(tropic)
print(red)


# -----------------------------------------------
# 31 :
thistuple = ("apple", "banana", "cherry")
for x in thistuple : # پیمایش ایتم های تاپل با حلقه فور
   print(x)


# ------------------------------------------------
# 32 :
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2  # ترکیب دو تاپل و ساخت تاپل جدید
print(tuple3)


# ------------------------------------------------
# 33 :
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2  # ایجاد یک تاپل جدید با تکرار دو بار آیتم های تاپل 
print(mytuple)


#-------------------------------------------------
# 34 :
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)  # شمارش تغداد دفعات عدد 5 در تاپل
print(x)


# ----------------------------------------------------
# 35 :
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)  # پیدا کردن اولین اندیس عدد 8 در تاپل
print(x)


# -----------------------------------------------------
# 36 :
thisset= {"apple","banana", "cherry"}
print(thisset)  # چاپ یک مجموعه شامل سه میوه


# ------------------------------------------------------
# 37 :
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) # ساخت مجموعه با استفاده از تابع set و دو پرانتز


# ------------------------------------------------------
# 38 :
myset = {"apple", "banana", "cherry"}
print(type(myset))  #  نمایش نوع داده ی myset


# -------------------------------------------------------
# 39 :
thisset= {"apple","banana", "cherry"} 
for x in thisset:
   print(x)  # پیمایش و چاپ هر آیتم مجموعه


# -------------------------------------------------------
# 40 :
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")  # افزودن یک آیتم به مجموعه
print(thisset)


# -------------------------------------------------------
# 41 :
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)  # اضافه کردن چند آیتم از مجموعه دیگر
print(thisset)


# -------------------------------------------------------
# 42 :
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)  # اضافه کردن چند آیتم از لیست
print(thisset)


# --------------------------------------------------------
# 43 :
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")  # حذف یک آیتم از مجموعه
print(thisset)


# --------------------------------------------------------
# 44 :
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")  # حذف یک /آیتم بدون خطا اگر موجود نباشد
print(thisset)


# --------------------------------------------------------
# 45 :
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()  # حذف و برگرداندن یک آیتم تصادفی
print(x)
print(thisset)


# --------------------------------------------------------
# 46 :
thisset = {"apple", "banana", "cherry"}
thisset.clear()  # پاک کردن همه ی آیتم های مجموعه
print(thisset)


# ----------------------------------------------------------
# 47 :
thisset = {"apple", "banana", "cherry"}
for x in thisset:
 print(x)  # پیمایش و چاپ هر آیتم مجموعه


# ----------------------------------------------------------
# 48 :
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)  # ادغام دو مجموعه و ساخت مجموعه جدید
print(set3)


# ----------------------------------------------------------
# 49 :
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2  # ادغام دو مجموعه با عملگر
print(set3)


# ---------------------------------------------------------
# 50 :
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)  # ادغام مجموعه با تاپل
print(z)


# ---------------------------------------------------------
# 51 :
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)  # افزودن آیتم های مجموعه دیگر به مجموعه موجود
print(set1)


# ---------------------------------------------------------
# 52 :
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)  # گرفتن اشتراک دو مجموعه
print(set3)


# ----------------------------------------------------------
# 53 :
mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)  # ساخت مجموعه ثابت و بدون تغییر
print(x)


# ----------------------------------------------------------
# 54 :
thisdict = {
 "brand": "Ford",
 "model": "Mustang",
 "year": 1964
 }
print(thisdict)  # چاپ کل دیکشنری


# -----------------------------------------------------------
# 55 :
thisdict = {
 "brand": "Ford",
 "model": "Mustang",
 "year": 1964
 }
print(thisdict["brand"])  # چاپ مقدار کلید brand


# -----------------------------------------------------------
# 56 :
thisdict = dict(name = "John", 
age= 36,country= "Norway")
print(thisdict)  # چاپ کل دیکشنری ساخته شده با dict 


# ------------------------------------------------------------
# 57 :
thisdict = {
 "brand": "Ford",
 "model": "Mustang",
 "year": 1964
 }
x = thisdict["model"]  # گرفتن مقدار کلید model 
" model "
print(x)


# ----------------------------------------------
# 58 :
thisdict = {
 "brand": "Ford",
 "model": "Mustang",
 "year": 1964
 }
x = thisdict.get("model")  # گرفتن مقدار کلید با متد get 
print(x)


# ---------------------------------------------
# 59 :
thisdict = {
 "brand": "Ford",
 "model": "Mustang",
 "year": 1964
 }
x = thisdict.keys()  # گرفتن همه ی کلیدهای دیکشنری
print(x)


# ----------------------------------------------
# 60 :
car = {
"brand": "Ford",
 "model": "Mustang",
 "year": 1964
 }
x = car.keys()
print(x) #before the change
car["color"] = "white" # افزودن کلید جدید
print(x) #after the change
print (car)  # چاپ دیکشنری کامل


# ----------------------------------------------
# 61 :
thisdict = {
 "brand": "Ford",
 "model": "Mustang",
 "year": 1964
 }
x = thisdict.values()  # گرفتن همه مقادیر دیکشنری
print(x)


# ------------------------------------------------
# 62 :
thisdict = {
 "brand": "Ford",
 "model": "Mustang",
 "year": 1964
 }
x = thisdict.items()  # گرفتن همه ی کلید-مقدار ها به صورت tuple 
print(x)


# ------------------------------------------------
# 63 :
thisdict = {
 "brand": "Ford",
 "model": "Mustang",
 "year": 1964
  }
if "model" in thisdict:  # بررسی وجود کلید 'model'
 print("Yes, 'model' is one of the keys in the thisdict dictionary")


 # -------------------------------------------------
 # 64 :
thisdict = {
 "brand": "Ford",
 "model": "Mustang",
 "year": 1964
 }
thisdict.update({"year": 2020})  # بروزرسانی مقدار کلید 'year'
print(thisdict)


# ---------------------------------------------------
# 65 :
thisdict = {
 "brand": "Ford",
 "model": "Mustang",
 "year": 1964
 }
thisdict["color"] = "red"  # اضافه کردن کلید حدید 'color'
print(thisdict)


# --------------------------------------------------
# 66 :
thisdict = {
 "brand": "Ford",
 "model": "Mustang",
 "year": 1964
 }
thisdict.pop("model")  # حذف کلید 'model'
print(thisdict)


# --------------------------------------------------
# 67 :
thisdict = {
 "brand": "Ford",
 "model": "Mustang",
 "year": 1964
 }
thisdict.popitem()  # حذف آخرین جفت کلید-مقدار
print(thisdict)


# --------------------------------------------------
# 68 :
thisdict = {
 "brand": "Ford",
 "model": "Mustang",
 "year": 1964
 }
del thisdict["model"]  # حذف کلید 'model'
print(thisdict)


# ---------------------------------------------------
# 69 :
thisdict = {
 "brand": "Ford",
 "model": "Mustang",
 "year": 1964
 }
thisdict.clear()  # پاک کردن تمتم محتویات دیکشنری
print(thisdict)


# ----------------------------------------------------
# 70 :
thisdict = {
 "brand": "Ford",
 "model": "Mustang",
 "year": 1964
 }
for x in thisdict:  # پیمایش کلیدها
 print(thisdict[x])  # چاپ مقدار هر کلید


 # -----------------------------------------------------
 # 71 :
thisdict = {
 "brand": "Ford",
 "model": "Mustang",
 "year": 1964
 }
for x in thisdict:  # پیمایش کلیدها
 print(x)  # چاپ کلیدها


 # -----------------------------------------------------
 # 72 :
thisdict = {
 "brand":"Ford",
 "model":"Mustang",
 "year":1964 
 }
for x in thisdict:  # پیمایش کلیدها
  print(x,thisdict[x])  # چاپ کلید و مقدار


# -------------------------------------------------------
# 73 :
thisdict = {
 "brand": "Ford",
 "model": "Mustang",
 "year": 1964
 }
for x in thisdict.values():  # پیمایش مقادیر
 print(x)  # چاپ مقدار


# --------------------------------------------------------
# 74 :
thisdict = {
 "brand": "Ford",
 "model": "Mustang",
 "year": 1964
 }
for x in thisdict.keys():  # پیمایش کلید ها
 print(x)  # چاپ کلید


# --------------------------------------------------------
# 75 :
thisdict = {
 "brand": "Ford",
 "model": "Mustang",
 "year": 1964
 }
for x, y in thisdict.items():  # پیمایش کلید-مقدار
 print(x, y)  # چاپ کلید و مقدار


# -------------------------------------------------------
# 76 :
thisdict = {
 "brand": "Ford",
 "model": "Mustang",
 "year": 1964
 }
mydict = dict(thisdict)  # کپی دیکشنری با dict
print(mydict)


# ------------------------------------------------------
# 77 :
thisdict = {
 "brand": "Ford",
 "model": "Mustang",
 "year": 1964
 }
mydict = thisdict.copy()   # کپی دیکشنری با متد کپی
print(mydict)


# -----------------------------------------------------
# 78 :
myfamily = {
 "child1" : {
 "name" : "Emil",
 "year" : 2004
 },
 "child2" : {
 "name" : "Tobias",
 "year" : 2007
 },
 "child3" : {
 "name" : "Linus",
 "year" : 2011
 }
}
print(myfamily)  # چاپ دیکشنری تو در تو


#-------------------------------------------------
# 79 :
child1 = {
 "name" : "Emil",
 "year" : 2004
 }
child2 = {
 "name" : "Tobias",
 "year" : 2007
 }
child3 = {
 "name" : "Linus",
 "year" : 2011
 }
myfamily = {
 "child1" : child1,
 "child2" : child2,
 "child3" : child3
 }
print(myfamily)  # چاپ دیکشنری با دیکشنری های داخلی


# --------------------------------------------
# 80 :
child1 = {
 "name" : "Emil",
 "year" : 2004
 }
child2 = {
 "name" : "Tobias",
 "year" : 2007
 }
child3 = {
 "name" : "Linus",
 "year" : 2011
 }
print( myfamily ["child2"]["name"])  # دسترسی به مقدار داخل دیکشنری تو در تو


# -----------------------------------------------
# 81 :
myfamily = {
 "child1" : {
 "name" : "Emil",
 "year" : 2004
 },
 "child2" : {
 "name" : "Tobias",
 "year" : 2007
 },
 "child3" : {
 "name" : "Linus",
 "year" : 2011
 },
}
for x, obj in myfamily.items():  # پیمایش کلید و دیکشنری داخلی
 print(x)  # چاپ کلید اصلی
 for y in obj:  # پیمایش کلید های داخلی
   print(y + ':', obj[y])  # چاپ کلید و مقدار داخلی


#----------------------------------اتمام فصل 3------------------------------------

