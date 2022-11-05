class First_class:
    pass

class Second_class(First_class):
    pass


obj_from_class_2 = Second_class()

print(isinstance(obj_from_class_2, First_class))
print(isinstance(obj_from_class_2, Second_class))