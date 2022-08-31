"""Tuples :- Ordered, Immutable and allows duplicate elements"""
tuppy = "Tim", "Pim", "Jim", "Kim", "Dim"                            # A tuple can be made without brackets.
print(type(tuppy))                                   # [1]
tuppy2 = tuppy[:3]
print(tuppy2)                                        # [2]

if "Kim" in tuppy:                                   # [3]
    print("Yes")
else:
    print("Nope")

# Indexing
print(tuppy[2], tuppy[-1])                           # [4]
for t in tuppy2:                                                     # t specifies each content [:] is the index of that specified content
    print(t[0:1])                                    # [5]

print(len(tuppy))                                    # [6]
print(tuppy.index("Tim"))                            # [7]
print(tuppy.count("Tim"))                            # [8]

# Conversion
listy = (list(tuppy))
print(listy)                                         # [9]
tuppy3 = tuple(listy)
print(tuppy3)                                        # [10]

# Specifying contents of tuple with variables
tuppy4 = "Slim", "Brim", "Flim"
a, b, c = tuppy4
print(b, c, a)                                       # [11]

tuppy5 = 1, 2, 3, 4, 5, 6, 7                                  # Elements not specified by a variable will be included in the variable with * in its begining.
ab, mn, *op, uv, xy = tuppy5                                  # Those remaining element will be placed inside a list.
print(ab, xy, mn, op, uv)                            # [12]   # Variables after the * variable, specifies the element at the end of the tupple.

# Size and time
import sys
list = [1, 2, 3, "pac", True]
tuple = 1, 2, 3, "pac", True
print(sys.getsizeof(list))                           # [13]         # Size will be in bytes.
print(sys.getsizeof(tuple))                          # [14]

import timeit                                                       # Tuple is takes up less time and space than a list.
print(timeit.timeit(stmt="list", number=10000))      # [15]
print(timeit.timeit(stmt="tuple",  number=10000))    # [16]
