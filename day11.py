from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import pandas as pd 
import numpy as np 
import joblib

rng = np.random.default_rng(42)
area = rng.uniform(30, 120, 200)      # 200 площадей от 30 до 120
rooms = rng.integers(1, 5, 200)       # 200 чисел комнат: 1, 2, 3 или 4
noise = rng.normal(0, 5000, 200)      # случайный разброс (в жизни цены не по формуле)
price = 1000 * area + 5000 * rooms + 10000 + noise

# создание пандас датафрейма для работы с данными
model_df = pd.DataFrame({
    "area": area,
    "rooms": rooms,
    "price": price
})

print(model_df.head())
print(model_df.describe())

model_df.to_csv("houses.csv", index=False)

X = model_df[["area", "rooms"]]
y = model_df["price"]

#разделение данных на тренировочные и тестовые
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# создание пустой модели и ее обучение (вид обучения "с учителем" данные + ответы)
model = LinearRegression()
model.fit(X_train, y_train)

print(model.coef_)
print(model.intercept_)

# проверка качества модели
predictions = model.predict(X_test)

print(mean_absolute_error(y_test, predictions))
print(r2_score(y_test, predictions))


# предсказание для нового дома
new_house = pd.DataFrame([[75, 3]], columns=["area", "rooms"])
print(model.predict(new_house))


# сохранение модели в файл
joblib.dump(model, "model.joblib")  
loaded = joblib.load("model.joblib") 
print(loaded.predict(new_house))