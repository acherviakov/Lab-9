

from tabulate import *
from random import *
'''
Сортировка пузырьком для массива, длиной n:
    Повторим n - 1 раз:
        создадим счётчик сравнений
        создадим счётчик перестановок
        попарно сравниваются элементы массива;
        +1 к счетчику сравнений
        Если первый элемент больше второго, то их значения обмениваются между собой и +1 к счётчику перестановок.
        если за проход не было совершено ни одной перестановки, то закончить сортировку
'''
def bubble_sort(array):
    comparation_counter = 0
    swap_counter = 0
    no_swaps = False
    times_repeated = 0
    
    while( not no_swaps and times_repeated < len(array) - 1):
        no_swaps = True
        array, add_comparations, add_swaps = one_cycle_of_bubble_sort(array)
        if(add_swaps != 0):
            no_swaps = False
        swap_counter += add_swaps
        comparation_counter += add_comparations
    return [array, comparation_counter, swap_counter]
    

def one_cycle_of_bubble_sort(array):
    comparation_counter = 0
    swap_counter = 0
    for i in range(1, len(array)):
        if array[i-1] > array[i]:
            array[i-1], array[i] = array[i], array[i-1]
            swap_counter += 1
        comparation_counter += 1
    return (array, comparation_counter, swap_counter)
'''
Сортировка простым выбором для массива, длиной n:
    Находится максимальный элемент в массиве:
        Сделаем текущий максимум первым элементом
        Для каждого элемента, сделаем его текущ. макс., если он больше текущ. максимума
        +1 к счетчику сравнений
    Пока в массиве отсортировано менее n - 1 элемнтов (если n - 1 отсортировано => оставшийся отсортирован => Массив отсортирова)
    Найденное значение обменивается со значением первого максимального по индексу неотсортированного элемента;
    Сортируется оставшаяся часть массива (отсортированные элементы не рассматриваются).
'''
def selection_sort(array):
    comparation_counter = 0
    swap_counter = 0
    sorted_elements_amount = 0
    while sorted_elements_amount < (len(array) - 1):
        max_index, add_comparations = find_max(array[0:len(array)-sorted_elements_amount])
        array[max_index], array[len(array)-1-sorted_elements_amount] = array[len(array)-1-sorted_elements_amount], array[max_index]
        swap_counter += 1
        comparation_counter += add_comparations
        sorted_elements_amount += 1
    return [array, comparation_counter, swap_counter]
'''
Сортировка вставками от 1 до n:
    Для каждого элемента начиная со второго:
        Пока индекс больше нуля и значение меньше значения предыдущего элемента (+1 сравнение):
            обменяем этот элемент с предыдущим 
            повторим для предыдущего элемента.
            +1 к перестановкам
'''
def one_cycle_of_insertion_sort(array, index):
    comparation_counter = 0
    swap_counter = 0
    while index > 0 and (array[index] < array[index - 1]):
        comparation_counter += 1
        array[index], array[index - 1] = array[index - 1], array[index]
        index -= 1
        swap_counter += 1
    comparation_counter += 1
    return (array, comparation_counter, swap_counter)


def insertion_sort(array):
    comparation_counter = 0
    swap_counter = 0
    for index in range(1, len(array)):
        array, add_comparations, add_swaps = one_cycle_of_insertion_sort(array, index)
        comparation_counter += add_comparations
        swap_counter += add_swaps
        
    return [array, comparation_counter, swap_counter]


def find_max(array):
    comparation_counter = 0
    current_max = array[0]
    current_max_index = 0
    for index in range(1, len(array)):
        comparation_counter += 1
        if array[index] > current_max:
            current_max = array[index]
            current_max_index = index
    return current_max_index, comparation_counter

'''
Проверка строки на число в диапазоне (включтельно):
1. Перебирая все символы в строке, проверим, что первый символ цифра или минус, а все остальные - цифры.
2. Представим строку в виде числа
3. Проверим, что данное число находится в диапазоне.
4. Получим это число
'''
'''
Проверка строки на число:
0. Проверим, что строка не пустая!!!
1. Перебирая все символы в строке, проверим, что первый символ цифра или минус, а все остальные - цифры
2. Если это не так, то заявим об этом, иначе об обратном
'''
def is_number(string):
    digits ="1234567890"
    first_symbols_possible = "-1234567890"
    if string == "":
        return False
    if string[0] not in first_symbols_possible:
        return False
    for i in range(1, len(string)):
        if string[i] not in digits:
            return False
    return True
'''
Предложить два вида работы: демонстрационный (число 1) и интерактивный (число 2).
Если пользователь вводит число 1, 
то запустить демонстрационный режим.
Если пользователь вводит число 2, 
то запустить интерактивный режим.
Если пользователь вводит что-то другое, сказать, 
что нужно ввести 1 или 2, 
повторить шаг 1.
'''
def start():
    print("Выберите режим работы: интерактивный (введите 2) или демонстративный (введите 1)")
    mode = input()
    if mode == "1":
        run_demo_mode()
    elif mode == "2":
        run_interactive_mode()
    else:
        start()

