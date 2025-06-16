
# Netflix Dataset Exploration Project
# Goal: Analyze Netflix Movies and TV Shows dataset to extract insights.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Load Dataset
df = pd.read_csv("netflix_titles.csv")


# Preview Data
print("Data Sample:")
print(df.head())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Clean Data: Fill missing values in 'country', 'cast', 'director' as "Unknown"
df['country'].fillna("Unknown", inplace=True)
df['cast'].fillna("Unknown", inplace=True)
df['director'].fillna("Unknown", inplace=True)
df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors='coerce')
df['year_added'] = df['date_added'].dt.year

# Content type count
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='type', palette='Set2')
plt.title('Movies vs TV Shows')
plt.savefig("content_type.png")
plt.show()

# Top 10 countries producing Netflix content
top_countries = df['country'].value_counts().head(10)
print(top_countries)
top_countries.plot(kind='bar', title='Top 10 Content Producing Countries', color='teal')
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_countries.png")
plt.show()


# Most common genres
df['listed_in'] = df['listed_in'].astype(str)
genres = df['listed_in'].str.split(', ').explode()
top_genres = genres.value_counts().head(10)

plt.figure(figsize=(8,4))
sns.barplot(x=top_genres.values, y=top_genres.index, palette='mako')
plt.title('Top 10 Genres on Netflix')
plt.xlabel('Number of Titles')
plt.tight_layout()
plt.savefig("top_genres.png")
plt.show()

# Number of new titles added per year
added_per_year = df['year_added'].value_counts().sort_index()
added_per_year.plot(kind='line', marker='o', title='Netflix Content Added Per Year')
plt.ylabel("Number of Titles")
plt.grid(True)
plt.savefig("content_per_year.png")
plt.show()

# Summary
print("\nKey Insights:")
print(f"Total Titles: {len(df)}")
print(f"Number of Movies: {len(df[df['type'] == 'Movie'])}")
print(f"Number of TV Shows: {len(df[df['type'] == 'TV Show'])}")
print(f"Most Common Country: {df['country'].value_counts().idxmax()}")
print(f"Most Popular Genre: {top_genres.idxmax()}")
