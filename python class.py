class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduction(self):
        print(f"Hello, my name is {self.name}, a {self.age} year old {self.gender} undertaking the PLP course.")


person = Person("Mark", 30, "male")


person.introduction()

