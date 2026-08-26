# TrendPulse - Task 4: Visualize the trends

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


# Find today's cleaned CSV
date_string = datetime.now().strftime("%Y%m%d")
input_file = f"data/trends_{date_string}.csv"


# Load the cleaned data
df = pd.read_csv(input_file)


# -------------------------------
# 1. Number of stories by category
# -------------------------------

category_counts = df["category"].value_counts()

plt.figure(figsize=(10, 6))
category_counts.plot(kind="bar")

plt.title("Number of Trending Stories by Category")
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()


# -------------------------------
# 2. Average score by category
# -------------------------------

average_score = df.groupby("category")["score"].mean()

plt.figure(figsize=(10, 6))
average_score.plot(kind="bar")

plt.title("Average Story Score by Category")
plt.xlabel("Category")
plt.ylabel("Average Score")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()


# -------------------------------
# 3. Average comments by category
# -------------------------------

average_comments = df.groupby("category")["num_comments"].mean()

plt.figure(figsize=(10, 6))
average_comments.plot(kind="bar")

plt.title("Average Comments by Category")
plt.xlabel("Category")
plt.ylabel("Average Comments")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()


# -------------------------------
# 4. Score distribution
# -------------------------------

plt.figure(figsize=(10, 6))
plt.hist(df["score"], bins=20)

plt.title("Distribution of Story Scores")
plt.xlabel("Score")
plt.ylabel("Number of Stories")

plt.tight_layout()
plt.show()


print("Visualization complete.")
