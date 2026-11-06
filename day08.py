f = lambda x: x**2
h = 0.001

print((f(1 + h) - f(1)) / h)
print((f(3 + h) - f(3)) / h)
print((f(-2 + h) - f(-2)) / h)


# создание функции 
def derivative(f, x):
    h = 0.001
    return (f(x + h) - f(x)) / h

print(derivative(f, 3))

# цикл спуска
fnc = lambda x: (x - 3)**2
x = 0
lr = 0.1

for step in range(20):
    grad = derivative(fnc, x)
    x -= lr * grad
    print(f"Шаг: {step} X: {x}")


# цикл спуска (Эксперимент 1)
fnc = lambda x: (x - 3)**2
x = 0
lr = 0.01

for step in range(20):
    grad = derivative(fnc, x)
    x -= lr * grad
    print(f"Шаг: {step} X: {x}")

# цикл спуска (Эксперимент 2)
fnc = lambda x: (x - 3)**2
x = 0
lr = 1.0

for step in range(20):
    grad = derivative(fnc, x)
    x -= lr * grad
    print(f"Шаг: {step} X: {x}")

# цикл спуска (Эксперимент 3)
fnc = lambda x: (x - 3)**2
x = 0
lr = 1.1

for step in range(20):
    grad = derivative(fnc, x)
    x -= lr * grad
    print(f"Шаг: {step} X: {x}")