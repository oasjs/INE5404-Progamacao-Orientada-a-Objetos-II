class Student():
    def __init__(self, name:str, id_code:int, email:str, phone_number:str) -> None:
        
        self.name = name
        self.id = id_code
        self.email = email
        self.phone = phone_number
        self.frequency = 0
        self.iaa = 0

    def get_info(self):
        student_info = {
            "Name": self.name,
            "ID": self.id,
            "Email": self.email,
            "Phone Number": self.phone,
            "Frequency": self.frequency,
            "IAA": self.iaa,
        }
        for info in student_info:
            print(f'{info}: {student_info[info]}')
        print("")


class Professor():
    def __init__(self, name:str, id_code:int, email:str, phone_number:str) -> None:
        
        self.name = name
        self.id = id_code
        self.email = email
        self.phone = phone_number

    def get_info(self):
        professor_info = {
            "Name": self.name,
            "ID": self.id,
            "Email": self.email,
            "Phone Number": self.phone,
        }
        for info in professor_info:
            print(f'{info}: {professor_info[info]}')
        print("")


class Class():
    def __init__(self, id_code:str, students:list, professors:list) -> None:
        
        self.id = id_code
        self.students = students
        self.professors = professors
        self.student_list = []

        self.__list_students()

    # Both __feed_name and __list_studens work to generate a list of students containing tuples with the student's name and ID respectively.
    def __feed_name(self, pair):
        return pair[0]

    def __list_students(self):
        for student in self.students:
            id_pair = (student.name, student.id)
            self.student_list.append(id_pair)

        self.student_list.sort(key=self.__feed_name)


    def get_info(self):
        print("Professors:")
        for prof in self.professors:
            print(f'    {prof.name}')
        print("")
        print("Students:")
        for stud in self.students:
            print(f'    {stud.name}')
        print("")


class Course():
    def __init__(self, name:str, id_code:str, classes:list) -> None:
        
        self._name = name
        self._id_code = id_code
        self._classes = classes

    def get_classes(self):
        pass


st1 = Student("Jonas", 123, "jonas@mail", "9999-9999")
st2 = Student("Peter", 321, "peter@mail", "8999-9999")
st3 = Student("Lucas", 231, "lucas@mail", "7999-9999")
st4 = Student("Rodris", 132, "rodris@mail", "6999-9999")
pf1 = Professor("Linguiça", 333, "ling@mail", "5555-5555")
cl1 = Class("LING5666", [st1,st2,st3,st4], [pf1])

cs1 = Course("Iô-Iô", "IOIO1000", [cl1])

st1.get_info()

cl1.get_info()