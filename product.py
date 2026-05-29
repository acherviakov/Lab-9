from style import *
class Product:
    counter = 0
    def __init__(self, name, type, price, amount, provider):
        self.__price = price
        self.__name = name
        self.__type = type
        self.__amount = amount
        self.__provider = provider
        Product.counter += 1
        self.id = Product.counter
        print("Создание ID " + str(self.counter))

    def __copy__(self):
        return Product(self.price, self.name, self.type, self.amount, self.provider)

    def __lt__(self, other):
        return self.__price
    
    def __eq__(self, other):
        return self.name == other.name
    
    def __gt__(self, other):
        return self.name > other.name
    def __repr__(self):
        return f"{self.name};{self.type};{self.price};{self.amount};{self.provider}"
    
    def __str__(self):
        return f"{self.name}(type:{self.type}, price:{self.price}, amount:{self.amount}, provider:{self.provider})"
    @property
    def price(self):
        return self.__price
    @property
    def name(self):
        return self.__name
    @property
    def type(self):
        return self.__type
    @property
    def amount(self):
        return self.__amount
    @property
    def provider(self):
        return self.__provider
    
    @price.setter
    def price(self, price):
        if price > 0:
            self.__price = price
    
    @name.setter
    def name(self, name):
        if len(name) > 2:
            self.__name = name
    
    @type.setter
    def type(self, type):
        if len(type) > 2:
            self.__type = type

    @provider.setter
    def provider(self, provider):
        if len(provider) > 2:
            self.__provider = self.provider

    @amount.setter
    def amount(self, amount):
        if amount > 0:
            self.__amount = amount


    def run_changer(self, changer):
        changer_list = changer.split(":")
        if(len(changer_list) != 2):
            print_error("Неверный changer-блок (см. help changer)")
            return 1
        attribute = changer_list[0]
        value = changer_list[1]
        if(attribute == "name"):
            self.name = value
        elif(attribute == "type"):
            self.type = value
        elif(attribute == "price"):
            self.price = int(value)
        elif(attribute == "amount"):
            self.amount = int(value)
        elif(attribute == "provider"):
            self.type = value
        else:
            print_error(f"Нет аттрибута {attribute}")
            return 1
        return 0
    




    @staticmethod
    def from_string(cls, string):
        data = string.split(";")
        return cls(data[0], data[1], int(data[2]), int(data[3]), data[4])
    

    

    def value(self, attribute):
        if attribute == "name":
            return self.name
        elif attribute == "type":
            return self.type
        elif attribute == "price":
            return self.price
        elif attribute == "amount":
            return self.amount
        elif attribute == "provider":
            return self.provider
        else:
            return self.id