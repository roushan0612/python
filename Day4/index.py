# TYPES OF LOOPS 
'''  1.FOR LOOP 
Used for iterating over a sequence (like a list, tuple, string, or range).
      -SYNTAX
        for variable in sequence:
          #WRITE LOGIC AND PROGRAM HERE  


  2.WHILE LOOP
Repeats as long as a condition is true.
-SYNTAX
 WHILE COND:
    #WRITE LOGIC AND CODE HERE
'''

#EXAMPLE FOR LOOP
# for i in range():
#         print(i)

# ----Iterating Over a List
eglist = ['first', 'second', 'third']
# for z in eglist:
#       print(z)

# #using range
# for i in range(1,4):
#     print(i)

# #over string
# word = "hello"
# for z in word:
#     print(z)

# over dict
# person = {'name': 'myname', 'age': 5, 'city': 'delhi'}
# for a, val in person.items():
#     print(f"{a}: {val}")

# # using enumerate
# colors = ['red', 'green', 'blue']
# for index, color in enumerate(colors):
#     print(f"Index {index}: {color}")
# #EXAMPLE WHILE LOOP
# num = 0
# while num < 5:
#     print(num)
#     num += 1

# loop control statement
'''break,continue,pass 
'''

#-----function
'''defined using def keyword
-syntax
def myfunc(parameter):
    own logic code
    return value  #optional

default parameter
def myfunc(name="hello"):
    own logic code
    return f"Hello, {name}"  #optional

 Variable-Length Arguments
 two case 
 keyword,non keyword
 *args , **kwargs

 Lambda Functions
 square = lambda x: x ** 2
'''


def mult(a, b):
    """Return the product of a and b."""
    return a * b


square = lambda x: x ** 2
print(square(6))
    
# file handling
#  built-in open() function to open a file.
'''
syntax
open(filename,mode)

modes
'r': Read (default mode)
'w': Write (creates a new file or truncates an existing file)
'a': Append (adds to the end of the file)
'b': Binary mode (e.g., 'rb' for reading binary files)
't': Text mode (default)
'''

with open('day4.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a new line.")
    # print(file.read())

# with open('output.txt', 'w') as file:


# question fibonaci  
"there are many way of doing same task here three solution of checking fibonaci seq"
# 1
def is_fibo(sequence):
    # Handle edge cases
    if len(sequence) < 3:
        return False  # A Fibonacci sequence must have at least 3 numbers

    # Check the Fibonacci condition
    for i in range(2, len(sequence)):
        if sequence[i] != sequence[i - 1] + sequence[i - 2]:
            return False
            
    return True


# recuring   2
def is_fibo_recur(sequence, index=2):
    # Base case: if the index reaches the length of the sequence, it's valid
    if index == len(sequence):
        return True
    
    # Check if the current element is the sum of the two previous elements
    if sequence[index] != sequence[index - 1] + sequence[index - 2]:
        return False
    
    # Recursive call to check the next element
    return is_fibo_recur(sequence, index + 1)

def check_fibo(sequence):
    # Handle edge cases
    if len(sequence) < 3:
        return False  # A Fibonacci sequence must have at least 3 numbers
    
    return is_fibo_recur(sequence)


# by slicing one index  3
def fibos(sequence):
     if len(sequence) < 3:
        return False    #no fibo seq is less than 3 in length
     else: return rfibo(sequence)


def rfibo(sequence):
    if len(sequence) < 3:
        return True
    
    if sequence[2] != sequence[1] + sequence[0]:
        return False
    
    return rfibo(sequence[1:]) #slicing one index from start


seq1 = [0, 1,1]
seq2 = [1, 1, 2, 3, 4, 5, 9]

# now we can test all 
print(is_fibo(seq1))
print(check_fibo(seq1))
print(fibos(seq1))

print(is_fibo(seq2))
print(check_fibo(seq2))
print(fibos(seq2))

# check by changing value of seq1,seq2