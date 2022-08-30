"""Lists :- Ordered, Mutable and allows duplicate elements"""
Frens = ["Bear", "Monkey", "Unicorn", "Penguin"]
Nums = [22, 28, 8, 18, 10, 17, 19]
Animals = Frens.copy()
print(Animals)                                 # [1]

# Adding items
Frens.extend(Nums)
print(Frens)                                   # [2]

Alpha = ["A", "B", "C"]
Alpha.append('D')
print(Alpha)                                   # [3]

Farm = ["Cow", "Buffalo", "Dog", "Sheep"]
Farm.insert(3, "Cat")
print(Farm)                                    # [4]

# Removing items
Fruits = ["Berry", "Pear", "Apple", "Orange", "Banana"]
Fruits.pop(3)
Fruits.remove("Banana")
print(Fruits)                                  # [5]


Veggies = ["Onion", "Potato", "Peas", "Garlic", "Peas"]

print(Veggies.count("Peas"))                   # [6]
print(Veggies.index("Potato"))                 # [7]

Veggies.reverse()
print(Veggies)                                 # [8]

Mum = [1, 2, 3, 6]
Mum.clear(), print(Mum)                        # [9]
