''' Try, Except and Finally'''
try:                                                                # Performs certain set of codes if there are no errors.
    p = 5/1
    q = 5 + "5"

except TypeError:                                                   # If the specified error is raised, it'll perform the given code.
    print("Cannot perform operation.")            # [1]

except ZeroDivisionError as z:                                      # Specifies the error as a variable.
    print(f"Tried to do {z}.")                    # [1]

except Exception as e:                                              # Can use Exception to catch any error that was raised and can be specified.
    print(e)                                      # [1]

except:                                                             # Will catch any exception that was raised.
    print("Exception too broad.")                 # [1]
else:                                                               # Excecutes certain codes if no errors were raised.
    print(p + q)                                  # [1]

finally:                                                            # Prints the given code regardless of previous codes or wrrors.
    print("Code works!")                          # [2]
