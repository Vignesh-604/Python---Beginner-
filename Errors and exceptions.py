"""Errors, Exceptions and Custom Exceptions."""
''' Types of errors '''
#print("Hello"))                                                    # SyntaxError

#print(5 + "5")                                                     # TypeError

#import somemodule                                                  # ModuleNotFoundError

#print(c)                                                           # NameError

#f = open("File")                                                   # FileNotFoundError

a = [1, 2, 3]
#a.remove(4)                                                        # ValueError

#a.pop(3)                                                           # IndexError

b = {"A": "Apple"}
#print(b["B"])                                                      # KeyError

#if a!=3:
#print(a)                                                           # IndentationError


''' Raising an Exception '''
x = 5

#if x != 3:
#    raise Exception("Variable does not equal to value.")           # Raises an Exception with a message if the condition is satisfied.

#assert(x!=5), "Assertion message."                                 # Raises an AssertionError with a message if the condition is not satisfied.

''' Custom Exception. '''

class HighValue (Exception):                                        # Creating a class exception with custom name.
    pass

class LowValue(Exception):                                          # Since it's a class, additional functions can be added to it.
    def __init__(self, message, number):
        self.mess = message
        self.val = number

def value(f):
    if f > 100:
        raise HighValue("Value is too high.")                      # The statement it'll print with the error.
    elif f < 100:
        raise LowValue("Value too low", f"Number input: {f}")      # Satisfying both parameters set in clsss which can be accessed individually.

try:
    value(50)

except HighValue as h:
    print(h, "Try lower.")

except LowValue as l:
    print(l.mess)













