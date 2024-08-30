import csv
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

# Read the data from the CSV file
data = pd.read_csv('temperature_data.csv')

# Convert time column to datetime format
data['time'] = pd.to_datetime(data['time'])

# Extract minute-level data
data['minute'] = data['time'].dt.floor('T')

# Group data by each minute
grouped = data.groupby('minute')['temp']

# Calculate statistics for each minute
stats = grouped.describe(percentiles=[.25, .5, .75])

# Create boxplot
plt.figure(figsize=(8, 6))
plt.boxplot([group for _, group in grouped], labels=grouped.groups.keys(), showmeans=True)

# Set plot labels and title
plt.xlabel('Minute')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Boxplot for Each Minute')

# Show plot
plt.show()
