import pandas as pd
import datetime
import random

# Define the start and end date for the year 2021
start_date = datetime.datetime(2021, 1, 1, 0, 0)
end_date = datetime.datetime(2021, 12, 31, 23, 55)  # Ending at 23:55

# Create a list of date-time values for every 5 minutes in the year
date_range = pd.date_range(start=start_date, end=end_date, freq='5T')

# Generate random GHI values for each date-time
ghis = [random.randint(0, 1000) for _ in range(len(date_range))]

# Create a DataFrame
df = pd.DataFrame({'mm:dd:yyyy hh:mm': date_range.strftime('%m:%d:%Y %H:%M'), 'ghi': ghis})

# Save the DataFrame to a CSV file without headers
df.to_csv('solar_ghi_2021_5min_mmddyyyy_hhmm.csv', index=True, header=True)

# Load the CSV file into a DataFrame
df = pd.read_csv('solar_ghi_2021_5min_mmddyyyy_hhmm.csv')

# Print the first few rows of the DataFrame
print(df.head())
