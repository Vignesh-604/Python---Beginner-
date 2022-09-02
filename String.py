"""Strings :- Ordered, Immutable and Text representators."""
String = "Cool Up "

print(String.islower())                      # [1]                 # Checks if all the letters are in lowercase.
print(String.isupper())                      # [2]                 # Checks if all the letters are in uppercase.
print(String.istitle())                      # [3]                 # Checks if the first letter of each word is capital.

print(String.isalpha())                      # [4]                 # Checks if all the strings are alphabets. Spaces are also counted for.
print(String.isalnum())                      # [5]                 # Checks if the strings are a combinations of alphabets and numbers.
                                                                   # If there's a space, sign or symbol, the ouput will be False.
print(String.isspace())                      # [6]                 # Checks if there's only space/s for a string.

print(String.lower())                        # [7]                 # Converts the letters into lowercase.
print(String.upper())                        # [8]                 # Converts the letters into uppercase.

print(String.replace("Cool Up", "Cool Down"))          # [9]                 # Replacing the string value of the variable.

print(len(String))                           # [10]                # The lenght of the string.

print(String[2])                             # [11]                # Gives the string at the specified index.

print(String.index("o"))                     # [12]                # Gives the index of the specified index.

# 'sep=' seperates two strings.   'end=' Attaches a string at the end.
print(f"{String}is", "Chilling.", sep=" ", end=" Peace out.")      # [13]

