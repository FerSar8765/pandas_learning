import pandas as pd

# languages = pd.Series(["Python", "JavaScript", "HTML", "SQL"])

# rankings = pd.Series([3 , 1 , 2 , 4])

# df = pd.DataFrame({
#     "Languages" : languages,
#     "Rankings" : rankings
# })

# df = pd.concat([languages , rankings], axis = 1)
# df.columns = ["Languages","Rankings"]

# print(df)

# df = pd.DataFrame([("Anne" , 30) , ("Bill" , 27) , ("Charlie" , 55)], columns = ["Name","Age"])
# print(df)

# df = pd.read_csv("speeds.csv")
# print(df)

# df = pd.read_excel("speeds.xlsx")
# print(df)


# Define the data for the planets
planet_data = {
    'Name': ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'],
    'Average Temperature (°C)': [167, 464, 15, -65, -110, -140, -195, -200],
    'Radius (km)': [2439.7, 6051.8, 6371, 3389.5, 69911, 58232, 25362, 24622],
    'Colour': ['Gray', 'Yellow', 'Blue', 'Red', 'Brown/White', 'Yellow/Gold', 'Blue/Green', 'Blue'],
    'Interesting Feature': [
        'Closest planet to the Sun',
        'Hottest planet due to thick atmosphere',
        'Only planet known to support life',
        'Home to the largest volcano in the solar system (Olympus Mons)',
        'Has a Great Red Spot, a giant storm larger than Earth',
        'Has the most extensive rings in the solar system',
        'Orbits the Sun on its side',
        'Strongest winds in the solar system'
    ]
}

# Create a pandas DataFrame
planet_df = pd.DataFrame(planet_data)

# # Display the DataFrame
# print(planet_df)

# planet_df.to_excel('planets_data.xlsx', index=False)  # index=False to avoid saving the DataFrame index as a column

# Add new columns to the DataFrame for discovery information and composition
planet_df['Discovered By'] = [
    'Known since ancient times', 'Known since ancient times', 'Known since ancient times', 
    'Known since ancient times', 'Known since ancient times', 'Known since ancient times', 
    'William Herschel', 'Johann Galle'
]

planet_df['Discovery Year'] = [
    'Prehistoric', 'Prehistoric', 'Prehistoric', 'Prehistoric', 'Prehistoric', 'Prehistoric', 
    1781, 1846
]

planet_df['Composition'] = [
    'Mostly iron and nickel', 
    'Carbon dioxide, nitrogen, sulfuric acid clouds', 
    'Nitrogen, oxygen, water vapor', 
    'Carbon dioxide, nitrogen', 
    'Hydrogen, helium', 
    'Hydrogen, helium', 
    'Hydrogen, helium, methane', 
    'Hydrogen, helium, methane'
]
# display the planet_df
# print(planet_df)

# Add Pluto data
pluto_data = pd.DataFrame({
    'Name': ['Pluto'],
    'Average Temperature (°C)': [-225],
    'Radius (km)': [1188.3],
    'Colour': ['Brown/Gray'],
    'Interesting Feature': ['Dwarf planet with a heart-shaped glacier'],
    'Discovered By': ['Clyde Tombaugh'],
    'Discovery Year': [1930],
    'Composition': ['Nitrogen, methane, carbon monoxide']
})

# # Add Pluto to the DataFrame
# planet_df = pd.concat([planet_df, pluto_data])

# Katy's method
# planet_df.loc[len(planet_df)] = [ 
# "Pluto", # Planet Name 
# "-229C", # Average Temp 
# "1188km", # Radius 
# "Brown", # Colour 
# "Dwarf Planet", # Notable Feature 
# "Clyde Tombaugh", # Discovered By 
# "1930", # Year Discovered 
# "Nitrogen, Methane" # Major Elements 
# ]

# Display the updated DataFrame
# print(planet_df)

# Activity 2 of Accessing Data
# planet_df = planet_df.set_index("Name")
# print(planet_df.loc["Venus":"Jupiter" , :"Composition"])

# # Activity 3 of Accessing Data
planet_changed_index_df = planet_df.set_index("Name")

# print("\nHere are the list of solar system planets: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto. ")
user_planet = input("\nPlease enter a planet name for accessing its information or type Quit to exit: ").capitalize()


# print("\nHere are the information we have: Average Temperature (°C), Radius (km), Colour, Interesting Feature, Discovered By, Discovery Year, Composition")



while user_planet != "Quit" and user_planet in planet_df["Name"].values:
        user_info_need = input("\nPlease type which information you wish to know. If you want to know all about this planet, please type all: ").capitalize()
        if user_info_need in planet_df.columns:
            print(f"The answer is {planet_changed_index_df.loc[user_planet , user_info_need]}")
            break
        elif user_info_need == "All":
            print(f"The answer is\n {planet_changed_index_df.loc[user_planet]}")
            break
        elif user_info_need not in planet_df.columns:
            print("Sorry! Our dataframe does not have the information you want!")
            # user_planet = input("\nPlease enter a planet name for accessing its information or type Quit to exit: ").capitalize()
            # user_info_need = input("\nPlease type which information you wish to know. If you want to now all about this planet, please type all: ").capitalize()

else:
     print("You either enter Quit or a wrong planet name!")       
           





