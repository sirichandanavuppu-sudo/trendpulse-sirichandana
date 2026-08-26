TrendPulse — What's Actually Trending Right Now

TrendPulse is a small Python data pipeline that collects trending stories, cleans the raw data, performs analysis with Pandas and NumPy, and creates visualizations with Matplotlib.

Project Pipeline

Collect → Clean → Analyse → Visualise

Task 1 — Data Collection

task1_data_collection.py

Collects trending story data.

Saves the raw data as a dated JSON file inside data/.

Example output:

data/trends_20260826.json

Task 2 — Data Processing

task2_data_processing.py

Loads the raw JSON file with Pandas and cleans the data.

Cleaning includes:

Removing duplicate post_id values

Removing rows with missing post_id, title, or score

Converting score and num_comments to integers

Removing stories with a score below 5

Stripping extra whitespace from titles

Printing stories per category

Output:

data/trends_clean.csv

Task 3 — Analysis

task3_analysis.py

Uses Pandas and NumPy to analyse the cleaned data.

The script calculates:

Average score

Average number of comments

Mean score

Median score

Standard deviation

Maximum score

Minimum score

Category with the most stories

Most-commented story

It also creates two new columns:

engagement = num_comments / (score + 1)
is_popular = score > average score

Output:

data/trends_analysed.csv

Task 4 — Visualisation

task4_visualization.py

Uses Matplotlib to create three charts:

Top 10 stories by score — horizontal bar chart

Stories per category — bar chart

Score vs comments — scatter plot, separated by popularity

The script also creates a combined dashboard.

Output files:

outputs/
├── chart1_top_stories.png
├── chart2_categories.png
├── chart3_scatter.png
└── dashboard.png

Project Structure

trendpulse-sirichandana/
│
├── data/
│   ├── trends_20260826.json
│   ├── trends_clean.csv
│   └── trends_analysed.csv
│
├── outputs/
│   ├── chart1_top_stories.png
│   ├── chart2_categories.png
│   ├── chart3_scatter.png
│   └── dashboard.png
│
├── task1_data_collection.py
├── task2_data_processing.py
├── task3_analysis.py
├── task4_visualization.py
└── README.md

Technologies Used

Python

Pandas

NumPy

Matplotlib

JSON

Git & GitHub

How to Run

Run the scripts in order:

python task1_data_collection.py
python task2_data_processing.py
python task3_analysis.py
python task4_visualization.py

Each task produces the data or visual output required by the next stage.

Final Result

The project demonstrates a complete basic data-analysis workflow:

Raw trending data
        ↓
JSON
        ↓
Pandas cleaning
        ↓
Clean CSV
        ↓
Pandas + NumPy analysis
        ↓
Analysed CSV
        ↓
Matplotlib visualisations
        ↓
TrendPulse Dashboard