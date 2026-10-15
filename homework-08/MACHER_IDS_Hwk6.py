# Part 1
import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the housing dataset
housing = fetch_california_housing()

X = pd.DataFrame(housing.data, columns=housing.feature_names)
y = pd.Series(housing.target, name="med_house_value")

# First five rows
print(X.head())

# Feature names and missing values
print(housing.feature_names)
print(X.isnull().sum())

# Summary statistics
print(X.describe())

# Part 2
# Split the data (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit the linear regression model on unscaled data
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)

# Make predictions on the test set
y_pred = lin_reg.predict(X_test)

# Evaluate model performance
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
print("MSE:", mse)
print("RMSE:", rmse)
print("R2:", r2)

# Model coefficients
print(pd.Series(lin_reg.coef_, index=X.columns))

# Part 3
# Select three features
features = ["MedInc", "HouseAge", "AveRooms"]
X_train_s = X_train[features]
X_test_s = X_test[features]

# Fit the simplified model
lin_reg_s = LinearRegression()
lin_reg_s.fit(X_train_s, y_train)
y_pred_s = lin_reg_s.predict(X_test_s)

# Evaluate the simplified model
mse_s = mean_squared_error(y_test, y_pred_s)
rmse_s = np.sqrt(mse_s)
r2_s = r2_score(y_test, y_pred_s)

print("Full       -> MSE:", mse, "RMSE:", rmse, "R2:", r2)
print("Simplified -> MSE:", mse_s, "RMSE:", rmse_s, "R2:", r2_s)