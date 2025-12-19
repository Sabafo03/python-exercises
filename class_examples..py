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

# Mesal 1 :
a = 33 # a is type of int
b = 200  # b is type of int
if b > a: # Check if b greater than a
 print("b is greater than a")  # display the result:


# ------------------------------------
# Mesal 2 :
a = 33  # a is type of int
b = 33  # b is type of int
if b > a:  # Check if b greater than a
 print("b is greater than a") 
elif a == b:  # check if a equals b
  print("a and b are equal") # display the result

# ------------------------------------
# Mesal 3 :
a = 200
b = 33
if b > a: # Check if b greater than a
 print("b is greater than a")
elif a == b: # check if a equals b
 print("a and b are equal")
else: # else...
 print("a is greater than b") # display the result

# -----------------------------------
# Mesal 4 :
a = 200
b = 33
if b > a: # Check if b greater than a
 print("b is greater than a")
else:  # else...
 print("b is not greater than a") # display the result

# ------------------------------------
# Mesal 5 :
a = 200
b = 33
c = 500
if a > b and c > a:  # check the both of conditions
 print("Both conditions are True")  # display the result 

# -------------------------------------
# Mesal 6 :
a = 200
b = 33
c = 500
if a > b or a > c: # check the both of conditions
 print("At least one of the conditions is True") # display the result  

# -------------------------------------
# Mesal 7 :
a = 33
b = 200
if not a > b: # check if a > b is not true
 print("a is NOT greater than b")  # display the result

# -------------------------------------
# Mesal 8 :
x = 41
if x > 10: # Check if x greater than 10
 print("Above ten,")
if x > 20: # Check if x greater than 20
 print("and also above 20!")
else: # else...
 print("but not above 20.") # display the result

# -------------------------------------
# Mesal 9 :
score = 85 
if score >= 90:    # Check if score is 90 or more
 print("Grade: A")
elif score >= 80 and score < 90:  # Check if score is 80 and between 80/90
 print("Grade: B")
elif score >= 70:  # Check if score is 70 or more  
 print("Grade: C")
else: # else...   
 print("Grade: F")

# --------------------------------------
# Mesal 10 :
day = 4
match day:  # start match-case
 case 1:  
  print("Monday") # if day == 1
 case 2:
  print("Tuesday") # if day == 2
 case 3:
  print("Wednesday") # if day == 3
 case 4:
  print("Thursday") # if day == 4
 case 5:
  print("Friday") # if day == 5
 case 6:
  print("Saturday") # if day == 6
 case 7:
  print("Sunday") # if day == 7

# ---------------------------------------
# Mesal 11 :
day = 4
match day: # start match-case
 case 6: 
  print("Today is Saturday")  # if day == 6
 case 7:
  print("Today is Sunday")  # if day == 7
 case _:
  print("Looking forward to the Weekend")  # becouse day == 4

# -----------------------------------------
# Mesal 12 :
month = 5
day = 4
match day:  # start match-case
 case 1 | 2 | 3 | 4 | 5 if month == 4:
  print("A weekday in April")  # if day is 1-5 and month is April
 case 1 | 2 | 3 | 4 | 5 if month == 5:
  print("A weekday in May")  # becouse day = 4 and month = 5
 case _:
  print("No match")  # if no other case matches

# ------------------------------------------
# Mesal 13:
i = 1
while i < 6:  # loop while i is less than 6
 print(i)  # display i
 i += 1  # increment i by 1

# ------------------------------------------
# MesaL 14 :
i = 1
while i < 6: # loop while i is less than 6
 print(i)  # display i
 if i == 3: # check if i equals 3
  break  # exit the loop immediately
 i += 1  # increment i by 1

# ------------------------------------------
# MesaL 15 :
i = 0
while i < 6:  # loop while i is less than 6
 i += 1  # increment i by 1
 if i == 3:  # check if i equals 3 
  continue  # skip rest of the loop
 print(i)  # display i

