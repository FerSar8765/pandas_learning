import pandas as pd

languages = pd.Series(["Python", "JavaScript", "HTML", "SQL"])
ranking = pd.Series([3,1,2,4])

df = pd.DataFrame({
    "Languages": languages,
    "Ranking": ranking
})

# Technique 1 - Adding a new row
# df.loc[4] = ["PHP", 11]
# df.loc[3.5] = ["KESL", 20]

# df = df.sort_index()
# print(df)

# df = df.reset_index()
# print(df)

# Technique 2 - Adding a new row
new_data = pd.DataFrame({
    "Languages" : ["PHP"],
    "Ranking" : [11]
})

df = pd.concat([df,new_data], ignore_index=True)

# Adding new rows
new_data_rows = pd.DataFrame({
    "Languages" : ["Java" , "TypeScript"],
    "Ranking" : [7 , 5]
})

df = pd.concat([df,new_data_rows], ignore_index=True)
# print(df)

#  Method 1 for adding new column
#  df["Ranking 2022"] = [4,1,2,3,10,6,5]
#  print(df)

#  Method 1 for adding new column
# new_data_column = pd.DataFrame({
#     "Ranking 2022" : [4,1,2,3,10,6,5]
# })

# df = pd.concat([df,new_data_column], axis=1)
#  print(df)

#  Technique 1 - Adding new columns
#  df["Ranking 2020"] = [4,1,2,3,8,5,9]
#  df["Ranking 2019"] = [4,1,2,3,8,5,10]

# Technique 2 - Adding new columns
new_data_columns = pd.DataFrame({
    "Ranking 2022": [4,1,2,3,10,6,5],
    "Ranking 2020": [4,1,2,3,8,5,9],
    "Ranking 2019": [4,1,2,3,8,5,10]
})

df = pd.concat([df,new_data_columns], axis=1)

# print(df)

# Adding a new column
df.insert(3, "Ranking 2021" , [3,1,2,4,11,5,7])
# print(df)

print(df.columns.get_loc("Ranking 2022"))