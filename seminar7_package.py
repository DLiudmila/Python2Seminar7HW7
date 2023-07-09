from random import randint, uniform, choice
from pathlib import Path
import os

MIN = -1000
MAX = 1000
DIC1 = "AIEYUO"
DIC2 = "QWRTPSDFHGKL"
RAND = 15


# Задание 1 Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.
def random_numbers(numb, name):

    with open(name, "a", encoding="utf-8") as f:
        for _ in range(numb):
            n1 = randint(MIN, MAX)
            n2 = uniform(MIN, MAX)
            f.write(f'{n1} | {n2} \n')



# Задание 2 Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.
def names():
    with open("filik.txt", "w", encoding="utf-8") as f:
        for i in range(RAND):
            name = ""
            for i in range(randint(2, 4)):   # генерация слов, состоящих от 4 до 7 букв
                name += choice(DIC1)
                if len(name) >= 7: break
                name += choice(DIC2)
            f.write(f'{name} \n')


# Задание №3
# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.
def mult():
    with (
        open('fl.txt', 'r', encoding='utf-8') as numbers,  # открытие файла с парами чисел для чтения
        open('filik.txt', 'r', encoding='utf-8') as liter, # открытие файла с псевдоименами для чтения
        open('result', 'a', encoding='utf-8') as r         # создание и открытие нового файла для записи результатов
    ):
        while res_n := numbers.readline():                # чтение по строкам и присваивание результатов
            a = res_n.replace(' \n', '').split(" | ")     # разделение содержимого по "|"  и удаление лишних символов (возвращает список)

            if a == ['\n']:                               # игнорирование последней строки с лишним знаком перехода на новую строку
                continue
            mult_ = int(a[0]) * float(a[1])
            if mult_ < 0:
                res_l = liter.readline().replace(' \n', '') # удаление лишних символов после имен
                r.write(f'{res_l.lower(), abs(mult_)} \n')
            elif mult_ >= 0:
                r.write(f'{res_l.upper(), round(mult_)} \n')



# Задание №4
# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона

def create_file_with_extension(text, a=5, b=30, c= 7, d=256, n = 42):
    for _ in range(n):
        name = ""
        for i in range(randint(6, 30)):
            name += choice(DIC1)
            if len(name) >= 30: break
            name += choice(DIC2)
        name = name + '.' + text              # формируется название файла
        with open(name, 'w', encoding='utf-8') as new_f:
            g = bytes(randint(0, 255) for i in range(randint(256, 4096)))
            new_f.write(f'{g}')


# Задание №5
# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи

def generate_files_with_extensions(dic, a=5, b=30, c=7, d=256):
    for key in dic:
        for _ in range(dic[key]):         # формируем файлы в количестве, указанном в словаре для каждого расширения
            name = ""
            for i in range(randint(6, 30)):
                name += choice(DIC1)
                if len(name) >= 30: break
                name += choice(DIC2)
            name = name + '.' + key
            with open(name, 'w', encoding='utf-8') as new_f:
                g = bytes(randint(0, 255) for i in range(randint(256, 4096)))
                new_f.write(f'{g}')


# Задание №6
# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

def generate_files_to_folder(dic, a=5, b=30, c=7, d=256):
    for key in dic:
        for _ in range(dic[key]):
            name = ""
            for i in range(randint(6, 30)):
                name += choice(DIC1)
                if len(name) >= 30: break
                name += choice(DIC2)
            name = name + '.' + key
            if Path(name).is_file():
                continue
            with open(name, 'w', encoding='utf-8') as new_f:
                g = bytes(randint(0, 255) for i in range(randint(256, 4096)))
                new_f.write(f'{g}')

def dir(text):    # создание директории
    if isinstance(text, str):
        a = Path(text)  # преобразование в class 'pathlib.WindowsPath'
    else:
        a = text
    if not a.is_dir():
        a.mkdir(parents=True)
    os.chdir(a)
    generate_files_to_folder({"txt": 5, "doc": 3}, a=5, b=30, c=7, d=256)


# Задание №7
# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
def sort_file(dict_file_extension, dir_name):
    if isinstance(dir_name, str):
        dir_name = Path(dir_name)
    else:
        dir_name = dir_name
    os.chdir(dir_name)
    for key in dict_file_extension:
        a = Path(key)
        if not a.is_dir():
            a.mkdir(parents=True)

    p = Path(Path().cwd())
    for obj in p.iterdir():
        for key in dict_file_extension:
            if obj.suffix in dict_file_extension[key]: # проверка на соответствие расширения файла расширению, указанному в списке для сортировки по папкам
                obj.replace(p / key / obj.name)


# dict_file_extension = {'video': ['.mov', '.avi', '.mp4'], 'docum': ['.txt', '.doc']}
# sort_file(dict_file_extension, 'C:\Учеба Инженер по тестированию 150 000 р\pythonProject\Sem7')


# 8. Напишите функцию группового переименования файлов. Она должна:
# принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# принимать параметр количество цифр в порядковом номере.
# принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# принимать параметр расширение конечного файла.
# принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
def rename_files(desired_name, number_digits, original_extension, new_extension, name_range=None):
    # Получаем список файлов в текущем каталоге
    file_list = os.listdir()

    # Фильтруем файлы, оставляя только те, у которых расширение соответствует original_extension
    filtered_files = [file for file in file_list if file.endswith(original_extension)]

    # Если не указан диапазон, используем всё имя файла
    if name_range is None:
        name_start = 0
        name_end = None
    else:
        name_start = name_range[0]
        name_end = name_range[1]

    # Счетчик для порядкового номера
    count = 1

    # Переименовываем каждый файл
    for old_name in filtered_files:

        # Получаем оригинальное имя для создания нового имени файла
        original_name = old_name[name_start:name_end]

        # Форматируем порядковый номер с указанным количеством цифр
        number = str(count).zfill(number_digits)

        # Создаем новое имя файла, добавляя оригинальное имя, если оно указано, и порядковый номер
        new_name = f"{original_name}_{desired_name}_{number}{new_extension}"

        # Переименовываем файл
        os.rename(old_name, new_name)

        # Увеличиваем счетчик порядкового номера
        count += 1

