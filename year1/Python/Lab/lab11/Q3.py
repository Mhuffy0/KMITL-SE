class Name:
    def __init__(self, title, first_name, last_name):
        self.t = title
        self.f = first_name
        self.l = last_name
        
    def setName(self, t, f , l):
        self.t = t
        self.f = f
        self.l = l
        
    def getFullName(self):
        name = self.t + ". " + self.f + " " + self.l
        return name
        
class Date:
    def __init__(self, day=1, month=1, year=2010):
        try:
            if 0 < day < 32 and 0 < month < 13: 
                self.day = day
                self.month = month
                self.year = year
            else:
                print("Day 1-31, Month 1 - 12")
        except ValueError:
            print("Err")
        
    def setDate(self, d, m, y):
        try:
            if 0 < d < 32 and 0 < m < 13: 
                self.day = d
                self.month = m
                self.year = y
            else:
                print("Day 1-31, Month 1 - 12")
        except ValueError:
            print("Err")
            
    def getDate(self):
        self.date = str(self.day) + "/" + str(self.month) + "/" + str(self.year)
        return self.date
        
    def getDateBC(self):
        self.year = self.year + 543
        self.date = str(self.day) + "/" + str(self.month) + "/" + str(self.year)
        return self.date
    
class Address:
    def __init__(self, houseNo, street, district, city, country, postcode):
        self.hno = houseNo
        self.street = street
        self.dis = district
        self.city = city
        self.country = country
        self.pcode = postcode
        
    def setAdd(self, houseNo, street, district, city, country, postcode):
        self.hno = houseNo
        self.street = street
        self.dis = district
        self.city = city
        self.country = country
        self.pcode = postcode
        
    def getAdd(self):
        self.adds = f"House: {self.hno}, Street: {self.street}, District: {self.dis}, City: {self.city}, Country: {self.country}, PostCode: {self.pcode}"
        return self.adds
    
class Person:
    def __init__(self, name, bd, adds):
        self.name = name  # This is an instance of the Name class
        self.bd = bd
        self.adds = adds
        
    def printInfo(self):
        print(f"Name: {self.name.getFullName()}\nBD: {self.bd.getDate()}\nAddress: {self.adds.getAdd()}")
        
class Employee(Person):
    def __init__(self, name, bd, adds, startD, department):
        super().__init__(name, bd, adds)
        self.startd = startD
        self.dpm = department
        
class TempEmp(Employee):
    def __init__(self, name, bd, adds, startD, department, wage):
        super().__init__(name, bd, adds, startD, department)
        self.wage = wage
        
    def printInfo(self):
        print(f"Name: {self.name.getFullName()}\nBD: {self.bd.getDate()}\nAddress: {self.adds.getAdd()} \nStart Date: {self.startd.getDate()} \nDepartment: {self.dpm} \nWage: {self.wage}")
        
class PermEmp(Employee):
    def __init__(self, name, bd, adds, startD, department, salary):
        super().__init__(name, bd, adds, startD, department)
        self.salary = salary
        
    def printInfo(self):
        print(f"Name: {self.name.getFullName()}\nBD: {self.bd.getDate()}\nAddress: {self.adds.getAdd()} \nStart Date: {self.startd.getDate()} \nDepartment: {self.dpm} \nSalary: {self.salary}")
        
class Department():
    def __init__(self, des, manager, list_of_emps=None):
        self.des = des
        self.mng = manager
        self.list = list_of_emps if list_of_emps is not None else []
        
    def addEmp(self, e):
        self.list.append(e)
        e.Department = self
        
    def removeEmp(self, e):
        self.list.remove(e)
        e.Department = None
        
    def setMng(self, e):
        if isinstance(e, PermEmp) and e in self.list:
            self.mng = e
            
    def printInfo(self):
        print(f"Desc: {self.des}")
        print(f"Manager: {self.mng.getFullName() if self.mng else None}")
        print(f"Employees: {[emp.name.getFullName() for emp in self.list]}")

        

# Test
obj = Name("Mr", "John", "Doe")
obj2 = Name("Mr", "Jackky", "Doe")
obj3 = Name("Mr", "Sun", "Doe")
print(obj.getFullName())

date = Date(12, 12, 2024)
print(date.getDateBC())

adds = Address(20, "Main Street", "District", "City", "Country", 20202020)
print(adds.getAdd())

person = Person(obj, date, adds)
person.printInfo()

depart = Department("How to Breathe", obj)
depart.addEmp(person)
depart.printInfo()
