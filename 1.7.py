class Time:
    __hour : int
    __minute : int
    __second : int

    def __init__(self, hour : int, minute : int, second : int):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def getHour(self) -> str:
        if self.__hour < 10:
            return  "0" + str(self.__hour)
        else:
            return str(self.__hour)

    def getMinute(self) -> str:
        if self.__minute < 10:
            return  "0" + str(self.__minute)
        else:
            return str(self.__minute)

    def getSecond(self) -> str:
        if self.__second < 10:
            return  "0" + str(self.__second)
        else:
            return str(self.__second)

    def setHour(self, hour : int):
        self.__hour = hour

    def setMinute(self, minute : int):
        self.__minute = minute

    def setSecond(self, second : int):
        self.__second = second

    def setTime(self, hour : int, minute : int, second : int):
        super().__init__(hour, minute, second)

    def toString(self) -> str:
        return str(self.getHour()) + ":" + str(self.getMinute()) + ":" + str(self.getSecond())

    def nextSecond(self) -> int:
        self.__second += 1
        if self.__second > 59:
            self.__second -= 60
            self.__minute += 1
        if self.__minute > 59:
            self.__minute -= 60
            self.__hour += 1
        if self.__hour > 23:
            self.__hour -= 24
        return self.toString()

    def previousSecond(self) -> int:
        self.__second -= 1
        if self.__second <= 0:
            self.__second += 59
            self.__minute -= 1
        if self.__minute <= 0:
            self.__minute += 59
            self.__hour -= 1
        if self.__hour <= 0:
            self.__hour += 23
        return self.toString()

time1 = Time(1,1,0)
print(time1.previousSecond())






