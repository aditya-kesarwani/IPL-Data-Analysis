import pandas as pd 
import matplotlib.pyplot as plt

# Cleaned dataset read 
df = pd.read_csv("cleaned_ipl_dataset.csv")

# Create figure size
plt.figure(figsize=(12,6))

# Bar chart 
plt.bar(df["Player"], df["Runs"])

# Chart title and labels 
plt.title("IPL Player Runs Analysis")

# X label 
plt.xlabel("Player")

# Y label
plt.ylabel("Runs")

# Rotate player name
plt.xticks(rotation=45)

# Adjust layout automatically 
plt.tight_layout()

# Show graph
plt.show()