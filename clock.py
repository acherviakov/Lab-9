# Алгоритм 
# 1. Проверить данные на корректность:
#     1.1. проверить, что введён только один пробел
#     1.2. проверить, что до и после пробела стоят целые числа, а не случайный набор символов
#     1.3. проверить, что эти числа обозначают возможное количество минут и часов.
# 2. Если данные некорректны вывести ошибку, иначе
#    2.1. Проверить введено ли 0 00, тогда вывести полдень
#    2.2. Проверить введено ли 12 00, тогда вывести полдень
#    2.3. Проверить является ли количество минут нулём, тогда вывести x час/часа/часов [часть суток] ровно
#    2.4. Иначе вывести x час/часа/часов y минута/минуты/минут [часть суток]

def is_clock_correct(clock):
    if len(clock) != 2:
        return False
    elif not(is_number(clock[0]) and is_number(clock[1])):
            return False
    else:
        minutes = int(clock[1])
        hours = int(clock[0])
        if (0 <= minutes and minutes <= 59) and (0 <= hours and hours <= 23):
            return True
        else:
            return False
        
def get_clock_error(clock):
    for word in clock:
        if not is_number(word):
            return "Введены недопустимые данные: " + word + " не является целым неотрицательным числом." 
    if len(clock) != 2:
        return "Введены недопустимые данные: должно быть 2 числа" 
    else:
        minutes = int(clock[1])
        hours = int(clock[0])
        if not (0 <= minutes and minutes <= 59):
            return "Введены недопустимые данные: минуты должны быть от 0 до 59."
        elif not (0 <= hours and hours <= 23):
            return "Введены недопустимые данные: часы должны быть от 0 до 23."
        else:
            return "Ошибок нет"    

def is_number(string):
    digits = "0123456789"
    for symbol in string:
        if symbol not in digits:
            return False
    return True

def get_correct_form_of_minutes(number):
    if(11 <= number <= 19):
        return "минут"
    else:
        if(number % 10 == 1):
            return "минута"
        elif(number % 10 == 2 or number % 10 == 3 or number % 10 == 4):
            return "минуты"
        else:
            return "минут"

def get_correct_form_of_hours(number):
    if(11 <= number <= 19):
        return "часов"
    else:
        if(number % 10 == 1):
            return "час"
        elif(number % 10 == 2 or number % 10 == 3 or number % 10 == 4):
            return "часа"
        else:
            return "часов"

def get_part_of_day(hours):
    if 0 <= hours and hours <= 5:
        return "ночи"
    elif 6 <= hours and hours <= 11:
        return "утра"
    elif 12 <= hours and hours <= 17:
        return "дня"
    else:
        return "вечера"
    
def get_time(hours, minutes):
    if hours > 12:
        hours_in_12_hour_system = hours - 12
    else:
        hours_in_12_hour_system = hours
    return str(hours_in_12_hour_system) + " " + get_correct_form_of_hours(hours_in_12_hour_system) + " " + str(minutes) + " " +  get_correct_form_of_minutes(minutes) + " " + get_part_of_day(hours)

def get_time_without_minutes(hours):
    if hours > 12:
        hours_in_12_hour_system = hours - 12
    else:
        hours_in_12_hour_system = hours    
    return str(hours_in_12_hour_system) + " " + get_correct_form_of_hours(hours_in_12_hour_system) + " " + get_part_of_day(hours) + " ровно"


clock = input().split()

if is_clock_correct(clock):
    hours = int(clock[0])
    minutes = int(clock[1])
    if (hours == 0 and minutes == 0):
        print("полночь")
    elif (hours == 12 and minutes == 0):
        print("полдень")
    else:
        if minutes == 0:
            print(get_time_without_minutes(hours))
        else:
            print(get_time(hours, minutes))
else:
    print(get_clock_error(clock))

