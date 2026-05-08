import pandas as pd

# CSV file read
df = pd.read_csv("ipl_dataset.csv")

# Original dataset print
print("Original Dataset:\n")
print(df)

# Missing values check 
print("\nMissing Values:\n")
print(df.isnull().sum())

# Fill missing values in Runs column with average 
df["Wickets"].fillna(df["Wickets"].mean(), inplace = True )

# Fill missing values in Matches column with average 
df["Matches"].fillna(df["Matches"].mean(), inplace = True)

# Print cleaned datasets 
average_runs = df["Runs"].mean()
print("\nAverage Runs:", average_runs )

# Saved cleaned dataset
df.to_csv("cleaned_ipl_dataset.csv ", index = False)

print("\nCleaned dataset saved successfully!")