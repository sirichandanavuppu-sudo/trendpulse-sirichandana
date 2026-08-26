# TrendPulse - Task 1: Fetch data from HackerNews API

import requests
import json
import os
import time
from datetime import datetime

# HackerNews API URL for top stories
top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"

# Required User-Agent header
headers = {"User-Agent": "TrendPulse/1.0"}

# Keywords used to categorize stories
categories = {
    "technology": [
        "AI", "software", "tech", "code", "computer",
        "data", "cloud", "API", "GPU", "LLM"
    ],
    "worldnews": [
        "war", "government", "country", "president",
        "election", "climate", "attack", "global"
    ],
    "sports": [
        "NFL", "NBA", "FIFA", "sport", "game", "team",
        "player", "league", "championship"
    ],
    "science": [
        "research", "study", "space", "physics", "biology",
        "discovery", "NASA", "genome"
    ],
    "entertainment": [
        "movie", "film", "music", "Netflix", "game", "book",
        "show", "award", "streaming"
    ]
}

# Fetch the list of top story IDs
try:
    response = requests.get(top_stories_url, headers=headers)

    if response.status_code != 200:
        print("Failed to fetch top story IDs:", response.status_code)
        exit()

    story_ids = response.json()[:500]

except requests.RequestException as error:
    print("Error fetching top story IDs:", error)
    exit()


# Store collected stories
collected_stories = []

# Keep track of how many stories were collected per category
category_counts = {
    category: 0 for category in categories
}


# Process each category
for category, keywords in categories.items():

    for story_id in story_ids:

        # Stop when we have 25 stories for this category
        if category_counts[category] >= 25:
            break

        story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"

        try:
            story_response = requests.get(
                story_url,
                headers=headers
            )

            if story_response.status_code != 200:
                print(
                    f"Failed to fetch story {story_id}: "
                    f"{story_response.status_code}"
                )
                continue

            story = story_response.json()

            # Some HackerNews items may not have a title
            title = story.get("title", "")

            # Convert title to lowercase for case-insensitive matching
            title_lower = title.lower()

            # Check whether any category keyword appears in the title
            matched = False

            for keyword in keywords:
                if keyword.lower() in title_lower:
                    matched = True
                    break

            if not matched:
                continue

            # Create the required output record
            story_data = {
                "post_id": story.get("id"),
                "title": title,
                "category": category,
                "score": story.get("score", 0),
                "num_comments": story.get("descendants", 0),
                "author": story.get("by", ""),
                "collected_at": datetime.now().isoformat()
            }

            collected_stories.append(story_data)

            category_counts[category] += 1

        except requests.RequestException as error:
            print(f"Failed to fetch story {story_id}: {error}")
            continue

    # Wait 2 seconds before moving to the next category
    time.sleep(2)


# Create data folder if it doesn't exist
os.makedirs("data", exist_ok=True)

# Create today's filename
date_string = datetime.now().strftime("%Y%m%d")

output_file = f"data/trends_{date_string}.json"


# Save collected stories to JSON
with open(output_file, "w", encoding="utf-8") as file:
    json.dump(collected_stories, file, indent=4)


# Print results
print(f"Collected {len(collected_stories)} stories.")
print(f"Saved to {output_file}")

print("\nStories per category:")
for category, count in category_counts.items():
    print(f"{category}: {count}")
