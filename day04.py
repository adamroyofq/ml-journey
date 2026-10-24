# создание DataFrame из списка мини-словарей "students"
import pandas as pd 

students = [
    {"name": "Аня", "grade": 5},
    {"name": "Борис", "grade": 3},
    {"name": "Вика", "grade": 4},
    {"name": "Глеб", "grade": 5},
]

df = pd.DataFrame(students)
print(df)

# получение средней оценки, получение таблицы студентов с оценкой 5 и списка имен студентов
print(df["grade"].mean()) # среднее арифметическое 
top_students = df[df["grade"] == 5]
top_names = top_students["name"].tolist()
print(top_students) # вывод строк таблицы для студентов  у которых "5"
print(top_names) # вывод списка студентов с "5"

# добавление столбца "passed" тип данных "bool", для фильтра студентов с оценкой 4 и выше
df["passed"] = df["grade"] >= 4 # новый столбец с bool значениями
print(df) # вывод всей таблицы
print(df["passed"].sum()) # сколько студентов сдали
print(df["passed"].mean()) # доля сдавших 

# Работа с данными из CSV файла, осмотр датасета через методы pandas
df_csv = pd.read_csv("students.csv")

print(df_csv) # вывод таблицы целиком
print(df_csv.head()) # показывает первые 5 строк таблицы для быстрого анализа
print(df_csv.shape) # подсчет столбцов и строк таблицы (строки, столбцы)
df_csv.info() # информация о типах данных столбцов, занятой памяти и т.д.
print(df_csv.describe()) # статистика по числовым столбцам (среднее, минимум, максимум, квартили)


# сколько студентов из каких городов в таблице
students_per_city = df_csv["city"].value_counts()
print(students_per_city)
