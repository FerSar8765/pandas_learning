import pandas as pd

# Create a DataFrame
data = {
    'ISP': ['ISP1', 'ISP2', 'ISP3'],
    'Download_Speed': [50, 70, 30],
    'Upload_Speed': [10, 20, 5]
}

df = pd.DataFrame(data)

# Apply function
df['Download_Speed'] = df['Download_Speed'].apply(lambda x: x ** 2)
print(df)