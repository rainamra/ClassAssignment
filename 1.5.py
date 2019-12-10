class Account():
    __id: str
    __name: str
    __balance : int

    def __init__(self, id :str, name : str, balance : int = 0):
        self.__id = id
        self.__name = name
        self.__balance = balance

    def getId(self) -> str:
        return self.__id

    def getName(self) -> str:
        return self.__name

    def getBalance(self) -> int:
        return self.__balance

    def credit(self, amount : int):
        return self.__balance + amount

    def debit(self, amount : int):
        if amount <= self.getBalance():
            return self.__balance + amount
        else:
            print("Amount exceeded balance")
        return self.getBalance()

    def transferTo(self, another , amount : int) -> int:
        if amount <= self.__balance:
           self.__balance -= amount
           another.credit(amount)
        else:
            print("Amount exceeded balance")
        return self.__balance

    def toString(self) -> str:
        return "Account [ id = " + self.getId() + ", name = " + self.getName() + ", balance = " + str(self.__balance)

Account1 = Account("27", "raina", 700)
Account2 = Account("29", "azel", 300)
print(Account1.transferTo(Account2, 200))
print(Account2.getBalance())











