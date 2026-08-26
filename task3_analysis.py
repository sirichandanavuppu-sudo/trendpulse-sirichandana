# TrendPulse - Task 3: Analyse the cleaned data

import pandas as pd
import numpy as np
from datetime import datetime


# Find today's cleaned CSV
date_string = datetime.now().strftime("%Y%m%d")
input_file = f"data/trends_{date_string}.csv"


# Load the cleaned CSV
df = pd.read_csv(input_file)


print("========== TREND PULSE ANALYSIS ==========\n")

# Basic information
print("Total stories:", len(df))
print("Total categories:", df["category"].nunique())

print("\nStories by category:")
print(df["category"].value_counts())


# Average score by category
average_score = df.groupby("category")["score"].mean()

print("\nAverage score by category:")
print(average_score.round(2))


# Average comments by category
average_comments = df.groupby("category")["num_comments"].mean()

print("\nAverage comments by category:")
print(average_comments.round(2))


# Total scores by category
total_score = df.groupby("category")["score"].sum()

print("\nTotal score by category:")
print(total_score)


# Find the highest-scoring story
highest_score_index = df["score"].idxmax()
highest_score_story = df.loc[highest_score_index]

print("\nHighest-scoring story:")
print("Title:", highest_score_story["title"])
print("Category:", highest_score_story["category"])
print("Score:", highest_score_story["score"])


# Find the most-commented story
highest_comments_index = df["num_comments"].idxmax()
highest_comments_story = df.loc[highest_comments_index]

print("\nMost-commented story:")
print("Title:", highest_comments_story["title"])
print("Category:", highest_comments_story["category"])
print("Comments:", highest_comments_story["num_comments"])


# NumPy calculations
scores = df["score"].to_numpy()

print("\nNumPy statistics:")
print("Maximum score:", np.max(scores))
print("Minimum score:", np.min(scores))
print("Mean score:", round(np.mean(scores), 2))
print("Median score:", np.median(scores))


print("\n========== ANALYSIS COMPLETE ==========")
