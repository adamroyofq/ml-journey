import pandas as pd
import matplotlib.pyplot as plt

df_csv = pd.read_csv("students.csv") # чтение csv файла

# (groupby на students.csv) средняя оценка и возраст по каждому городу 
middle_grade = df_csv.groupby("city")["grade"].mean() # вычисление и группировка средней оценки по городам
middle_age = df_csv.groupby("city")["age"].mean() # вычисление и группировка среднего возраста по городам

print(middle_grade) # вывод средней оценки
print(middle_age)   # вывод среднего возраста


# сортировка по оценкам от большей к меньшей и вывод топ-3 по оценке

print(df_csv.sort_values("grade", ascending=False)) # сортировка
print(df_csv.sort_values("grade", ascending=False).head(3)) # топ 3


# работа с пропусками в данных

df_exam_csv = pd.read_csv("exam.csv") # чтение csv файла

skips_per_column = df_exam_csv.isna().sum() # подсчет пропусков в каждом столбце
exam_no_skips = df_exam_csv.dropna() # таблица без пропусков
table_null_skips = df_exam_csv[["math", "physics"]].fillna(df_exam_csv[["math", "physics"]].mean())
# вариант таблицы где места пропусков заменены средним значением по этому столбцу   

print(skips_per_column) # вывод skips_per_column
print(exam_no_skips)    # вывод exam_no_skips
print(table_null_skips) # вывод table_null_skips
print(f"len = {len(exam_no_skips)}")    # вывод количества оставшихся строк


# график с помощью plt

middle_grade.plot(kind="bar") # нарисовать столбцы 
plt.title("Средняя оценка по городам") # заголовок 
plt.ylabel("Оценка") # подпись вертикальной оси
plt.xlabel("Город") # подпись горизонтальной оси
plt.savefig("grades_by_city.png") # сохранить картинку в файл
plt.show() # показать окно с графиком

