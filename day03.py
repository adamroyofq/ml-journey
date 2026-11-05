#работа со срезами и методами
nums = [3, 8, 1, 14, 7, 20, 5]

print(nums[:3])
print(nums[-2:])
print(nums[::2])

#list comprehension с условиями 
greater_than_5 = [x for x in nums if x > 5]
doubled = [2 * x for x in nums]

print(greater_than_5)
print(doubled)

#создание словаря, вывод пар "ключ: значение" через цикл
worker = {
    "name": "Andrew",
    "age": 18,
    "skills": ["Python", "SQL", "GIT"],
    "goal": "ML engineer"
}

for key, value in worker.items():
    print(key, value)

#создание функции average_grade() вычисляющей среднюю оценку студентов.
#получение списка имен студентов с оценкой 5 с помощью list comprehension.
students = [
    {"name": "Аня", "grade": 5},
    {"name": "Борис", "grade": 3},
    {"name": "Вика", "grade": 4},
    {"name": "Глеб", "grade": 5},
]

def average_grade(students):
    total = 0
    count = 0
    for student in students:
        total += student["grade"]
        count += 1
    return total / count

top_students = [student["name"] for student in students if student["grade"] == 5]

print(average_grade(students))
print(top_students)



