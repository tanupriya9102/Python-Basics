def print_name(obj):
    print(obj.func())

class Person:
    name1 = "Person"

    def func(self):
        return self.name1

class Student(Person):
    a = 2
    b = 4
    def func(self):
        return self.a + self.b

def main():
    person = Person()
    student = Student()

    print_name(person)  # Prints "Person"
    print_name(student)  # Prints "6"

if __name__ == "__main__":
    main()
