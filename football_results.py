import pandas as pd

pd.set_option('display.max_rows', 500)

df = pd.read_csv("results.csv")

# print(df)
# print(df.head())

# df.info()

# print(df["home_score"].value_counts())

# print(df["home_score"] < 7)

# mask = df["home_score"] < 7
# masked_df = df[mask]
# print(masked_df["home_score"].mean())

# print(df[df["home_score"] < 5]["home_score"].mean())

# print(df[df["home_score"] < 5])





# ........................................ Activity 1 Week5Day2 ..................................................
# 1 - How many different kinds of tournaments were played? = 147
# print(len(df["tournament"].unique()))

# 2 - How many matches were played under each tournament?
# print(df["tournament"].value_counts())

# 3 - The most reported home team and away team?
# print(df["home_team"].mode()[0])
# print(df["away_team"].mode()[0])

# 4 - The least reported home team and away team?
# print(df["home_team"].value_counts().nsmallest(1))
# print(df["away_team"].value_counts().nsmallest(1))


# ................................... Activity 2 Week5Day2 ..................................................
# 1 - How many times England played at home in each tournament?
# england_home_matches = df[df['home_team'] == 'England']
# print(england_home_matches["tournament"].value_counts().sum())

# england_away_matches = df[df['away_team'] == 'England']
# print(england_away_matches["tournament"].value_counts().sum())


# My study on England's avg score in all matches either at home or away...............................................
# mask = (df['away_team'] == 'England') | (df['home_team'] == 'England')
# england_total_matches = df[mask] 
# england_total_scores = england_total_matches['home_score'].sum() + england_total_matches['away_score'].sum()
# print(england_total_scores)

# england_total_matches_number = (england_total_matches['home_score'].value_counts().sum()) + (england_total_matches['away_score'].value_counts().sum())
# print(england_total_matches_number)

# england_total_matches_avg = england_total_scores / england_total_matches_number
# print(england_total_matches_avg)
#....................................................................................................................


# 2 - How many times England scored more than average amount of goals at a home match?
# mask = df['home_team'] == 'England'
# england_home_matches_df = df[mask]
# avg_England_home_score = england_home_matches_df["home_score"].mean()
# new_mask = england_home_matches_df["home_score"] > avg_England_home_score
# england_more_than_average_home_score_df = england_home_matches_df[new_mask]
# print(england_more_than_average_home_score_df["home_score"].value_counts().sum())


# 3 - How many times England scored more than the average amount of goals at an away match? similar to 2
# mask = df['away_team'] == 'England'
# england_away_matches_df = df[mask]
# avg_England_away_score = england_away_matches_df["away_score"].mean()
# new_mask = england_away_matches_df["away_score"] > avg_England_away_score
# england_more_than_average_away_score_df = england_away_matches_df[new_mask]
# print(england_more_than_average_away_score_df["away_score"].value_counts().sum())

# 4 - What is England's average amount of goals scored at home?
# england_home_matches = df[df['home_team'] == 'England']
# average_goals_england_home = england_home_matches['home_score'].mean()
# print(average_goals_england_home)

# 5 - What is each team's average home score and away score?

# average_home_scores = df.groupby('home_team')['home_score'].mean()
# print(average_home_scores)
# print(average_home_scores.loc["England"])


#  My search result:
# Calculate each team's average home score
# average_home_scores = df.groupby('home_team')['home_score'].mean().reset_index()
# average_home_scores.columns = ['team', 'average_home_score']


# Calculate each team's average away score
# average_away_scores = df.groupby('away_team')['away_score'].mean().reset_index()
# average_away_scores.columns = ['team', 'average_away_score']

# Merge the two results into a single dataframe
# team_average_scores = pd.merge(average_home_scores, average_away_scores, on='team', how='outer')

# Display the result
# print(team_average_scores)

# ................................... Stretch Week5Day2 ..................................
# mask = (df["home_team"] == "Iceland") & (df["away_team"] == "England")
# masked_df = df[mask]
# print(masked_df)

# Filter the data for matches where Iceland is the home team and England is the away team
iceland_england_matches = df[(df['home_team'] == 'Iceland') & (df['away_team'] == 'England')]

# Calculate the average goals scored by Iceland and England in these matches
average_iceland_home_score = iceland_england_matches['home_score'].mean()
average_england_away_score = iceland_england_matches['away_score'].mean()

# Display the match results and the average scores
print(iceland_england_matches)
print(f"Average goals scored by Iceland at home: {average_iceland_home_score}")
print(f"Average goals scored by England away: {average_england_away_score}")



