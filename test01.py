import pandas as pd 
import matplotlib.pyplot as plt

# чтение таблицы
df = pd.read_csv("sales.csv")

# вывод размеров и количества пропусков по столбцам
print(df.shape)
print(df.isna().sum())


# удаление пропусков и запись в переменную таблицы без них
clear_df = df.dropna()
print(len(clear_df)) # вывод количества оставшихся строк


# создание столбца revenue в clear_df (price * quantity)
clear_df["revenue"] = clear_df["price"] * clear_df["quantity"]
print(clear_df)


# группировка и сортировка (суммарная выручка по категориям из clear_df)
sum_revenue = clear_df.groupby("category")["revenue"].sum()
sum_revenue = sum_revenue.sort_values(ascending=False)
print(sum_revenue)


# построение графика выручки
sum_revenue.plot(kind="bar")
plt.title("Выручка по категориям")
plt.xlabel("Категория")
plt.ylabel("Выручка")
plt.savefig("revenue_by_category.png")
plt.show()

# нахождение города-лидера (города с наибольшей суммарной выручкой)
revenue_by_city = clear_df.groupby("city")["revenue"].sum()

top_city_sum = revenue_by_city.max()
top_city_name = revenue_by_city.idxmax()

# вывод города с максимальной выручкой и самой суммы выручки
print(f"{top_city_name}: {top_city_sum}")