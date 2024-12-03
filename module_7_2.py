# Создаём функцию custom_write(file_name, strings) с аргументами
# file_name - название файла для записи,
# strings - список строк для записи.
def custom_write(file_name, strings):
    strings_positions = {}
# Далее записываем в файл file_name все строки из списка strings, где каждая на новой строке.
# Возвращаем словарь strings_positions, где ключом будет кортеж
# (<номер строки>, <байт начала строки>), а значением будет записываемая строка.
# Для получения номера байта начала строки будем использовать метод tell() перед записью.
    with open(file_name, 'w', encoding='utf-8') as file:
        for index, string in enumerate(strings, start=1):
            byte_position = file.tell()  # Получаем текущую позицию в байтах
            file.write(string + '\n')  # Записываем строку в файл с переходом на новую строку
            strings_positions[(index, byte_position)] = string  # Сохраняем информацию в словаре
    return strings_positions

# Пример как тест выполняемого кода
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]
# Создается список строк info, который передается в функцию custom_write.
# Результат выполнения функции выводится на консоль.
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
