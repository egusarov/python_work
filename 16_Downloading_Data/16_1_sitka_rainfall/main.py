from pathlib import Path
from datetime import datetime

import csv
import matplotlib.pyplot as plt


path = Path('C:\DEV\python_work\weather_data\sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract dates and daily rainfall amounts (PRCP)
dates, prcps = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        prcp = float(row[5])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        prcps.append(prcp)

# Plot the PRCP
plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(dates, prcps, color='blue')

# Format plot
title = "Daily Precipitation, 2021 (Sitka, US)"
ax.set_title(title, fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Precipitation Amount (in)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()