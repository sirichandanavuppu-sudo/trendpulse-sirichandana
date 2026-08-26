# TrendPulse - Task 2: Process and clean the collected data

import json
import pandas as pd
import os
from datetime import datetime


# Find today's JSON file
date_string = datetime.now().strftime("%Y%m%d")
input_file = f"data/trends_{date_string}.json"

# Output CSV file
output_file = f"data/trends_{date_string}.csv"


# Load JSON data
with open(input_file, "r", encoding="utf-8") as file:
    data = json.load(file)


# Convert JSON data into a DataFrame
df = pd.DataFrame(data)


# Remove duplicate stories
df = df.drop_duplicates(subset="post_id")


# Remove rows where title is missing
df = df.dropna(subset=["title"])


# Fill missing numeric values with 0
df["score"] = df["score"].fillna(0)
df["num_comments"] = df["num_comments"].fillna(0)


# Make sure numeric columns have the correct data type
df["score"] = pd.to_numeric(df["score"], errors="coerce").fillna(0)
df["num_comments"] = pd.to_numeric(
    df["num_comments"], errors="coerce"
).fillna(0)


# Remove leading/trailing spaces from titles
df["title"] = df["title"].str.strip()


# Save cleaned data as CSV
df.to_csv(output_file, index=False)


# Print summary
print(f"Processed {len(df)} stories.")
print(f"Saved cleaned data to {output_file}")
