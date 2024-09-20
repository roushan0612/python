# keywords  cannot used as indentifier
# and	--------A logical operator
# as	--------To create an alias
# assert --------For debugging
# break	-------To break out of a loop
# class ---------	To define a class
# continue	-----To continue to the next iteration of a loop
# def	----To define a function
# del	-----To delete an object
# elif	-----in conditional statements, same as else if
# else	-------- in conditional statements
# except-----	Used with exceptions, what to do when an exception occurs
# False-----	Boolean value, result of comparison operations
# finally-----	Used with exceptions, a block of code that will be executed no matter if there is an exception or not
# for	-----To create a for loop
# from	-----To import specific parts of a module
# global-----	To declare a global variable
# if	-----To make a conditional statement
# import	-----To import a module
# in	-----To check if a value is present in a list, tuple, etc.
# is	-----To test if two variables are equal
# lambda	-----To create an anonymous function
# None	-----Represents a null value
# nonlocal	-----To declare a non-local variable
# not	-----A logical operator
# or	-----A logical operator
# pass	-----A null statement, a statement that will do nothing
# raise	-----To raise an exception
# return	-----To exit a function and return a value
# True	-----Boolean value, result of comparison operations
# try	-----To make a try...except statement
# while	-----To create a while loop
# with	-----Used to simplify exception handling
# yield-----To return a list of values from a generator
# -------------------
# array   const
# ----------------------
# reset = '\033[0m'
bold = '\033[01m'
# disable = '\033[02m'
# underline = '\033[04m'
# reverse = '\033[07m'
# strikethrough = '\033[09m'
# invisible = '\033[08m'
fg_green = '\033[32m'
reset = '\033[0m'
bold = '\033[01m'
fg_yellow = '\033[93m'
fg_blue = '\033[34m'
# fg:
#         black = '\033[30m'
#         red = '\033[31m'
#         green = '\033[32m'
#         orange = '\033[33m'
#         blue = '\033[34m'
#         purple = '\033[35m'
#         cyan = '\033[36m'
#         lightgrey = '\033[37m'
#         darkgrey = '\033[90m'
#         lightred = '\033[91m'
#         lightgreen = '\033[92m'
#         yellow = '\033[93m'
#         lightblue = '\033[94m'
#         pink = '\033[95m'
#         lightcyan = '\033[96m'
#  bg:
#         black = '\033[40m'
#         red = '\033[41m'
#         green = '\033[42m'
#         orange = '\033[43m'
#         blue = '\033[44m'
#         purple = '\033[45m'
#         cyan = '\033[46m'
#         lightgrey = '\033[47m'

# syntax
# if True:
#     pass
# if True: print("true")

# if cond:
#   print("true")
# --------
# if cond:
#   print("true")
# else:
#   print("true default if not cond meet")
# --------
# if cond:
#   print("true")
# elif cond:
#   print("print true if above is false")
# ---------
# if cond:
#   print("true")
# elif cond:
#   print("print true if above is false")
# else:
#   print("true default if not cond meet")

# print("true") if cond else print("else")



# def cfun():
#   print("test function")


# question 
# palindrome
# Fibonacci
# hacking screen
# creating result from marksheet
# VGF=12
# VGF=13
# print(VGF)   #false constant

# str1="first"
# print("str1 id , value",id(str1),str1)
# str1="second"
# print("str1 id , value",id(str1),str1)
a=5
b=2
res=a/b
res2=a//b
res3=a%b
# print("complete division",res,type(res))
# print("floor division",res2,type(res2))
# print("remainder",res3,type(res3))
# print("division result {a}{b}".format(b="df",a="ty"))
strq=f"{bold}{fg_blue}division result {reset}\n{fg_green}complete div {fg_yellow}{res}\n{fg_green}floor div {fg_yellow}{res2}\n{fg_green}remainder {fg_yellow}{res3}{reset}"
print(strq)
