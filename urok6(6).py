try:
    print("start code")
    print(10/0)
    print("No errors")
except (NameError, ZeroDivisionError):
    print("We have an NameError")

print("code after capsule")