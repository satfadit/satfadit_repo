# Функция для конвертации температуры
def convert_temperature(temp):
    # Проверка окончания на 'C' - градусы Цельсия
    if temp[-1].upper() == 'C':
        celsius = float(temp[:-1])  # Получаем числовое значение из строки, убрав последний символ
        fahrenheit = celsius * 9/5 + 32  # Перевод в Фаренгейты по формуле
        return f"{fahrenheit}F"  # Возвращаем результат с указанием шкалы

    # Проверка окончания на 'F' - градусы Фаренгейта
    elif temp[-1].upper() == 'F':
        fahrenheit = float(temp[:-1])  # Аналогично получаем значение
        celsius = (fahrenheit - 32) * 5/9  # Перевод в Цельсий
        return f"{celsius}C"  # Возвращаем результат с указанием шкалы

    else:
        return "Некорректный ввод, попробуйте снова."  # Сообщение об ошибке

# Основная часть программы
if __name__ == "__main__":
    user_input = input("Введите температуру с указанием шкалы (например, 20C или 68F): ")
    result = convert_temperature(user_input)
    print(result)  # Вывод результата