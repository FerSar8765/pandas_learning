import pandas as pd

df = pd.read_excel("cleaning_activity.xlsx")

# print(df)
# print(df.info())
# print(df.describe())

df = df.set_index("Transaction ID")

df = df.drop(columns = ["Till ID"])

df = df.dropna(how = "any")

# print(df[df.duplicated()])

df = df.drop_duplicates()

df.at[56.0, "Cost"] = 6.0

df = df.drop([60.0])

def split_basket(contents: str):
  items = contents[1:-1].split(',')
  stripped_items = [item.strip() for item in items]
  return stripped_items

df["Basket"] = df["Basket"].apply(split_basket)
# print(df["Basket"])

exploded_data = df.explode("Basket", ignore_index=False)
# print(exploded_data["Basket"])

# print(df)

# print(df["Basket"])

text = " Tea" ," Coffee "," Water "," Milk " # with [] or without it, text is a list.
print(text[-1]) # output:  Milk with 2 white spaces around it _Milk_ ( where _ : white space)


items = "Tea , Coffee , water , Milk".split(",") # output : ['Tea ', ' Coffee ', ' water ', ' Milk']
print(items)
print(items[-1])
