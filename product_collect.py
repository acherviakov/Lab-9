from product import *
class Shop:
    def __init__(self, array):
        self.array = array
    def __str__(self):
        return str(self.array)
    def run_query(self, data):
        data = data.split()
        if(data[0] == "create"):
            product = Product("xxx", "xxx", 1, 1, "xxx")
            wrong_generation = False
            for el in data[1:]:
                result = product.run_changer(el)
                if result == 1:
                    wrong_generation = True
            if not wrong_generation:
                self.array.append(product)
        elif(data[0] == "change"):
            product =  Product("xxx", "xxx", 1, 1, "xxx")
            wrong_generation = False
            for el in data[1:]:
                result = product.run_changer(el)
                if result == 1:
                    wrong_generation = True
            if not wrong_generation:
                self.array.append(product)
                print(styled("Успешно!","green"))
        elif(data[0] == "delete"):
            product_name = data[1]
            if product_name.isdigit():
                found = False
                id = int(product_name)
                for i in range(len(self.array)):
                    if self.array[i].id == id:
                        del self.array[i]
                        found = True
                if not found:
                    print_error("Данного ID не существует")
                else:
                    print(f"ID {id} успешно удалён")
            else:
                found = False
                name = product_name
                for i in range(len(self.array)):
                    if self.array[i].name == name:
                        del self.array[i]
                        found = True
                if not found:
                    print_error("Данного имени не существует")
                else:
                    print(f"{name} успешно удалён")
        elif(data[0] == "print"):
           for product in self.array:
               print(product)
        elif(data[0] == "save"):
           self.write_in_database()
        elif(data[0] == "read"):
           self.read_from_database()
        elif(data[0] == "help"):
            if len(data) == 1:
                print("Доступные команды: create, change, help, delete, print, save, sort, read. Подробнее: help <command>")
            else:
                Shop.help(data[1])
        elif(data[0] == "sort"):
            self.array = self.bubble_sort(self.array, data[1])
        else:
            print_error(f"Не существует команды {data[0]}")
    def write_in_database(self):
        with open("db2.txt", "w") as database:
            for product in self.array:
                print(repr(product), file=database)
    def read_from_database(self):
        with open("db2.txt", "r") as database:
            self.array = []
            max_id = 0
            for line in database:
                current_line = line.strip("\n")
                self.array.append(Product.from_string(current_line))
                max_id = max(self.array[-1].id, max_id)
            Product.counter = max_id
    def help(command):
        if command == "help":
            print("help <command> - Подсказывает пользователю, как работает команда <command>")
        elif command == "changer":
            print(
                '''
                changer-блок - конструкция, которая показывает, какому аттрибуту какое значение присвоить
                Синтаксис changer-блока: <аттрибут>:<значение>
                Аттрибуты:
                name:<строка> 
                type:<cтрока>
                price:<число>
  
                Примеры: 
                name:Mars
                price:1389
                '''
            )
        elif command == "create":
            print("create <changerblock-1> <changerblock-2> ... - создаёт товар с исходными параметрами")
        elif command == "change":
            print("change <ID/имя> <changerblock-1> <changerblock-2> ... - изменяет переметры товара с заданным именем или ID")
        elif command == "delete":
            print("delete <ID/имя> ... - удаляет товар с заданным именем или ID")
        elif command == "read":
            print("read - считать данные из базы данных")
        elif command == "save":
            print("save - сохранить данные в БД")
        elif command == "print":
            print("выводит текущие данные")
        elif command == "sort":
            print("сортирует планеты по заданногму атрибуту")
        else:
            print_error("Неизвестная команда")


    def bubble_sort(array, parameter):
        no_swaps = False
        times_repeated = False
        in_array_same_found = False
        while( not no_swaps and times_repeated < len(array) - 1):
            no_swaps = True
            array, same_found, no_swaps = one_cycle_of_bubble_sort(array)
            if(not in_array_same_found):
                in_array_same_found = same_found
            times_repeated += 1
        return array
    

def one_cycle_of_bubble_sort(array, parameter):
    same_found = False
    no_swaps = True
    for i in range(1, len(array)):
        if array[i-1].value(parameter) > array[i].value(parameter):
            array[i-1], array[i] = array[i], array[i-1]
            no_swaps = False
        if array[i-1] == array[i]:
            same_found = True
    return (array, same_found, no_swaps)



        