'''
Если режим работы демонстрационный, то:
1. создадим массив из 1000 случайных элементов от 0 до 99.
2. отсортировать массив пузырьком (простым обменом)
3. отсортировать массив вставками
4. отсортировать способом
5. вывести режим результатов
6. предложить выйти, введя любую строку
'''
def run_demo_mode():
    array = [randint(0, 99) for index in range(1000)]
    array_copy = array.copy()
    table = []
    table.append(["Сортировка пузырьком"] + bubble_sort(array)[1:])
    table.append(["Cортировка простым выбором"] + selection_sort(array)[1:])
    array = array_copy
    table.append(["Cортировка вставками"] + insertion_sort(array)[1:])
    headers = ["Сортировка", "Сравнения", "Перестановки" ]
    print(tabulate(table, headers=headers))
    print("Введите любую строку, чтобы выйти")
    users_input = input()
    start()    




'''

Если режим работы интерактивный, то:
1. Предложить ввести размер массива, если он не является числом, то написать об этом и повторить операцию
2. Сгенерировать массив (случайные числа от 0 до 99)
2+. Сохранить себе его.
3-5. вывести таблицу
6. Спросить пользователя о его дальнейших действиях.
7. Если пользователь ввёл 1, то замена части массива:
    Вводится начальный индекс замены, часть массива.
    +проверка, чтобы введенные данные являлись числами 
    и начальный индекс находится от 0 до длины массива, 
    иначе повторить ввод
    +проверить, что сумма индекса замены 
    и длины части массива не больше, чем индекс последнего элемента, 
    иначе повторить ввод
    +следующие n элемнтов, где n - длина части массива, заменим элементы из этого массива
8. Если пользователь ввёл 2,
 то вывести массив (отсортированный)
8+. Если пользователь ввёл 3, 
то вывести неотсортированный массив
9. Если пользователь ввёл 4, 
то повторить сначала
10. Если пользователь ввёл 5, 
то выйти из режима
11. Во всех остальных случаях повторить ввод




'''

'''
1. выполнить сортировку пузырьком
2. выполнить сортировку выбором
3. выполнить сортировку вставками
4. вывести в виде таблицы
'''
def show_table(array, unsorted_array):
    table = []
    table.append(["Сортировка пузырьком"] + bubble_sort(array)[1:])
    array = unsorted_array.cpoy()
    table.append(["Cортировка простым выбором"] + selection_sort(array)[1:])
    array = unsorted_array.copy()
    table.append(["Cортировка вставками"] + insertion_sort(array)[1:])
    headers = ["Сортировка", "Сравнения", "Перестановки" ]
    print(tabulate(table, headers=headers))

'''
Проверим, что все элемнты списка - числа
'''
def is_number_array(array):
    for element in array:
        if not(is_number(element)):
            return False
    return True

def action(array, unsorted_array):
    action_code = input()
    if action_code == "1":
        starter_position = 0
        print("Введите индекс, начиная с которого хотите сделать замену")
        possible = False
        while not possible:
            value = input()
            if(not is_number(value)):
                print("Введите число, а не " + value)
            else:
                if int(value) >= len(unsorted_array):
                    print("Ошибка. Стартовый элемент не должен лежать за пределами массива")
                else:
                    possible = True
                    starter_position = int(value)
        print("Введите массив (числа через пробел), на который вы хотите заменить часть исх. массива")
        possible = False
        number_replacement_list = []
        while not possible:
            value = input().split()
            if(not is_number_array(value)):
                print("Не все элементы массива - числа. Введите числа, разделенные пробелом")
            else:
                if len(value) + starter_position > len(array):
                    print("Ошибка. Конечный элемент за рамками массива.")
                else:
                    possible = True
                    number_replacement_list = list(map(int, value))
        unsorted_array = unsorted_array[0:starter_position]+number_replacement_list+unsorted_array[starter_position+len(number_replacement_list):]
        action(array, unsorted_array)
        



    elif action_code == "2":
        print(array)
        action(array, unsorted_array)
    elif action_code == "3":
        print(unsorted_array)
        action(array, unsorted_array)
    elif action_code == "4":
        array = unsorted_array.copy()
        show_table(array, unsorted_array)
        action(array, unsorted_array)
    else:
        start()

def run_interactive_mode():
    size = ""
    size_possible = False
    print("Введите длину массива")
    while not size_possible:
        size = input()
        if(not is_number(size)):
            print("Введите число, а не " + size)
        else:
            if int(size) < 0:
                print("Длина массива должна быть неотрицательной. Введите неотрицательное число")
            else:
                size_possible = True
    array = [randint(0, 99) for index in range(int(size))]
    unsorted_array = array.copy()
    show_table(array, unsorted_array)
    print("Чтобы изменить массив (изначальный), введите 1. Чтобы вывести его (будет выведен отсортированный), введите 2. Чтобы вывести неотсортированный (изначальный) массив, введите 3. Чтобы отсорировать ещё раз, введите 4. Чтобы выйти, введите любую другую строку")
    action(array, unsorted_array)
    
start()
