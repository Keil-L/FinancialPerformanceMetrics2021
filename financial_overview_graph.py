
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Creating a mock dataset
np.random.seed(0)
dates = pd.date_range('20210101', periods=100)
data = pd.DataFrame({
    'Sales': np.random.randn(100).cumsum() + 100,
    'Expenses': np.random.randn(100).cumsum() + 80,
    'Profit': np.random.randn(100).cumsum() + 20
}, index=dates)

# Plotting the data
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['Sales'], label='Sales', color='blue', linewidth=2)
plt.plot(data.index, data['Expenses'], label='Expenses', color='red', linewidth=2)
plt.plot(data.index, data['Profit'], label='Profit', color='green', linewidth=2)

# Adding titles and labels
plt.title('Company Financial Overview (2021)', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Amount ($)', fontsize=12)
plt.legend()

# Enhancing the design
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()
