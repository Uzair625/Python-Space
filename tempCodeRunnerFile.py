from sklearn.linear_model import LinearRegression
# import matplotlib.pyplot as plt
# import numpy as np

# # Example data
# sizes = np.array([1500, 2000, 2500, 3000, 3500]).reshape(-1, 1)
# prices = np.array([300000, 400000, 500000, 600000, 700000])

# # Model training
# model = LinearRegression()
# model.fit(sizes, prices)

# # Prediction
# predicted_prices = model.predict(sizes)

# # Plotting the results
# plt.scatter(sizes, prices, color='blue', label='Actual Prices')
# plt.plot(sizes, predicted_prices, color='red', label='Predicted Prices')
# plt.xlabel('Size (sq ft)')
# plt.ylabel('Price ($)')
# plt.title('Linear Regression Example')
# plt.legend()
# plt.show()


# #Second part r2 score
# from sklearn.metrics import r2_score

# r2 = r2_score(prices, predicted_prices)
# print(f"R² Score: {r2:.2f}")
