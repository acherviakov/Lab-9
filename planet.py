from style import *
class Planet:
    counter = 0
    def __init__(self, radius, mass, name, distance_from_sun, type):
        self.__radius_in_km = radius
        self.__mass_in_kg = mass
        self.__name = name
        self.__distance_from_sun_in_million_km = distance_from_sun
        self.__type = type
        Planet.counter += 1
        self.id = Planet.counter
        print("Создание ID " + str(self.counter))

    def __copy__(self):
        return Planet(self.raduis_in_km, self.mass_in_kg, self.name, self.distance_from_sun_in_million_kg, self.type)

    def __lt__(self, other):
        return self.distance_from_sun_in_million_km < other.distance_from_sun_in_million_km
    
    def __eq__(self, other):
        return self.name == other.name
    
    def __gt__(self, other):
        return self.name > other.name
    def __repr__(self):
        return f"{self.radius_in_km};{self.mass_in_kg};{self.name};{self.distance_from_sun_in_million_km};{self.type}"
    
    def __str__(self):
        return f"{self.name}(radius:{self.radius_in_km}km, mass:{self.mass_in_kg}kg, distance:{self.distance_from_sun_in_million_km/1000000}km; type:{self.type})"
    @property
    def radius_in_km(self):
        return self.__radius_in_km
    @property
    def mass_in_kg(self):
        return self.__mass_in_kg
    @property
    def name(self):
        return self.__name
    @property
    def distance_from_sun_in_million_km(self):
        return self.__distance_from_sun_in_million_km
    @property
    def type(self):
        return self.__type
    
    @radius_in_km.setter
    def radius_in_km(self, radius_in_km):
        if radius_in_km > 0:
            self.__radius_in_km = radius_in_km
    
    @mass_in_kg.setter
    def mass_in_kg(self, mass_in_kg):
        if mass_in_kg > 0:
            self.__mass_in_kg = mass_in_kg
    @distance_from_sun_in_million_km.setter
    def distance_from_sun_in_million_km(self, distance_from_sun_in_million_km):
        if distance_from_sun_in_million_km > 0:
            self.__distance_from_sun_in_million_km = distance_from_sun_in_million_km
    @type.setter
    def type(self, type):
        self.__type = type

    @name.setter
    def name(self, name):
        self.__name = name


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
        else:
            seperated_parts = Planet.seperate_units(value)
            value = seperated_parts[0]
            unit = seperated_parts[1]
            if unit == "":
                print_error(f"Нет единицы измерения")
                return 1
            if(attribute == "distance"):
                if unit == "m":
                    self.distance_from_sun_in_million_km = float(value)/1000000000
                elif unit == "km":
                    self.distance_from_sun_in_million_km = float(value)/1000000
                elif unit == "au":
                    self.distance_from_sun_in_million_km = float(value)*149.6
                else:
                    print_error(f"Единица измерения {unit} недоступна для расстояния до солнца")
                    return 1
            elif(attribute == "mass"):
                if unit == "g":
                    self.mass_in_kg = float(value)/1000
                elif unit == "kg":
                    self.mass_in_kg = 1000000
                elif unit == "em":
                    self.mass_in_kg = float(value)*6*(10**24)
                else:
                    print_error(f"Единица измерения {unit} недоступна для массы планеты")
                    return 1
            elif(attribute == "radius"):
                if unit == "m":
                    self.distance_from_sun_in_million_km = float(value)/1000
                elif unit == "km":
                    self.distance_from_sun_in_million_km = float(value)
                else:
                    print_error(f"Единица измерения {unit} недоступна для радиуса планеты")
                    return 1
            else:
                print_error(f"Неизвестный аттрибут {attribute} (см. help changer)")
                return 1
        return 0




    @staticmethod
    def from_string(cls, string):
        data = string.split(";")
        return cls(float(data[0]), float(data[1]), data[2], float(data[3]), data[4])
    
    @staticmethod
    def seperate_units(string):
        value = ""
        unit = ""
        is_value = True
        for symbol in string:
            if is_value:
                if symbol in "1234567890":
                    value += symbol
                else:
                    unit += symbol
                    is_value = False
            else:
                unit += symbol
        return (value, unit)
    

    def value(self, attribute):
        if attribute == "radius":
            return self.radius_in_km
        elif attribute == "mass":
            return self.mass_in_kg
        elif attribute == "distance":
            return self.distance_from_sun_in_million_km
        elif attribute == "type":
            return self.type
        elif attribute == "name":
            return self.name
        else:
            return self.id


    


    