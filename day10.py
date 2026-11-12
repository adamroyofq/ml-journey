import numpy as np 
import matplotlib.pyplot as plt

x = np.array([1, 2, 3])
y = np.array([3, 5, 7])
w = 0.0
b = 0.0
lr = 0.05   
losses = []

for step in range(2000):
    slope_w = (2 * (w * x + b - y) * x).mean()
    slope_b = (2 * (w * x + b - y)).mean()
    w = w - lr * slope_w
    b = b - lr * slope_b
    loss = ((w * x + b - y) ** 2).mean()
    losses.append(loss)
    if step % 200 == 0:
        print(f"W:{w}, B:{b}")
print(f"W:{w}, B:{b}")


# график обучения
plt.plot(losses)
plt.title("Кривая обучения")
plt.xlabel("шаги")
plt.ylabel("ошибка")
plt.savefig("loss_curve.png")
plt.show()

print(np.polyfit(x, y, 1))