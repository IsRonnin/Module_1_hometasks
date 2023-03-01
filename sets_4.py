task = 2 # TODO Ну что-ж ничего не меняется...

# Задание 1
if task == 1:
    to_set = lambda list: (set(list),len(set(list)))
    print(to_set('я обычная строка'), to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]), sep="\n")
    '''а вот я не обычная строка!'''

# Задание 2
elif task == 2:
    sum_range = lambda start, end: sum(range(min([start, end]), max([start,end])+1))
    print(sum_range(2, 12), sum_range(-4, 4), sum_range(3, 2), sep="\n")

else:
    print("Ну вот опять! вы забыли что нужно указать в 1 строке номер задания!")