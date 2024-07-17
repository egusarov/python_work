from pathlib import Path
from datetime import datetime

import csv
import matplotlib.pyplot as plt


path = Path('C:\DEV\python_work\weather_data\odesa_2023_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

date_index = header_row.index('DATE')
high_index = header_row.index('TMAX')
low_index = header_row.index('TMIN')
name_index = header_row.index('NAME')

# Extract dates, and high and low temperatures
dates, highs, lows = [], [], []
place_name = ""
for row in reader:
    # Grab the station name, if it's not already set
    if not place_name:
        place_name = row[name_index]

    current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
    try:
        high = float(row[high_index])
        low = float(row[low_index])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plot the high and low temperatures
plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
title = f"Daily High and Low Temperatures, 2023\n{place_name}"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (C)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()