class Date:
    __day : int
    __month : int
    __year : int

    def __init__(self, day : int, month : int, year : int):
        self.__day = day
        self.__month = month
        self.__year = year

    def getDay(self) -> str:
        if self.__day < 10:
            return  "0" + str(self.__day)
        else:
            return str(self.__day)

    def getMonth(self)  -> str:
        if self.__month < 10:
            return  "0" + str(self.__month)
        else:
            return str(self.__month)

    def getYear(self) -> int:
        return self.__year

    def setDay(self, day : int):
        self.__day = day

    def setMonth(self, month : int):
        self.__month = month

    def setYear(self, year : int):
        self.__year = year

    def setDate(self, day : int, month : int, year : int):
        super().__init__(day, month, year)

    def toString(self) -> str:
        return str(self.getDay()) + "/" + str(self.getMonth()) + "/" + str(self.getYear())

Date1 = Date(10, 11, 2019)
print(Date1.toString())
