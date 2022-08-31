# Basic math operators
print(4 + 6 / (2 - 5) * 3)          # [1]                 # + Add, - Sub, * Multiplication, / Divison

print(15 % 5)                       # [2]                 # Prints out the remainder.

print(4 ** 3)                       # [3]                 # Raises the base number to it's power: (base_no. , power_no.)

print(9//5)                         # [4]                 # // gives out the whole number without the numbers after the decimal of the result (Floored Division).

print(pow(7, 2))                    # [5]                 # Raises the base number to it's power: pow(base_no. , power_no.).

print(round(30.53))                 # [6]                 # Rounds up the number the nearest whole number.

print(abs(-70))                     # [7]                 # The positive value of that number (regardless of it's sign).

a,b,c = 2.7, 5.1, 4.7

print(max(a, b, c))                 # [8]                 # Gives out the biggest number from the given numbers.

print(min(a, b, c))                 # [9]                 # Gives out the smallest number from the given numbers.

# Some more operators from the math module.
from math import*
#import math                                        # If imported like this, 'math' should be typed before every function. Fpr ex. math.floor()

print(floor(3.71))                  # [10]                # 'floor' will round the number down to the nearest whole number i.e. he number before the decimal.
print(floor(-3.8))                  # [11]

print(ceil(3.001))                  # [12]                # 'ciel' will round the number up to the next whole number if there are any numbers after the decimal.
print(ceil(-4.41))

print(sqrt(64))                     # [13]                # Finds the square root of the number.

print(fmod(13, 5))                  # [12]                # Prints out the remainder in float.

print(fsum((2, 3, 4, 5, 1)))        # [13]                # Will add all the numbers in the iterable/ sequence. like tuple, list, set.

print(fabs(-4))                     # [14]                # The positive value of that number in float.

print(factorial(6))                 # [15]                # Prints the factorial of the number. For ex. 5! = 5*4*3*2*1
