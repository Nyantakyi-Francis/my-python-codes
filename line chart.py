import matplotlib.pyplot as plt
# data
years = [2018, 2019, 2020, 2021, 2022]
sales = [150, 180, 210, 190, 240]

# create chart
plt.plot(years, sales, marker='o', color='blue')
plt.title("Company Sales Over Time")
plt.xlabel("year")
plt.ylabel("Sales (in thousands)")
plt.grid(True)
plt.show()