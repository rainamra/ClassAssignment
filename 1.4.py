class InvoiceItem:
    __id : str
    __desc : str
    __qty : int
    __unitPrice : float

    def __init__(self, id : str, desc : str, qty : int, unitPrice : float):
        self.__id = id
        self.__desc = desc
        self.__qty = qty
        self.__unitPrice = unitPrice

    def getId(self) -> str:
        return self.__id

    def getDesc(self) -> str:
        return self.__desc

    def getQty(self) -> int:
        return  self.__qty

    def setQty(self, qty : int):
        self.__qty = qty

    def getUnitPrice(self) -> float:
        return self.__unitPrice

    def setUnitPrice(self, unitPrice : float):
        self.__unitPrice = unitPrice

    def getTotal(self) -> float:
        return self.__unitPrice * self.__qty

    def toString(self):
        return "InvoiceItem [ id = " + self.getId() + ", desc = " + self.getDesc() + ", qty = " + str(self.getQty()) + ", unitPrice = " + str(self.getUnitPrice()) + "]"

item1 = InvoiceItem ("23", "book", 4, 300)
print(item1.toString())
