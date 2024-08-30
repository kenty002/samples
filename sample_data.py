import csv
from datetime import datetime, timedelta
import random

# Set start time and duration
start_time = datetime(2023, 7, 26, 16, 15, 0)  # Starting at 2023-07-26 16:15:00
end_time = start_time + timedelta(minutes=2)   # End time is 2 minutes after start

# Generate data
data = []
current_time = start_time

while current_time < end_time:
    # Generate random temperature between 40 and 60 degrees
    temp = random.uniform(40, 60)
    # Append time and temperature to the data list
    data.append([current_time.strftime("%Y-%m-%d %H:%M:%S"), round(temp, 2)])
    # Increment time by one second
    current_time += timedelta(seconds=1)

# Write data to CSV file
with open('temperature_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['time', 'temp'])
    writer.writerows(data)

print("CSV file 'temperature_data.csv' created successfully.")
