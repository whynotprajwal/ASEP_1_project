import pandas as pd
import sqlite3

conn = sqlite3.connect("voiceup.db")

# Load issues table to Pandas
issues_df = pd.read_sql_query("SELECT * FROM issues", conn)

# Example: Filter issues by status
open_issues = issues_df[issues_df['status'] == 'Open']

# Example: Count issues per category
category_summary = issues_df.groupby('category_id').size()

print("Open Issues:\n", open_issues)
print("Issues per Category:\n", category_summary)
