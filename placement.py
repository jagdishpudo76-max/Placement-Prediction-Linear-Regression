
# 1. Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 2. Load Dataset
dataset = pd.read_csv("placement.csv")

# 3. Data Understanding
print(dataset.head())
print(dataset.info())

# 4. Separate Independent and Dependent Variables
x = dataset.iloc[:, 0:1]
y = dataset.iloc[:, -1]

print("Independent Variable (CGPA):")
print(x.head())

print("Dependent Variable (Package):")
print(y.head())

# 5. Data Visualization
plt.scatter(dataset['cgpa'], dataset['package'])
plt.xlabel('CGPA')
plt.ylabel('Package')
plt.title('CGPA vs Placement Package')
plt.show()

# 6. Split Dataset into Training and Testing
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=2
)

# 7. Create Linear Regression Model
from sklearn.linear_model import LinearRegression

lr = LinearRegression()

# 8. Train Model
lr.fit(x_train, y_train)

# 9. Predict Package
y_pred = lr.predict(x_test)

print("Actual Package:")
print(y_test.values)

print("Predicted Package:")
print(y_pred)

# 10. Model Evaluation
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error, r2_score

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("MAE:", mae)
print("MSE:", mse)
print("R2 Score:", r2)

# 11. Predict Package for New CGPA
new_cgpa = pd.DataFrame({'cgpa': [8.5]})

predicted_package = lr.predict(new_cgpa)

print("Predicted Package for CGPA 8.5:",
      predicted_package[0])
