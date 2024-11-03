import pandas as pd

df = pd.read_excel("first_hour_sales.xlsx")

# print(df.info())
# print(df.describe())

df = df.set_index("Transaction ID")

df = df.drop(columns = ["Till ID"])

df = df.drop(columns = ["Unnamed: 0"])

df = df.dropna(how= "any")

# print(df[df.duplicated()])

df = df.drop_duplicates()

df.at[15.0 , "Cost"] = 6.00

def float_to_time(time_record):
    # convert float to a string
    time_record = str(time_record)
    # split the input string at the decimal point
    hours, minutes = time_record.split('.')
    # format the hours and minuets into HH:MM
    timestamp = f"{int(hours):02}:{int(minutes):02}"
    return timestamp
 

df["Time"] = df["Time"].apply(float_to_time)
# print(df)

df["Time"] = pd.to_datetime(df["Time"])
# print(df)

def split_basket(string):
    items = string.split(",")
    stripped_items = [item.strip() for item in items]
    return stripped_items

df["Basket"] = df["Basket"].apply(split_basket)
# print(df)

# exploded_data = df.explode("Basket", ignore_index=False)
# print(exploded_data["Basket"])

# ......... NOW DATA IS READY TO BE ANALYSED ...............

# 1. The average price of an item? 1.62
products = {
    "Items" : ["Tea" , "Americano" , "Latte" , "Cappuccino" , "Mocha" , "Hot Chocolate" , "Croissant" , "Muffin" , "Toast" , "Panini" , "Buttered Roll" , "Stroopwafel"],
    "Price" : [ 1.00 , 1.70 , 1.90 , 1.90 , 2.00 , 2.20 , 1.50 , 2.10 , 1.00 , 2.90 , 0.70 , 0.50]
}

products_df = pd.DataFrame(products)

print(products_df)

print(products_df["Price"].mean())

# 2. The average basket price 7.44
print(df["Cost"].mean())

# 3. The maximum spend in one transaction
print(df["Cost"].max())

# 4. The minimum spend in one transaction
print(df["Cost"].min())

# 5. The most common spend amount
print(df["Cost"].mode())

# 6. The most common payment type Debit
print(df["Payment Method"].mode())