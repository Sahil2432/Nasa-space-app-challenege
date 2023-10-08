import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
dataset = pd.read_csv("file.csv")

print(dataset.shape)
print(dataset)

# Calculate the correlation matrix
dataset2 = dataset.corr()
print(dataset2)

# Write the correlation matrix to a CSV file
dataset2.to_csv("correlation_matrix.csv")

# Scatter plot
x = dataset['Number']
y = dataset['name']
plt.xlabel('Number')
plt.ylabel('name')
plt.scatter(x, y)
plt.show()
