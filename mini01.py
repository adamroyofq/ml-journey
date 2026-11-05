import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

temps = np.array([12, 18, 25, 31, 22, 15, 9])

print(f"Температуры выше 20: {temps[temps > 20]}")
print(f"Средняя температура: {temps.mean()}")
print(f"Индекс самого теплого дня: {temps.argmax()}")


temp_per_day = pd.DataFrame({
    "day": ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"],
    "temp": [12, 18, 25, 31, 22, 15, 9]
})

temp_per_day["hot"] = temp_per_day["temp"] >= 25
hot_days_count = temp_per_day["hot"].sum()


print(f"Жарких дней: {hot_days_count}")
print(f"Три самых теплых дня в табличном виде:\n{temp_per_day.sort_values("temp", ascending=False).head(3)}")


# столбчатый график температур по дням
temp_per_day.plot(kind="bar", x="day", y="temp")
plt.title("График температур по дням")
plt.xlabel("День")
plt.ylabel("Температура")
plt.savefig("temps.png")
plt.show()