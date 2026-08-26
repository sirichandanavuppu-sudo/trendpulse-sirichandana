# TrendPulse - Task 4: Visualizations

import pandas as pd
import matplotlib.pyplot as plt
import os


# STEP 1: Load the analysed data

input_file = "data/trends_analysed.csv"
df = pd.read_csv(input_file)

print(f"Loaded data: {df.shape}")

# Create outputs folder if it does not exist

os.makedirs("outputs", exist_ok=True)


# CHART 1: Top 10 Stories by Score

# Sort stories by score from highest to lowest
# and take the top 10

top_stories = df.sort_values(
    by="score",
    ascending=False
).head(10).copy()


# Shorten titles longer than 50 characters

top_stories["short_title"] = top_stories["title"].apply(
    lambda title: title[:50] + "..."
    if len(title) > 50
    else title
)


# Create horizontal bar chart

plt.figure(figsize=(10, 6))

plt.barh(
    top_stories["short_title"],
    top_stories["score"]
)

# Put highest score at the top

plt.gca().invert_yaxis()

plt.title("Top 10 Stories by Score")
plt.xlabel("Score")
plt.ylabel("Story Title")

plt.tight_layout()

# Save BEFORE show

plt.savefig(
    "outputs/chart1_top_stories.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

plt.close()


# CHART 2: Stories per Category

# Count how many stories belong to each category

category_counts = df["category"].value_counts()


# Create different colours for each bar

bar_colors = [
    "skyblue",
    "orange",
    "green",
    "red",
    "purple"
]


plt.figure(figsize=(9, 6))

plt.bar(
    category_counts.index,
    category_counts.values,
    color=bar_colors[:len(category_counts)]
)

plt.title("Number of Stories per Category")
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.xticks(rotation=20)
plt.tight_layout()

# Save BEFORE show

plt.savefig(
    "outputs/chart2_categories.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

plt.close()


# CHART 3: Score vs Comments

plt.figure(figsize=(10, 6))


# Separate popular and non-popular stories

popular = df[df["is_popular"] == True]

not_popular = df[df["is_popular"] == False]


# Plot non-popular stories

plt.scatter(
    not_popular["score"],
    not_popular["num_comments"],
    label="Not Popular",
    alpha=0.7
)


# Plot popular stories

plt.scatter(
    popular["score"],
    popular["num_comments"],
    label="Popular",
    alpha=0.7
)


plt.title("Score vs Comments")
plt.xlabel("Score")
plt.ylabel("Number of Comments")

plt.legend()

plt.tight_layout()

# Save BEFORE show

plt.savefig(
    "outputs/chart3_scatter.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

plt.close()


# BONUS: TrendPulse Dashboard

fig, axes = plt.subplots(
    2,
    2,
    figsize=(16, 11)
)


# Dashboard Chart 1

axes[0, 0].barh(
    top_stories["short_title"],
    top_stories["score"]
)

axes[0, 0].invert_yaxis()

axes[0, 0].set_title("Top 10 Stories by Score")
axes[0, 0].set_xlabel("Score")
axes[0, 0].set_ylabel("Story Title")


# Dashboard Chart 2

axes[0, 1].bar(
    category_counts.index,
    category_counts.values,
    color=bar_colors[:len(category_counts)]
)

axes[0, 1].set_title("Stories per Category")
axes[0, 1].set_xlabel("Category")
axes[0, 1].set_ylabel("Number of Stories")

axes[0, 1].tick_params(axis="x", rotation=20)


# Dashboard Chart 3

axes[1, 0].scatter(
    not_popular["score"],
    not_popular["num_comments"],
    label="Not Popular",
    alpha=0.7
)

axes[1, 0].scatter(
    popular["score"],
    popular["num_comments"],
    label="Popular",
    alpha=0.7
)

axes[1, 0].set_title("Score vs Comments")
axes[1, 0].set_xlabel("Score")
axes[1, 0].set_ylabel("Number of Comments")
axes[1, 0].legend()


# Remove unused fourth subplot

axes[1, 1].axis("off")

# Overall dashboard title

fig.suptitle(
    "TrendPulse Dashboard",
    fontsize=20
)

plt.tight_layout()

# Save dashboard

plt.savefig(
    "outputs/dashboard.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()
plt.close()


# FINAL MESSAGE

print("\n-----------------------------------")
print("TrendPulse - Task 4 Complete")
print("-----------------------------------")

print("Created:")
print("outputs/chart1_top_stories.png")
print("outputs/chart2_categories.png")
print("outputs/chart3_scatter.png")
print("outputs/dashboard.png")