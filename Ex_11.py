print(' --- Copy a list to another list')
list_1 = ["A", "B", "C"]
list_2 = list_1 [:]     # ca list_2 sa-si pastreze continutul de sine statator chiar daca list_1 se modifica
list_3 = list_2

print(list_2)
del list_1[0]
print(list_3)

print('\n --- Classes - Employee')
class Employee:
    def __init__(self, name , age, section, an):
        self.name = name
        self.age = age
        self.section = section
        self.an = an

    def isSuperAngajat(self):
        if 2022 - self.an > 10:
            print(f'{self.name} is super employee')
        else:
            print(f'{self.name} not proposed for bonus')

angajat1 = Employee("Vasile", 34, "marketing", 2023)
angajat2 = Employee("Ion", 60, "IT", 2010)
print("Employee 1: ", angajat1.name, ",", angajat1.age, ",", angajat1.section, ",", angajat1.an)
print("Employee 2: ", angajat2.name, ",", angajat2.age, ",", angajat2.section, ",", angajat2.an)

if angajat1.age > angajat2.age:
    print(f'Employee1 {angajat1.name} has {angajat1.age} and is the oldest')
else:
    print(f'\nEmployee2 {angajat2.name} has {angajat2.age} and is the oldest\n')

angajat1.isSuperAngajat()
angajat2.isSuperAngajat()

print("\n", Employee("Vasile", 34, "marketing", 2023))
print(Employee("Ion", 60, "IT", 2010))
print("\n", angajat1)
print(angajat2)

print('\n --- Classes - Baker')
class Baker:
    def __init__(self, name, age, type):
        self.name = name
        self.age = age
        self.type = type

    def whatCooks(self, speciality):
        print(f'{self.name} knows how to make {speciality}')

    def hasPerformances(self, hasMichelin):
        if hasMichelin == True:
            print(f'{self.name} has Michelin stars')
        else:
            print(f'{self.name} is a regular baker')

baker1 = Baker("Petru", 54, "pastry")
baker2 = Baker("Mihai", 38, "confectionery ")
baker3 = Baker("Luigi", 40, "bakery")

baker1.whatCooks("croissants")
baker2.whatCooks("cookies")
baker3.whatCooks("bread and pizza")
print()
baker1.hasPerformances(True)
baker2.hasPerformances(True)
baker3.hasPerformances(False)
