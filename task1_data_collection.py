# TrendPulse - Task 1: Fetch data from HackerNews API

import requests
import json
import os
import time
from datetime import datetime


# HackerNews API URL for top stories
TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"

# Required User-Agent header
HEADERS = {
    "User-Agent": "TrendPulse/1.0"
}


# Keywords used to assign stories to categories
categories = {
    "technology": [
        "AI",
        "software",
        "tech",
        "code",
        "computer",
        "data",
        "cloud",
        "API",
        "GPU",
        "LLM",
        "programming",
        "developer",
        "developer tools",
        "machine learning",
        "artificial intelligence",
        "cybersecurity",
        "security",
        "open source",
        "database",
        "web",
        "internet",
        "linux",
        "python",
        "javascript",
        "startup"
    ],

    "worldnews": [
        "war",
        "government",
        "country",
        "president",
        "election",
        "climate",
        "attack",
        "global",
        "politics",
        "political",
        "minister",
        "parliament",
        "military",
        "conflict",
        "international",
        "world",
        "iran",
        "israel",
        "ukraine",
        "russia",
        "china",
        "europe",
        "america",
        "united states"
    ],

    "sports": [
        "NFL",
        "NBA",
        "FIFA",
        "sport",
        "sports",
        "game",
        "team",
        "player",
        "league",
        "championship",
        "football",
        "soccer",
        "baseball",
        "basketball",
        "tennis",
        "cricket",
        "athlete",
        "coach",
        "tournament",
        "olympics",
        "olympic",
        "match",
        "race",
        "racing",
        "golf",
        "boxing",
        "hockey",
        "formula 1",
        "F1",
        "marathon",
        "medal",
        "world cup"
    ],

    "science": [
        "research",
        "study",
        "space",
        "physics",
        "biology",
        "discovery",
        "NASA",
        "genome",
        "science",
        "scientist",
        "scientists",
        "quantum",
        "chemistry",
        "medical",
        "medicine",
        "health",
        "astronomy",
        "planet",
        "earth",
        "energy",
        "experiment",
        "laboratory",
        "laboratory",
        "lab",
        "microscope",
        "genetics",
        "neuroscience",
        "climate",
        "evolution",
        "biology",
        "molecule",
        "particle",
        "telescope",
        "satellite",
        "rocket",
        "mars",
        "moon"
    ],

    "entertainment": [
        "movie",
        "film",
        "music",
        "Netflix",
        "game",
        "book",
        "show",
        "award",
        "streaming",
        "TV",
        "television",
        "actor",
        "actress",
        "director",
        "cinema",
        "series",
        "album",
        "song",
        "concert",
        "video game",
        "gaming",
        "YouTube",
        "podcast",
        "comedy",
        "theater",
        "celebrity",
        "Disney",
        "Amazon Prime",
        "HBO"
    ]
}


# Keep track of collected stories
collected_stories = []

# Keep track of the number collected in each category
category_counts = {
    category: 0
    for category in categories
}


# ---------------------------------------------------------
# STEP 1: Fetch the first 500 top story IDs
# ---------------------------------------------------------

try:

    response = requests.get(
        TOP_STORIES_URL,
        headers=HEADERS,
        timeout=15
    )

    response.raise_for_status()

    story_ids = response.json()[:500]

    print(f"Fetched {len(story_ids)} story IDs.")

except requests.RequestException as error:

    print("Error fetching top story IDs:", error)

    exit()


# ---------------------------------------------------------
# STEP 2: Fetch each story only once
# ---------------------------------------------------------

for index, story_id in enumerate(story_ids, start=1):

    # Stop when all categories have 25 stories
    if all(
        count >= 25
        for count in category_counts.values()
    ):
        break

    # HackerNews API URL for individual story
    story_url = (
        f"https://hacker-news.firebaseio.com/v0/item/"
        f"{story_id}.json"
    )

    try:

        story_response = requests.get(
            story_url,
            headers=HEADERS,
            timeout=10
        )

        if story_response.status_code != 200:

            print(
                f"Failed to fetch story {story_id}: "
                f"{story_response.status_code}"
            )

            continue

        story = story_response.json()

    except requests.RequestException as error:

        print(
            f"Error fetching story {story_id}: "
            f"{error}"
        )

        continue


    # Get the title
    title = story.get("title", "")

    # Skip stories without a title
    if not title:
        continue


    # Convert title to lowercase
    # so keyword matching is case-insensitive
    title_lower = title.lower()


    # -----------------------------------------------------
    # Check which categories match the title
    # -----------------------------------------------------

    for category, keywords in categories.items():

        # Do not collect more than 25 for a category
        if category_counts[category] >= 25:
            continue

        matched = False

        for keyword in keywords:

            if keyword.lower() in title_lower:

                matched = True

                break


        # If no keyword matched, skip this category
        if not matched:
            continue


        # -------------------------------------------------
        # STEP 3: Extract required fields
        # -------------------------------------------------

        story_data = {

            "post_id": story.get("id"),

            "title": title,

            "category": category,

            "score": story.get("score", 0),

            "num_comments": story.get(
                "descendants",
                0
            ),

            "author": story.get(
                "by",
                ""
            ),

            "collected_at": datetime.now().isoformat()

        }


        # Add the story to the collection
        collected_stories.append(story_data)


        # Increase category count
        category_counts[category] += 1


        print(
            f"{category}: "
            f"{category_counts[category]}/25 - "
            f"{title[:70]}"
        )


    # Small delay between API requests
    time.sleep(0.1)


# ---------------------------------------------------------
# STEP 4: Wait 2 seconds after collection
# ---------------------------------------------------------

time.sleep(2)


# ---------------------------------------------------------
# STEP 5: Create data folder
# ---------------------------------------------------------

os.makedirs(
    "data",
    exist_ok=True
)


# ---------------------------------------------------------
# STEP 6: Create today's filename
# ---------------------------------------------------------

date_string = datetime.now().strftime(
    "%Y%m%d"
)

output_file = (
    f"data/trends_{date_string}.json"
)


# ---------------------------------------------------------
# STEP 7: Save stories to JSON
# ---------------------------------------------------------

with open(
    output_file,
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        collected_stories,
        file,
        indent=4,
        ensure_ascii=False
    )


# ---------------------------------------------------------
# STEP 8: Print final results
# ---------------------------------------------------------

print("\n-----------------------------------")

print(
    "TrendPulse - Task 1 Complete"
)

print("-----------------------------------")

print(
    f"Collected {len(collected_stories)} stories."
)

print(
    f"Saved to {output_file}"
)


print("\nStories per category:")

for category, count in category_counts.items():

    print(
        f"{category}: {count}"
    )


# ---------------------------------------------------------
# STEP 9: Check minimum requirement
# ---------------------------------------------------------

if len(collected_stories) >= 100:

    print(
        "\nMinimum requirement of "
        "100 stories reached."
    )

else:

    print(
        f"\nWarning: Only "
        f"{len(collected_stories)} stories "
        "matched the provided keywords "
        "within the first 500 stories."
    )

    print(
        "Some categories did not reach "
        "25 stories."
    )