# Задание 1
task = 1 # TODO << поставьте 1 для проверки первого задания или 2 для второго >>

if (task == 1):
    side = int(input("Введите сторону: ")) # Ввод только для целочисленных!
    print(f"\nПлощадь: {side ** 2}") # Вывод


# Задание 2
elif (task == 2):
    long = int(input("Введите длинну: "))
    width = int(input("Введите ширину: "))

    print(f"\nПлощадь: {long*width} \n" f"Периметр: {2 * (long+width)}")

else:
    print("Хей хей! вы не поставили какое именнно задание тестируете!\
          \n непорядок... Перечитайте комментарий на 2 строке.")
