def square_print(x):
    print(x * x)

def square_return(x):
    return x * x

a = square_return(5)   
b = square_print(5)    

def find_max(numbers):

    MaxNumber = numbers[-1]

    for number in numbers:
        if MaxNumber < number:
            MaxNumber = number

    return MaxNumber 

def find_min(numbers):
    MinNumber = numbers[0]

    for number in numbers:
        if MinNumber < number:
            MinNumber = number

    return MinNumber

def average(numbers):
    total = 0
    count = 0

    for number in numbers:
        total += number #тоже самое можно было указать sum(numbers) / len(numbers)
        count += 1      #но для обучения я подумал что этот вариант даже лучше
    result = total / count

    return result

def is_even(x):
    return x % 2 == 0:

print(find_max([4, 6, 1, 17, 44, 2]))
print(find_min([4, 6, 1, 17, 44, 2]))
print(average([5, 9, 11, 25, 41, 13]))
print(is_even(6))
print(is_even(5))