# ------------------------------------------
# MesaL 16 :
i = 1
while i < 6:  # loop while i is less than 6
 print(i)   # display i
 i += 1  # increment i by 1
else:  # else ...
  print("i is no longer less than 6")  # display the result

# ------------------------------------------
# MesaL 17 :
fruits = ["apple", "banana", "cherry"]
for x in fruits:  # loop through each fruit
 print(x)  # display x

# ------------------------------------------
# MesaL 18 :
fruits = ["apple", "banana", "cherry"]
for x in fruits:  # loop through each fruit
 print(x)  # display x
 if x == "banana":  # check if fruit is banana
  break  # stop the loop
 
# ------------------------------------------
# MesaL 19 :
fruits = ["apple", "banana", "cherry"]
for x in fruits:  # loop through each fruit
 if x == "banana":  # check if fruit is banana
  break  # stop the loop
 print(x)  # display x

# --------------------اتمام فصل 4 ----------------------
# Mesal 1:
def greed():  # this is a function
 print("Hello from a function")
greed()  # call the function

#--------------------------------------------
# Mesal 2:
def my_function():  # this is a function
 print("Hello World")  
my_function()   # call the function 
my_function()   # call the function 
my_function()   # call the function 

#--------------------------------------------
# Mesal 3:
def fahrenheit_to_celsius(fahrenheit):  # this is a function
 return (fahrenheit- 32) * 5 / 9         # convert formula
print(fahrenheit_to_celsius(90))         # print result
print(fahrenheit_to_celsius(100))        # print result
print(fahrenheit_to_celsius(77))         # print result

#--------------------------------------------
# Mesal 4:
def greed():  # this is a function
 print('Hello world!')
greed() # call the function
print("outside function") # outside print

#--------------------------------------------
# Mesal 5:
def get_greeting():  # this is a function
 return "Hello from a function" # return string
message = get_greeting() # store return
print(message) # print value

#--------------------------------------------
# Mesal 6:
def get_greeting():  # this is a function
 return "Hello from a function" # return string
print(get_greeting())# print return

#--------------------------------------------
# Mesal 7:
n=10  # n is type of int
if n > 10:  # use pass inside if statement
 pass  # empty body
print('Hello') # call function

#--------------------------------------------
# Mesal 8:
def future_function():  # this is a function
 pass
# this will execute without any action or error
future_function() 

#--------------------------------------------
# Mesal 9:
# function with two arguments
def add_numbers(num1, num2): # this is a function
 sum = num1 + num2  # add numbers
 print("Sum: ", sum)
# function call with two values
add_numbers(5, 4)  # call function

#--------------------------------------------
# Mesal 10:
def greet(name):  # this is a function
 print("Hello", name)  # greet name
# pass argument
greet("John")

#---------------------------------------------
# Mesal 11:
def my_function(name): # name is a parameter
 print("Hello", name)
my_function("Emil") # "Emil" is an argument

#---------------------------------------------
# Mesal 12:
def my_function(fname, lname):  # two parameters
 print(fname + " " + lname)     # combine names
my_function("Emil", "Refsnes")  # call function

#---------------------------------------------
# Mesal 13:
def my_function(name = "friend"):  # this is a function
 print("Hello", name)
my_function("Emil")              # custom value
my_function("Tobias")            # custom value
my_function()                    # default value
my_function("Linus")             # custom value

#---------------------------------------------
# Mesal 14:
def my_function(fruits):  # list parameter
 for fruit in fruits:     # loop items
  print(fruit)            # print item
my_fruits = ["apple", "banana", "cherry"]  #list
my_function(my_fruits)    # call function

#----------------------------------------------
# Mesal 15:
def my_function(person):     # dict parameter
 print("Name:", person["name"]) # access name
 print("Age:", person["age"]) # access age
my_person = {"name": "Emil", "age": 25} # dictionary
my_function(my_person)      # call function


