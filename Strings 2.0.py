"""Strings :- Ordered, Immutable and Text representators."""
Spreadout = ('''Hello          everyone                 having
                 a                                              great
               day??                                       I              hope
                                      you
                                                    do!!            
                                                                  haha ''')      # Prints in the exact way it's written.
print(Spreadout)                                 # [1, 6]
print('''Green \
apple''')                                     # [2]

strng = "                    buzzy bee                 "     # Removes the extra unused space.
print(strng.strip())                          # [3]

# Indexing/ Slicing
String = "Ting Ting"
print(String[0], String[2:7], String[6::-1])  # [4]          # [6::-1] will take in account the first 6 inputs then reverse it.

Cb = "Cowboy rides a horse."
print(Cb[0::10].upper(), Cb[4:17].lower())    # [5]
print(Cb.startswith("Cow"))                   # [6]
print(Cb.endswith("chh"))                     # [7]
print(Cb.index(" "), Cb.find("a"),
      Cb.count("b"))                          # [8]          # Find and index does the same operation.

# String to list conversion
Cb2 = "Yes! you can talk to anyone."
Cb3 = "No!xTalkingxisxfree"

Cb_list = Cb2.split(" ")                                     # The object inside the brackets are the dividers.
Cb_list2 = Cb3.split("x")
print(Cb_list, Cb_list2)                      # [9]

# List to sting conversion
Cb_sting = ["Party", "we", "do", str(24), "*", str(7)]
Cb4 = " ".join(Cb_sting)                                     # The object inside the quotes are the joiners.
print(Cb4)                                    # [10]

# Formatting a string
str = "Max"
dec = 10
flt = 85.333333

sent = "I am %s." %str                                       # %s : string , %d : decimal , %f : float
sent2 = "I got %d apples." %dec
sent3 = "I got %.2f in 10th." %flt                           # %.nf : where n is the number of decimal numbers you want to have.
print(sent, sent2, sent3)                    # [11]

sent4 = "My name is {} and I got {:.2f} in {}th.".format(str, flt, dec)      # :.nf :- where n is the number of decimal numbers you want to have.
print(sent4)                                 # [12]

sent5 = f"{str} got {flt} in {dec}th but less in {dec + 2}th."
print(sent5)                                 # [13]
