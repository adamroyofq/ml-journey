import numpy as np 

x = np.array([1, 2, 3])
y = np.array([3, 6, 9])
w = 0.0
lr = 0.01

for step in range(100):
    # 1. расчет склона: среднее от 2 * (w*x - y) * x по всем точкам
    slope = (2 * (w * x - y) * x).mean()
    # 2. обновление w: w = w - lr * склон
    w = w - lr * slope
    # 3. каждые 10 шагов вывод w
    if step % 10 == 0:
        print(w)
print(w) # вывод 100