"""Lists :- Ordered, Mutable and allows duplicate elements"""
lst = ["Apple", "Banana", "Cherry", "Dragonfruit"]
print(len(lst))                           # [1]

# Sorting a list
lst2 = [1, 5, 9, 3, 7]
lst3 = ["Blueberry", "Peach", "Grapes", "Coconut"]

lst2.sort()                                                                 # Sorts a list in ascending/ alphbetical order.
lst4 = sorted(lst3)                                                         # This will not sort original list.
print(lst2, lst4)                         # [2]

# Same elements, multiple times
lst5 = [1, 0]*5                                                             # This will print the contents of the list n times.
print(lst5)                               # [3]

# Adding two lists
lst6, lst7 = [1, "Two", False], [(2, 3), 5.6]
lst8 = lst7 + lst6                                                         # It'll print in the order it is added.
print(lst8)                               # [4]

# Slicing (Indexing)
lst9 = ["Green", "Pink", "Blue", "Red", "Yellow", "Purple"]
slce = lst9[4:], lst9[:3], lst9[::2], lst9[::-2]
print(slce)                               # [5]

# Copying a list
lst10 = ["Copy"]
lst_c = lst10                                                              # Modifications made to this list will affect the orignal list aswell.
lst_c2 = lst10.copy()                                                      # Won't affect the origanl list.
lst_c3 = lst10[:]                                                          # Could use [::] aswell.
print(lst_c, lst_c2, lst_c3)             # [6]

# List comprehension
lst12 = [1, 2, 3, 4, 5]
a = [i*5 for i in lst12]                                                   # Performs a certain operation for all the contents of the list.
b = [e+5 for e in lst12]
c = [o+o for o in lst12]
d = [s for s in lst12 if s % 2 == 0]                                       # Conditional comprehension.
print(a, b, c, d)                           # [7]
