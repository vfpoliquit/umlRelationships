class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.__age = age
        self.height = height

    def get_age(self):
        return self.__age

    def study(self):
        print(f"{self.name} is studying")


teacher = Person("JUAN JUBAHIB MOCOY", 45, 160)
student = Person("MARS PAROHINOG", 45, 160)

print(
    f"Name: {teacher.name}\n"
    f"Age: {teacher.get_age()}\n"
    f"Height: {teacher.height} cm"
)
student.study()