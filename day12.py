from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, classification_report

# подготовка данных
data = load_breast_cancer(as_frame=True)
df = data.frame

print(df.shape)
print(df.head())

# разделение данных на тренировочные и тестовые 
X = df.drop(columns="target")
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

print(X_train.shape)
print(X_test.shape)

# создание модели
model = LogisticRegression(max_iter=5000)
model.fit(X_train, y_train)
predictions = model.predict(X_test)

# точность модели
print(accuracy_score(y_test, predictions))

print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))
