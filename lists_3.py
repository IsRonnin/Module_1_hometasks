task = 1 # TODO Напоминашка! не забудьте поставить номер задания!

# Задание 1
if task == 1:
    your_num = int(input("Введите ваше число: "))
    table = [print(f"{i} * {your_num} = {i * your_num}") for i in range(1, 13)] # <- тут-а краткая запись for
# Задание 2

elif task == 2:
    def hey_array(your_arr: list): # функция вывода списка - для разнообразия что-ли?
        print(your_arr)

    arr = [i for i in range(1, 11)]
    hey_array(arr)
    print(arr[0], arr[1], sep="\n")
    hey_array(arr)
    arr[8] = 99 # замена по индексу 8 на 99
    hey_array(arr)
    arr.append(49) # вставка в конец числа 49
    hey_array(arr)
    arr.insert(5, 49) # вставка 49 по индексу 5
    hey_array(arr)
    arr = arr[1:] # удаление первого элемента. почему не remove? Потому что скучно!
    hey_array(arr)
    arr = arr[::-1] # переворот. да можно и так -> arr.reverse() я об этом знаю, не стукайте меня!
    hey_array(arr)
    print(f"{arr.count(4)} чётвёрка-(ок)")
    hey_array(arr)
    print(''.join([(f"{i}-") for i in arr])[0:-1])
    hey_array(arr) # Вы сами сказали после каждого ;3
    print(f"{len(arr)} Элементов в списке")
    hey_array(arr) # да да! так всё и было

    # Уф какое оно всё таки обьёмное... 
