"""Slicing or Indexing is the method to obtain a sub-iterable from an iterable."""

# Elements of an iterable are counted in whole numbers i.e. from 0.
# The numbers are called Indexes and the dots [:] are called slicing operators.
# Indexing is done by printing the list with the start and stop index of the iterable: list_name[start_index : stop_index]
# It'll print from the element at the start index to the element represented by the index before the given stop index.

a = ["A", "B", "C", "D", "E", "F", "G"]

print(a[5])                    # [1]               # Accessing a single element from the list.
print(a[0:5])                  # [2]               # Starts from element at index 0 to element before stop index 5.
print(a[2:])                   # [3]               # All the elements after the start index along with the element represented by the start index.
print(a[:4])                   # [4]               # All elements before the end index but not the element represented by end index.

# Negative numbers are counted from the right side of the iterable.
# For ex. For list 'a', the last element 'G' has both index 6 and -1.

print(a[-3])                   # [5]               # The third element from the right.
print(a[-4:])                  # [6]               # From element at index -4 and the elements it follows.
print(a[:-4])                  # [7]               # All elements before index -4 except the one at -4.
print(a[-5:-2])                # [8]
print(a[-6:6])                 # [9]

# [::] is the slice step operator. Suppose list[::n], then it'll print every n'th element.

print(a[::3])                  # [10]              # Here, every third element is printed skipping the ones in-between.
print(a[2::2])                 # [11]              # list[start :: step]. It'll take into accord the elements after the start index.

# If step index is negative, the list is reversed. Since the list is reversed, the start index counts back i.e. takes the elements before the start index.
# For ex. [5::-1] The list is reversed and is counted backwards from index 5.

print(a[::-1])                 # [12]              # Reverses a list.
print(a[::-2])                 # [13]              # The list is reversed and every 2nd element is printed.
print(a[2::-2])                # [14]              # Elements before the start index are taken into accord.

# list[start:end:step]. This slice operator will have a start, stop and step indexes.
# For ex. [0:5:2] The elemnets between 0 and 5 are taken into accord with step index 2, so it'll print every second element.

print(a[1:7:2])                # [15]
print(a[:2:3])                 # [16]              # Only prints the first element.
print(a[6:1:-2])               # [17]              # The elements before the start index are taken into accord since the list is in reverse order.
