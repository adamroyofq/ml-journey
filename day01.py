#приветстве
name = input("Как тебя зовут? ")
print(f"Привет, {name}! Начинаю путь в ML.")

#сумма и среднее чисел
numbers = [4, 8, 15, 16, 23, 42]
total = sum(numbers)
average = total / len(numbers)
print(f"Сумма: {total}, среднее: {average:.2f}")

#поиск максимального и минимального числа в списке без max/min
numbers = [6, 4, 21, 8, 19, 43, 24, 35]
MaxNumber = numbers[-1]
MinNumber = numbers[0]

for number in numbers:
    if MaxNumber < number:
        MaxNumber = number
    if MinNumber > number:
        MinNumber = number

print(f"Максимальное число {MaxNumber}, а минимальное {MinNumber}")

