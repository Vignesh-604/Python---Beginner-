"""Sets :- Unordered, Mutable and doesn't allow duplication of elements."""
set1 = {"dello", "bello", "fello", "dello", "mello", "fello"}
set2 = set("google")
print(set2, set1)                        # [1]
print(type(set1))                        # [2]

# Adding and removing elements
set3 = set()                                               # You can't make a regular set with numbers. For ex: set = set(1, 2, 3)
set3.add(1)                                                # But we can do that by {}. For ex: setn = {2, 65, 8}
set3.add(2)
set3.add(3), set3.add(4)
set3.add(5),   print(set3)               # [3]
set3.discard(3)                                            # If the given object isn't in the set, it'll print the set as it is.
set3.remove(2)                                             # If the given object isn't in the set, it'll throw up an error.
set3.pop(),    print(set3)               # [4]             # Deletes the first object in a set.

# Checking for elements
if "bello" in set1:
    for thing in set1:
        print(thing)                     # [5, 4]

# Set fuctions
SetA = {"cat", "dog", "cow", 'bear', "monke"}
SetB = {"monke", "tiger", 'sloth', "bear", "deer"}
Isec = {"bear", "monke"}
LeftOuts = {"frog", "hen", "rat"}
print(SetB.union(SetA))                   # [6]               # Combining both elements of the set without repetition.
print(SetB.intersection(SetA))            # [7]               # Only those elements which are in both sets.
print(SetB.difference(SetA))              # [8]               # SetB elements exclding SetA elements.
print(SetB.symmetric_difference(SetA))    # [9]               # Both SetA & SetB elements excluding the ones in both sets.

#SetB.update(SetA), print(SetB)                               # The update functions updates the set overall.
#SetB.intersection_update(SetA), print(SetB)
#SetB.difference_update(SetA), print(SetB)
#SetB.symmetric_difference_update(SetA), print(SetB)

print(SetA.issubset(Isec))               # [10]
print(SetA.issuperset(Isec))             # [11]              # Superset is subset with places of Seta and SetB interchanged.
print(SetA.isdisjoint(LeftOuts))         # [12]              # Disjoint means elements not in set.

# Copying sets
Copy_Sets = {"Copy"}
Animals = set(Copy_Sets)
Domestic = Copy_Sets.copy()
print(Animals, Domestic)                # [13]

# FrozenSet
FSet = frozenset[("Bol", "Dol", "Gol")]                    # Frozensets cannot be modified i.e. add elements, remove elements or updated.
print(FSet)                             # [14]             # Other functions like union, intersection won't work either
