import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import os

# Ensure the output directory exists
output_dir = r"c:\Users\AMEY THAKUR\OneDrive\Desktop\Amey-Thakur.github.io\content\posts\2023-09-29-multiple-linear-regression\figures"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Given dataset
hours_studied = np.array([1.0, 3.0, 2.3, 6.0, 1.5, 7.0, 5.0, 3.3, 4.0, 2.0, 3.0, 0.0, 5.5, 4.3]).reshape(-1, 1)
grades_received = np.array([35, 55, 42, 94, 36, 96, 90, 70, 80, 39, 50, 34, 95, 83])

# Create a linear regression model
model = LinearRegression()

# Fit the model using the dataset
model.fit(hours_studied, grades_received)

# Predict the grades based on the hours studied
grades_predicted = model.predict(hours_studied)

# Plot the original data points
plt.scatter(hours_studied, grades_received, color='black')

# Plot the best fit line
plt.plot(hours_studied, grades_predicted, color='blue', linewidth=3)

plt.xlabel('Hours Studied')
plt.ylabel('Grades Received')
plt.title('Linear Regression: Best Fit Line')

# Save the figure
output_path = os.path.join(output_dir, "regression_plot.png")
plt.savefig(output_path)
print(f"Plot saved to {output_path}")

# Print the slope and intercept of the best fit line
print('Slope:', model.coef_[0])
print('Intercept:', model.intercept_)
