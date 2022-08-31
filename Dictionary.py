"""Dictionary :- Unordered, Mutable and Key-Value pairs."""
D1 = {"Animal": "Bear", "Bird": "Eagle", "Fish": "Salmon", "Worm": "Earthworm"}
D2 = dict(mammal= "Whale", pet= "Cat")
D3 = {"D-Animal": "Cow"}

# Accessing the dictionary
print(D1["Animal"], D2.get("pet"),
      D2.get("Fish", "Not in Dictionary."))          # [1]                # If the key word isn't in the dictionary, it'll prit the message. 

# Addining elements
D3["Insect"] = ["Beetle"]
print(D3)                                            # [2]
D3["Insect"] = ["Butterfly"]
print(D3)                                            # [3]

# Removing elements
del D1["Bird"]
print(D1)                                            # [4]
print(D1.pop("Animal"))                              # [5]                 # Prints the value of specified key and removes it from the dict.
D1.pop("Worm"), print(D1)                            # [6]                 # Will print the dict after removing the item mentioned.
D2.popitem(), print(D2)                              # [7]                 # Removes the last item.

# Checking for an item in a dict
if "D-Animal" in D3:
    print("It does.")
try:
    print(D3["W-animal"])
except:
    print("Doesn't have.")

# Keys and values in items
D4 = dict(A = "Apple", B = "Banana")
for k in D4.keys():
    print(k)                                         # [8, 2]
for v in D4.values():
    print(v)                                         # [9, 2]
for k, v in D4.items():
    print(k, v)                                      # [10, 2]
for i in D4.items():
    print(i)                                         # [11, 2]

# Copying a dictionary
D5 = {"Copy": "Copied"}
DC = D5                                                                    # Changes done to this dictionary will affect the original dictionary.
DC2 = D5.copy()
DC3 = dict(D5)
print(DC, DC2, DC3)                                  # [12]

# Updating a dictionary
D6 = dict(Cows= 22, Buffalo= 17, Goats= 10)
D7 = dict(Cows= 26, Buffalo= 20, Sheep= 14)
D6.update(D7)                                                              # Updates the vallues and adds new items. Doesn't remove old items.
print(D6)                                            # [13]

# Differnt data types in dictionary
D8 = {7: 49, "3": 64, 9: "String"}
print(D8[7])                                         # [14]                # Can't index a dictionary.

D8[(8, 1)] = [64]                                                          # The keys and values can be Str, Int or a Tuple.
tupy = (9, 9)

D9 = {tupy: "tuple"}
print(D8, D9)                                        # [15]
