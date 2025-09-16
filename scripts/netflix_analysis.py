"""
Netflix Data Visualization Project
Author: Your Name
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def main():
    """Main function to run the analysis."""
    print("Netflix Data Analysis Started")

    # Load the dataset
    data_path = os.path.join("data", "netflix_titles.csv")
    if not os.path.exists(data_path):
        print(f"Error: Dataset not found at {data_path}")
        print("Please download the dataset from https://www.kaggle.com/datasets/shivamb/netflix-shows and place it in the 'data' directory.")
        return

    df = pd.read_csv(data_path)

    # --- Data Cleaning and Preprocessing ---
    df['date_added'] = df['date_added'].str.strip()
    df['date_added'] = pd.to_datetime(df['date_added'])
    df['year_added'] = df['date_added'].dt.year
    df['month_added'] = df['date_added'].dt.month

    # --- Analysis and Visualizations ---

    # 1. Content Type Distribution
    plt.figure(figsize=(8, 6))
    sns.countplot(x='type', data=df, palette='pastel')
    plt.title('Distribution of Content Types')
    plt.xlabel('Type (Movie/TV Show)')
    plt.ylabel('Count')
    plt.savefig('images/content_type_distribution.png')
    print("Generated images/content_type_distribution.png")

    # 2. Content Added Over the Years
    plt.figure(figsize=(12, 6))
    df.groupby('year_added')['show_id'].count().plot(kind='line')
    plt.title('Content Added Over the Years')
    plt.xlabel('Year Added')
    plt.ylabel('Number of Titles Added')
    plt.savefig('images/content_added_over_years.png')
    print("Generated images/content_added_over_years.png")

    # 3. Top 10 Countries with Most Content
    plt.figure(figsize=(12, 6))
    top_countries = df['country'].value_counts().nlargest(10)
    sns.barplot(x=top_countries.index, y=top_countries.values, palette='viridis')
    plt.title('Top 10 Countries with Most Content')
    plt.xlabel('Country')
    plt.ylabel('Number of Titles')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('images/top_10_countries.png')
    print("Generated images/top_10_countries.png")

    print("Analysis complete!")

if __name__ == "__main__":
    main()