#----------------------------------------------
# Mesal 16:
# declare global variable
message = 'Hello'
def greet():
# declare local variable
 print('Local', message)
greet()
print('Global', message)

#---------------------------------------------
# Mesal 17:
# outside function
def outer():
 message = 'local'
# nested function
 def inner():
# declare nonlocal variable
  nonlocal message
 message = 'nonlocal'
 print("inner:", message)
 inner()
 print("outer:", message)
outer()

#----------------------------------------------
# Mesal 18:
def myfunc():        # outer function
 x = 300
 def myinnerfunc():  # inner function
  print(x)
 myinnerfunc()       # call inner
myfunc()             # call function

#----------------------------------------------
# Mesal 19:
def countdown(n):         # recursive function
 if n <= 0:               # base case
  print("Done!")          # end message
 else:                    # recursive case
  print(n)                # print number
  countdown(n - 1)        # recursive call
countdown(5)              # start recursion

#----------------------------------------------
# Mesal 20:
def factorial(n):         # factorial function
 # Base case
 if n == 0 or n == 1:
  return 1
# Recursive case
 else:
  return n * factorial(n - 1)# recursion
print(factorial(5))
 
#-----------------------------------------------
# Mesal 21:
def fibonacci(n):         # fibonacci function
 if n <= 1:               # base case
  return n                # return n
 else:                    # recursive case
  return fibonacci(n - 1) + fibonacci(n - 2) # recursion
print(fibonacci(7))       # print result

#-----------------------------------------------
# Mesal 22:
name = input("Enter your name: ") # user input
print("Hello, " + name)           # greet user

#----------------------------اتمام فصل 5 ------------------------
# Mesal 1:
class MyClass:        # define class
 x = 5                # class variable
p1 = MyClass()        # create object
print(p1.x)           # access attribute

#------------------------------------
# Mesal 2:
class Person:                     # define class
 def __init__(self, name, age):   # constructor
  self.name = name                # set name
  self.age = age                  # set age
p1 = Person("Emil", 36)           # create object
print(p1.name)                     # print name
print(p1.age)                      # print age

#-----------------------------------
# Mesal 3:
class Person:                     # define class
 def __init__(self, name):         # constructor
  self.name = name                # set name
 def greet(self):                 # define method
  print("Hello, my name is " + self.name) # greeting
p1 = Person("Emil")                # create object
p1.greet()                         # call method

#-----------------------------------
# Mesal 4:
class Calculator:                 # define class
 def add(self, a, b):              # add method
  return a + b                    # return sum
 def multiply(self, a, b):         # multiply method
  return a * b                    # return product
calc = Calculator()                # create object
print(calc.add(5, 3))              # call add
print(calc.multiply(4, 7))         # call multiply

#----------------------------------
# Mesal 5:
class Person:                     # define class
 def __init__(self, name, age):    # constructor
  self.name = name                # set name
  self.age = age                  # set age
p1 = Person("Emil", 36)            # create object
print(p1.name)                     # print name
print(p1.age)                      # print age

#---------------------------------
# Mesal 6:
class Person:                     # define class
 def __init__(self, name):         # constructor
  self.name = name                # set name
 def printname(self):              # define method
  print(self.name)                # print name
p1 = Person("Tobias")              # create object
p2 = Person("Linus")               # create object
p1.printname()                     # call method
p2.printname()                     # call method

#---------------------------------
# Mesal 7:
class Car:                         # define class
 def __init__(self, brand, model): # constructor
  self.brand = brand              # set brand
  self.model = model              # set model
car1 = Car("Toyota", "Corolla")    # create object
print(car1.brand)                  # print brand
print(car1.model)                  # print model

#---------------------------------
# Mesal 8:
class Person:                     # define class
 def __init__(self, name, age):    # constructor
  self.name = name                # set name
  self.age = age                  # set age
 def celebrate_birthday(self):     # define method
  self.age += 1                   # increase age
  print(f"Happy birthday! You are now {self.age}") # message
