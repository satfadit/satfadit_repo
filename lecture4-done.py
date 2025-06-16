def sieve_of_eratosthenes(n):
    # Создаем список булевых значений, где True означает, что число простое
    is_prime = [True] * (n + 1) 
    p = 2
    while (p * p <= n):
        if (is_prime[p] == True):
            # Обновляем все кратные p как не простые
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    # Выводим простые числа
    for p in range(2, n + 1):
        if is_prime[p]:
            print(p)

def main():
    try:
        # Запрос ввода от пользователя
        n = int(input("Введите целое число N для поиска всех простых чисел от 2 до N: "))
        if n < 2:
            print("Введите число больше или равное 2.")
        else:
            sieve_of_eratosthenes(n)
    except ValueError:
        print("Некорректный ввод! Пожалуйста, введите целое число.")

if __name__ == "__main__":
    main()