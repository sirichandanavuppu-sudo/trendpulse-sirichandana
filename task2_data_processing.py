# TrendPulse - Task 2: Clean the Data & Save as CSV

import pandas as pd
import glob
import os


# ---------------------------------------------------------
# STEP 1: Find and load the JSON file from the data folder
# ---------------------------------------------------------

json_files = glob.glob("data/trends_*.json")

if not json_files:
    print("Error: No trends JSON file found in the data folder.")
    exit()

# Use the latest trends JSON file
input_file = max(json_files, key=os.path.getmtime)

# Load JSON into Pandas DataFrame
df = pd.read_json(input_file)

print(f"Loaded {len(df)} stories from {input_file}")


# ---------------------------------------------------------
# STEP 2: Remove duplicate stories
# ---------------------------------------------------------

# Remove rows having the same post_id
df = df.drop_duplicates(subset="post_id")

print(f"\nAfter removing duplicates: {len(df)}")


# ---------------------------------------------------------
# STEP 3: Handle missing values
# ---------------------------------------------------------

# Strip extra spaces from title
df["title"] = df["title"].str.strip()

# Convert score to numeric
df["score"] = pd.to_numeric(df["score"], errors="coerce")

# Convert num_comments to numeric
df["num_comments"] = pd.to_numeric(
    df["num_comments"],
    errors="coerce"
)

# Drop rows where post_id, title, or score is missing
df = df.dropna(
    subset=["post_id", "title", "score"]
)

print(f"After removing nulls: {len(df)}")


# ---------------------------------------------------------
# STEP 4: Convert data types
# ---------------------------------------------------------

# Convert score to integer
df["score"] = df["score"].astype(int)

# num_comments should also be an integer.
# Missing comment counts are treated as 0.
df["num_comments"] = df["num_comments"].fillna(0).astype(int)


# ---------------------------------------------------------
# STEP 5: Remove low-quality stories
# ---------------------------------------------------------

# Remove stories where score is less than 5
df = df[df["score"] >= 5]

print(f"After removing low scores: {len(df)}")


# ---------------------------------------------------------
# STEP 6: Save cleaned data as CSV
# ---------------------------------------------------------

output_file = "data/trends_clean.csv"

df.to_csv(
    output_file,
    index=False
)

print(f"\nSaved {len(df)} rows to {output_file}")


# ---------------------------------------------------------
# STEP 7: Print stories per category
# ---------------------------------------------------------

print("\nStories per category:")

category_counts = df["category"].value_counts()

for category, count in category_counts.items():
    print(f"  {category:<15} {count}")