p1 = Person("Linus", 25)           # create object
p1.celebrate_birthday()            # call method
p1.celebrate_birthday()            # call method

#---------------------------------
# Mesal 9:
class Person:                     # define class
 def __init__(self, name, age):    # constructor
  self.name = name                # set name
  self.age = age                  # set age
p1 = Person("Emil", 36)            # create object
print(p1)                          # print object

#---------------------------------
# Mesal 10:
class Person:                     # define class
 def __init__(self, name, age):    # constructor
  self.name = name                # set name
  self.age = age                  # set age
 def __str__(self):                # string method
  return f"{self.name} ({self.age})" # custom string
p1 = Person("Tobias", 36)          # create object
print(p1)                          # print object

#---------------------------------
# Mesal 11:
class Playlist:                   # define class
 def __init__(self, name):         # constructor
  self.name = name                # playlist name
  self.songs = []                 # empty list

 def add_song(self, song):         # add method
  self.songs.append(song)         # add song
  print(f"Added: {song}")         # confirm add

 def remove_song(self, song):      # remove method
  if song in self.songs:           # check song
   self.songs.remove(song)        # remove song
   print(f"Removed: {song}")      # confirm remove

 def show_songs(self):             # show method
  print(f"Playlist '{self.name}':") # title
  for song in self.songs:          # loop songs
   print(f"- {song}")             # print song

my_playlist = Playlist("Favorites") # create object
my_playlist.add_song("Bohemian Rhapsody") # add song
my_playlist.add_song("Stairway to Heaven") # add song
my_playlist.show_songs()            # show playlist

#---------------------------------
# Mesal 12:
# Mesal 12:
class Person:                     # define class
 def __init__(self, fname, lname): # constructor
  self.firstname = fname          # first name
  self.lastname = lname           # last name
 def printname(self):              # define method
   print(self.firstname, self.lastname) # print name
#Use the Person class to create an object, and then execute the printname method:   
x = Person("John", "Doe")          # create object
x.printname()                      # call method

#---------------------------------
# Mesal 13:
class Student(Person):             # inherit class
 pass                               # no changes
x = Student("Mike", "Olsen")       # create object
x.printname()                      # inherited method

#---------------------------------
# Mesal 14:
class Outer:                       # outer class
 def __init__(self):               # constructor
  self.name = "Outer Class"        # set name
class Inner:                       # inner class
 def __init__(self):               # constructor
  self.name = "Inner Class"        # set name
 def display(self):                # define method
  print("This is the inner class") # display text
outer = Outer()                    # create object
print(outer.name)                  # print name

#---------------------------------
# Mesal 15:
class Car:                         # define class
 def __init__(self, brand, model): # constructor
  self.brand = brand              # set brand
  self.model = model              # set model
 def move(self):                   # move method
  print("Drive!")                 # car action
class Boat:                        # define class
 def __init__(self, brand, model): # constructor
  self.brand = brand              # set brand
  self.model = model              # set model
 def move(self):                   # move method
  print("Sail!")                  # boat action
class Plane:                       # define class
 def __init__(self, brand, model): # constructor
  self.brand = brand              # set brand
  self.model = model              # set model
 def move(self):                   # move method
  print("Fly!")                   # plane action
car1 = Car("Ford", "Mustang")       # Create a Car object
boat1 = Boat("Ibiza", "Touring 20") # Create a Boat object
plane1 = Plane("Boeing", "747")     # Create a Plane object
for x in (car1, boat1, plane1):    # loop objects
 x.move()                          # polymorphism

#---------------------------------
# Mesal 16:
class Vehicle:                    # base class
 def __init__(self, brand, model):# constructor
  self.brand = brand              # set brand
  self.model = model              # set model
 def move(self):                  # move method
  print("Move!")                 # default action
class Car(Vehicle):               # inherit class
 pass                              # no override
