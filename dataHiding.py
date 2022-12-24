class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age


person1=Person("Messi",35)
print(person1._Person__name)
print(person1._Person__age)