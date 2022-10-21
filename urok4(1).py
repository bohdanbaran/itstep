class Human:
 height = 170
 satiety = 50
class Student(Human):
 satiety = 10
class Worker(Human):
 satiety = 100
nick = Student()
ann = Worker()
print(nick.height, nick.satiety)
print(ann.height, ann.satiety)