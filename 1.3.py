class Employee:
    __id : int
    __firstName : str
    __lastName : str
    __salary : int


    def __init__(self, id : int, firstName : str, lastName : str, salary : int):
        self.__id = id
        self.__firstName = firstName
        self.__lastName = lastName
        self.__salary = salary


    def getID(self) -> int:
        return self.__id

    def getFirstName(self) -> str:
        return self.__firstName.title()

    def getLastName(self) -> str:
        return self.__lastName.title()

    def getName(self) -> str:
        return self.getFirstName() + " " + self.getLastName()

    def getSalary(self) -> int:
        return self.__salary

    def setSalary(self, salary : int):
        self.__salary = salary

    def getAnnualSalary(self) -> int:
        return self.getSalary() * 12

    def raiseSalary(self, percent : int) -> float:
        return (self.getSalary() * percent)/100 + self.getSalary()

    def toString(self) -> str:
        return "Employee [ id = " + str(self.getID()) + ", name = " + str(self.getName()) + ", salary = " + str(self.raiseSalary(20)) + " ]"



Employee1 = Employee(23, "rainamira", "azzahra", 12000000)
print(Employee1.getAnnualSalary())
print(Employee1.toString())
