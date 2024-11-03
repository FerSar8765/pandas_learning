import matplotlib.pyplot as plt

# ........................... Classroom Example ...............................
# years = [2018 , 2019 , 2020 , 2021 , 2022 , 2023]
# python_position = [7 , 4 , 4 , 3 , 4 , 3]
# js_position = [1 , 1 , 1 , 1 , 1 , 1]
# sql_position = [4 , 3 , 3 , 4 , 3 ,4]
# typescript_position = [12 , 10 , 9 , 7 , 5 ,5]


# plt.plot(years , python_position, label = "Python")
# plt.plot(years , js_position, label = "JavaScript", linestyle = "dashed")
# plt.plot(years , sql_position, label = "SQL", linestyle = "dotted")
# plt.plot(years , typescript_position, label = "TypeScript", linestyle = "dashdot")
# plt.title("Most-Wanted Language Ranking")
# plt.xlabel("Year")
# plt.ylabel("Position")
# plt.ylim(bottom = 20 , top = 0)
# # plt.legend([
# #     "Python",
# #     "JavaScript",
# #     "SQL",
# #     "TypeScript"
# # ])

# plt.legend()

# plt.show()

# ................................... Challenge 1 ........................................
days_of_week = ["Mon" , "Tues" , "Wed" , "Thur" , "Fri"]
YouTube = [2 , 1 , 3 , 6 , 3]
Twitter = [1 , 1 , 0 , 0 , 2]
WhatsApp = [3 , 1 , 0 , 2 , 1]
Raid_ShadowLegends = [0 , 4 , 2 , 3 , 3]
TikTok = [3 , 0 , 1 , 0 , 2]

plt.plot(days_of_week , YouTube, label = "YouTube", marker = 'v')
plt.plot(days_of_week , Twitter, label = "Twitter", marker = 'D', linestyle = "dashed")
plt.plot(days_of_week , WhatsApp, label = "WhatsApp", marker = 's', linestyle = "dotted")
plt.plot(days_of_week , Raid_ShadowLegends, label = "Raid_ShadowLegends", marker = 'h', linestyle = "dashdot")
plt.plot(days_of_week , TikTok, label = "TikTok", marker = 'o', linestyle = (0, (5,10)))
plt.title("Screen Time")
plt.xlabel("Days of Week")
plt.ylabel("hours")
plt.ylim(bottom = 0 , top = 8)
# plt.legend([
#     "Python",
#     "JavaScript",
#     "SQL",
#     "TypeScript"
# ])
 
plt.legend()
plt.show()


