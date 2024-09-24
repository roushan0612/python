class test:
    def __init__(self, parameters):
        # This is the constructor method
        self.attribute1 = parameters
        self.attribute2 = "a"

    def intro(self):
        # This is a regular method
        print(self.attribute1)

"inheritence"

class test2(test):
    def intro(self):
        print("from tes2")


# @classmethod and @staticmethod

"we can use above @classmethod decorator to create method that can modify class attribute directly "
'and @staticmethod to create a static method'
class test3:
    name="a"
    def __init__(self, parameters):
        # This is the constructor method
        self.attribute1 = parameters
        self.attribute2 = "a"
    
    def intro(self):
        '''regular public method here self refer to objecte'''
        print("from tes2")
    
    # static method
    @staticmethod
    def hello():
        '''this is static method without parameter '''
        print("hello")
    
    @classmethod
    def class_method(cls, *args, **kwargs):
        '''this is class method which will change class attribute  directly here cls refer to class not a obj'''
        pass




# error handling
try:
    result = 20/ 5
except ZeroDivisionError as e:
    print(f"Error: {e}")
else:
    print(f"Result: {result}")  # Runs if no exception occurs
finally:
    print("Execution complete.")  # Always runs


"--------------"
def check_age(age):
    '''raising a value error'''
    if age < 0:
        raise ValueError("Age cannot be negative.")

try:
    check_age(-5)
except ValueError as e:
    print(f"An error occurred: {e}")


"----------------"
# coustom error

class Cust_Error(Exception):
    '''this is coustom error defined by itself'''
    pass

'''now we can raise error/ coustom error'''
try:
    raise Cust_Error("custom error.")
except Cust_Error as e:
    print(f"custom error: {e}")