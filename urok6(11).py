def checker(var_1):
    if type(var_1)!= str:
        raise TypeError(f"Sorry, we can’t work with {type(var_1)}," f" "f"we need class str")
    else:
        return var_1
# first_var = 10
first_var = "Hello"
checker(first_var)