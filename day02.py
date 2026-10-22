def find_max(numbers): #поиск максимального значения в списке без max()

    max_number = numbers[-1]

    for number in numbers:
        if max_number < number:
            max_number = number

    return max_number

def find_min(numbers): #поиск минимального значения в списке без min()
    min_number = numbers[0]

    for number in numbers:
        if min_number > number:
            min_number = number

    return min_number

def average(numbers): # поиск среднего значения без sum(), len()
    total = 0
    count = 0

    for number in numbers:
        total += number
        count += 1
    result = total / count #тоже самое можно было указать sum(numbers) / len(numbers)
                            #но для обучения я подумал что этот вариант даже лучше
    return result

def is_even(x):
    return x % 2 == 0

print(find_max([4, 6, 1, 17, 44, 2]))
print(find_min([-2, 5, 3, 27, -34, -7]))
print(average([5, 9, 11, 25, 41, 13]))
print(is_even(6))
print(is_even(5))