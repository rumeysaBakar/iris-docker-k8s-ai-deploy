from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import joblib

iris = load_iris()
X, y = iris.data, iris.target

model = LogisticRegression(max_iter=200)
model.fit(X, y)

joblib.dump(model, 'model.joblib')
print("Model kaydedildi.")
