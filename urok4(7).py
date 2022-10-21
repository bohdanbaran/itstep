class Grandparent:
    def about(self):
        print("I am GrandParent")

    def about_myself(self):
        print("I am Grandparent")

class Parent(Grandparent):
    def about_myself(self):
        print("I am Parent")
class Child(Parent):
    def __init__(self):
        super().about()
        super().about_myself()

nick = Child()