
# Напишите функцию группового переименования файлов. Она должна:
# принимать параметр желаемое конечное имя файлов. При переименовании в конце имени
# добавляется порядковый номер.
# принимать параметр количество цифр в порядковом номере.
# принимать параметр расширение исходного файла. Переименование должно работать только
# для этих файлов внутри каталога.
# принимать параметр расширение конечного файла.
# Далее счётчик файлов и расширение.
# Пример:
# a.txt , b.txt , c.txt -> a_rename1.md , b_rename2.md , c_rename3.md
#
# 3.Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

import os

def bulk_rename(new_name: str, changeable_format: str, new_form: str, count_number: int):
    """
    функцию группового переименования файлов

    :param new_name:
    :param find_f:
    :param new_form:
    :param count_number:
    :return:
    """

    file_dir = os.listdir()
    counter_file = 0

    for i in file_dir:
        old_name, old_extension = i.split(".")
        if old_extension == changeable_format:
            counter_file += 1
            os.rename(i, f"{old_name}_{new_name}{count_number}.{new_form}")
            count_number += 1
            print(f"Периименовали файл-{i} на -------- {old_name}_{new_name}{count_number}.{new_form}")
    print(f"всего фалов периименовано - {counter_file}")


bulk_rename("file","txt", "md", 1)