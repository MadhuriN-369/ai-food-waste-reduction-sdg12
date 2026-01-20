from sklearn.linear_model import LinearRegression
from data_preprocessing import load_data, preprocess

data = load_data("../data/sample_data.csv")
X, y = preprocess(data)

model = LinearRegression()
model.fit(X, y)

prediction = model.predict([[8]])
print("Predicted demand for day 8:", prediction[0])
