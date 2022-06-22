

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old')


if __name__ == '__main__':
    person = Person('Juan', 21)

    print(f'Age: {person.age}')
    person.say_hello()