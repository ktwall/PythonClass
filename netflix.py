import pandas as pd 

df = pd.read_csv('netflix daily top 10.csv')

df.drop(columns=['Viewership Score', 'Netflix Release Date', 'Last Week Rank', 'Year to Date Rank', 'Netflix Exclusive'], inplace=True)

df = df[(df['As of'] >= '2020-07-01') & (df['As of'] < '2020-07-31')]

# mask = df['Type'] == 'Movie'

mask = df['Type'] == 'TV Show'

df = df[mask]

df.to_csv(r'C:Users\Desktop\Top 10 Shows July.csv')

print(df)