from planet import *
class Collect:
    def __init__(self, array):
        self.array = array
    def __str__(self):
        return str(self.array)
    def run_query(self, data):
        data = data.split()
        if(data[0] == "create"):
            planet = Planet(1,1,"Unnamed_"+str(Planet.counter),1,"Nonetype")
            wrong_generation = False
            for el in data[1:]:
                result = planet.run_changer(el)
                if result == 1:
                    wrong_generation = True
            if not wrong_generation:
                self.array.append(planet)
        if(data[0] == "change"):
            planet = Planet(1,1,"Unnamed_"+str(Planet.counter),1,"Nonetype")
            wrong_generation = False
            for el in data[1:]:
                result = planet.run_changer(el)
                if result == 1:
                    wrong_generation = True
            if not wrong_generation:
                self.array.append(planet)
                print(styled("Успешно!","green"))
        elif(data[0] == "delete"):
            planet_name = data[1]
            if planet_name.isdigit():
                found = False
                id = int(planet_name)
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
                name = planet_name
                for i in range(len(self.array)):
                    if self.array[i].name == name:
                        del self.array[i]
                        found = True
                if not found:
                    print_error("Данного имени не существует")
                else:
                    print(f"{name} успешно удалён")
                
            

                    
        elif(data[0] == "print"):
           for planet in self.array:
               print(planet)
        elif(data[0] == "save"):
           self.write_in_database()
        elif(data[0] == "read"):
           self.read_from_database()
        elif(data[0] == "help"):
            if len(data == 1):
                print("Достурные команды: create, change, help, delete, print, save, read. Подробнее: help <command>")
            else:
                Collect.help(data[1])
        else:
            print_error(f"Не существует команды {data[0]}")
    def write_in_database(self):
        with open("db.txt", "w") as database:
            for planet in self.array:
                print(repr(planet), file=database)
    def read_from_database(self):
        with open("db.txt", "r") as database:
            self.array = []
            for line in database:
                current_line = line.strip("\n")
                self.array.append(Planet.from_string(current_line))
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
                mass:<число><g - в граммах, kg - в килограммах, em - в массах Земли>
                distance:<число><m - в метрах, km - в километрах, au - в астономических единицах>
                radius:<число><m - в метрах, km - в километрах>
                Примеры: 
                name:Mars
                radius:18.5km
                '''
            )
        elif command == "create":
            print("create <changerblock-1> <changerblock-2> ... - создаёт планету с исходными параметрами")
        elif command == "change":
            print("change <ID/имя> <changerblock-1> <changerblock-2> ... - изменяет переметры планеты с заданным именем или ID")
        elif command == "delete":
            print("delete <ID/имя> ... - удаляет планету с заданным именем или ID")
        elif command == "read":
            print("read - считать данные из базы данных")
        elif command == "save":
            print("save - сохранить данные в БД")
        elif command == "print":
            print("выводит текущие данные")
        else:
            print_error("Неизвестная команда")