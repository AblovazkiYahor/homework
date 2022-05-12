from datetime import datetime

"""№4. Написать декоратор к двум любым функиям, который бы считал и выводил время бы считал и выводил время
их выполнения."""

def decorator(func):

    def wrapper():
        start_time = datetime.now()
        end_time = datetime.now()
        res = func
        print('Duration: {}'.format(end_time - start_time))
        return res
    return wrapper()

"""№1. Написать лямбда-функцию определяющую четное/нечетное число."""

la = lambda x: "Число четное" if not x % 2 == 1 else "Число нечетно"
print(la(3))
print(la(2))
print()


"""№2. """
@decorator
def for_map():
    print(list(map(lambda x: str(x + 0), [1, 2, 3, 4, 5])))

for_map()

print()

"""N3 При помощи функции filter() из котрежа слов отфильтровать только те которые являются палиндромами."""
@decorator
def palindroms():
    word = ("кот", "дед", "казак", "доход", "авто", "книга")
    palindromes = list(filter(lambda word: word == word[::-1], word))
    print("Слова палиндромы: ", list(palindromes))

palindroms()



"""№5. """

