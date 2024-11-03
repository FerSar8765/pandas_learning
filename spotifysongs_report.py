import pandas as pd

# pd.set_option('display.max_rows', None)

df = pd.read_csv("spotify_songs.csv")

# print(df.shape)
# print(df.columns)
# print(df.head())

# print(df["playlist_genre"].value_counts())
# print(df["playlist_genre"].mode()[0])

# print(df["duration_ms"].median())
# print(df["duration_ms"].mean())

# max_duration = df["duration_ms"].max()
# min_duration = df["duration_ms"].min()
# print(max_duration-min_duration)

# print(df["duration_ms"].sum())

# print(df.sort_values(by=["duration_ms"], ascending=False))

# print(df.sort_values(by=["track_name"]))

# print(df.groupby("playlist_genre")["duration_ms"].min())

# print(df.query("track_artist=='Ricky Martin'"))

# mean_value = df["duration_ms"].mean()

# print(df.query("duration_ms> @mean_value"))