class Boat(Vehicle):              # inherit class
 def move(self):                  # override method
  print("Sail!")                 # boat action
class Plane(Vehicle):             # inherit class
 def move(self):                  # override method
  print("Fly!")                  # plane action
car1 = Car("Ford", "Mustang")      # car object
#Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")
#Create a Plane object
for x in (car1, boat1, plane1):    # loop objects
 print(x.brand)                   # print brand
 print(x.model)                   # print model
 x.move()                         # call method

#----------------------------اتمام فصل 6---------------------------
# Mesal 1:
cars = ["Ford", "Volvo", "BMW"]  # list items
x = cars[0]                     # first element
print(x)                        # print value

#----------------------------
# Mesal 2:
import array                    # import module
arr = array.array('i', [1, 2, 3, 4]) # create array
arr.append(5)                   # add element
arr[1] = 10                     # change value
print(arr)                      # print array 

#----------------------------
# Mesal 3:
lst = [1, 2, 3]                 # create list
lst.append(4)                   # add item
print("LIST=",lst)              # print list

import array                    # import module
arr = array.array('i', [1, 2, 3]) # create array
('i', [1, 2, 3])                # array info
arr.append(4)                   # add item
print(arr)                      # print array

import array                    # import module
arr = array.array('i', [1, 2, 3, 4]) # create array
arr.append(5)                   # add item
arr[1] = 10                     # update value
print(arr)                      # print array

#----------------------------
# Mesal 4:
print("Enter your name:")       # prompt text
name = input()                  # user input
print(f"Hello {name}")          # greeting

#---------------------------
# Mesal 5:
name = input("Enter your name:") # name input
print(f"Hello {name}")           # greeting
fav1 = input("What is your favorite animal:") # animal input
fav2 = input("What is your favorite color:")  # color input
fav3 = input("What is your favorite number:") # number input
print(f"Do you want a {fav2} {fav1} with {fav3} legs?") # output

#---------------------------
# Mesal 6:
import math                     # import math
x = input("Enter a number:")    # user input
y = math.sqrt(float(x))         # square root
print(f"The square root of {x} is {y}") # print result

#---------------------------
# Mesal 7:
y = True                        # loop flag
while y == True:                # while loop
 x = input("Enter a number:")   # user input
 try:                           # try block
  x = float(x)                  # convert number
  y = False                     # stop loop
 except:                        # error handling
  print("Wrong input, please try again.") # error message
print("Thank you!")             # end message

#---------------------------
# Mesal 8:
try:                            # try block
 print(x)                       # print variable
except NameError:               # name error
 print("Variable x is not defined") # error message
except:                         # other errors
 print("Something else went wrong") # error message

#---------------------------
# Mesal 9:
try:                            # try block
 print("Hello")                 # print text
except:                         # error block
 print("Something went wrong")  # error message
else:                           # no error
 print("Nothing went wrong")    # success message

#---------------------------
# Mesal 10:
try:                            # try block
 print(x)                       # print variable
except:                         # error block
 print("Something went wrong")  # error message
finally:                        # always run
 print("The 'try except' is finished") # final message

#---------------------------
# Mesal 11:
x = min(5,10,25)                # minimum value
y = max(5,10,25)                # maximum value
print(x)                        # print min
print(y)                        # print max

#---------------------------
# Mesal 12:
x = abs(-7.25)                  # absolute value
print(x)                        # print result

#---------------------------
# Mesal 13:
x = pow(4,3)                    # power calculation
print(x)                        # print result

#---------------------------
# Mesal 14:
import math                     # import math
x = math.sqrt(64)               # square root
print(x)                        # print result

#---------------------------
# Mesal 15:
import math                     # import math
x = math.ceil(1.4)              # round up
y = math.floor(1.4)             # round down
print(x)                        # print ceil
print(y)                        # print floor
#----------------------------اتمام فصل7---------------------------