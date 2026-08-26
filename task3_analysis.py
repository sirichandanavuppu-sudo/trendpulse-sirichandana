# TrendPulse - Task 3: Analysis with Pandas & NumPy

import pandas as pd
import numpy as np
# STEP 1: Load the cleaned CSV

input_file = "data/trends_clean.csv"
df = pd.read_csv(input_file)
print(f"Loaded data: {df.shape}")

# STEP 2: Explore the data
print("\nFirst 5 rows:")
print(df.head())
print("\nShape of DataFrame:")
print(df.shape)


# Calculate average score and average comments

average_score = df["score"].mean()
average_comments = df["num_comments"].mean()

print(f"\nAverage score   : {average_score:.2f}")
print(f"Average comments: {average_comments:.2f}")


# STEP 3: NumPy statistics
# Convert score column to NumPy array

scores = df["score"].to_numpy()


# Mean
mean_score = np.mean(scores)


# Median
median_score = np.median(scores)


# Standard deviation
std_score = np.std(scores)


# Highest score
highest_score = np.max(scores)


# Lowest score
lowest_score = np.min(scores)


print("\n--- NumPy Stats ---")
print(f"Mean score   : {mean_score:.2f}")
print(f"Median score : {median_score:.2f}")
print(f"Std deviation: {std_score:.2f}")
print(f"Max score    : {highest_score}")
print(f"Min score    : {lowest_score}")


# STEP 4: Find category with the most stories

category_counts = df["category"].value_counts()

most_common_category = category_counts.idxmax()
most_common_count = category_counts.max()

print(
    f"\nMost stories in: "
    f"{most_common_category} "
    f"({most_common_count} stories)"
)

# STEP 5: Find the story with the most comments

most_commented_index = df["num_comments"].idxmax()

most_commented_story = df.loc[
    most_commented_index,
    "title"
]

most_comments = df.loc[
    most_commented_index,
    "num_comments"
]

print(
    f'\nMost commented story: '
    f'"{most_commented_story}" '
    f'— {most_comments} comments'
)


# STEP 6: Add engagement column

df["engagement"] = (
    df["num_comments"] / (df["score"] + 1)
)

# STEP 7: Add is_popular column

df["is_popular"] = (
    df["score"] > average_score
)

# STEP 8: Save analysed data

output_file = "data/trends_analysed.csv"

df.to_csv(
    output_file,
    index=False
)

print(f"\nSaved to {output_file}")