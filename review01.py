import pandas as pd
import matplotlib.pyplot as plt

# чтение таблицы
df_csv = pd.read_csv("students.csv") 


# вывод таблицы и ее размера
print(df_csv)
print(df_csv.shape)


# вывод средней оценки по каждому городу
mean_grade_per_city = df_csv.groupby("city")["grade"].mean()
print(mean_grade_per_city)


# вывод студентов с оценкой 5 таблицей
print(df_csv[df_csv["grade"] == 5])


# вывод имен студентов с оценкой 5 списком
top_students = df_csv[df_csv["grade"] == 5]
top_students_list = top_students["name"].tolist()
print(top_students_list)


# добавление столбца "adult", где True возраст >= 20
df_csv["adult"] = df_csv["age"] >= 20 
print(df_csv)
# сортировка от большего к меньшему и вывод 3 самых старших
print(df_csv.sort_values("age", ascending=False).head(3))



# столбчатая диаграмма сколько студентов в каждом городе 
students_city = df_csv.groupby("city").size() # подсчет кол студентов в каждом городе

# построение, сохранение и вывод графика 
students_city.plot(kind="bar")
plt.title("сколько студентов в каждом городе")
plt.ylabel("колличество студентов")
plt.xlabel("города") 
plt.savefig("students_review.png") 
plt.show()