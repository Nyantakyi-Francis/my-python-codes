import matplotlib.pyplot as plt

# Data to plot
labels = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [45, 25, 15, 15]  # These usually add up to 100
colors = ['skyblue', 'gold', 'lightcoral', 'lightgreen']
explode = (0.1, 0, 0, 0)  # "explode" the 1st slice (Python)

# Create the pie chart
plt.pie(sizes, 
        explode=explode, 
        labels=labels, 
        colors=colors,
        autopct='%1.1f%%', # Adds the percentage formatted to 1 decimal place
        shadow=True, 
        startangle=140)

plt.title("Programming Language Popularity")
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Show the plot
plt.show()
