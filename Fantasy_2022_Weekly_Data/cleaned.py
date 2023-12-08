import pandas as pd
import glob

# Pattern to match all quarterback CSV files
pattern = 'Fantasy_2022_Weekly_Data/FantasyPros_Fantasy_Football_Statistics_QB*.csv'
qb_files = glob.glob(pattern)

# List to hold dataframes
df_list = []

# Loop through all matching files
for file in qb_files:
    # Read the CSV file
    df = pd.read_csv(file, usecols=["Player", "FPTS", "ROST"])
    # Append the dataframe to the list
    df_list.append(df)

# Concatenate all dataframes into one
qb_df = pd.concat(df_list, ignore_index=True)

# Display the resulting dataframe
print(qb_df)