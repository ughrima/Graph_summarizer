import matplotlib.pyplot as plt

# Sample data for plotting
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 15, 30]
# Sample data for plotting
labels = ['A', 'B', 'C', 'D', 'E']
sizes = [15, 30, 25, 10, 20] 
scatter_x = [1, 2, 3, 4, 5]
scatter_y = [10, 15, 20, 25, 30]
areas = [100, 200, 300, 400, 500]
line_x = [1, 2, 3, 4, 5]
line_y = [10, 15, 20, 25, 30]

# Bar graph
plt.figure(figsize=(8, 6))
plt.bar(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Bar Graph')
plt.xticks(x, labels)
plt.show()
import matplotlib.pyplot as plt


# Pie chart
plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Pie Chart')
plt.savefig('pie_chart.png')  # Save the plot as an image
plt.close()


# Scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(scatter_x, scatter_y, s=areas)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')
plt.show()

# Area graph
plt.figure(figsize=(8, 6))
plt.fill_between(line_x, line_y, color="skyblue", alpha=0.4)
plt.plot(line_x, line_y, color="Slateblue", alpha=0.6, linewidth=2)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Area Graph')
plt.show()

# Line chart
plt.figure(figsize=(8, 6))
plt.plot(line_x, line_y, marker='o')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Chart')
plt.show()

import matplotlib.pyplot as plt

# Data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [20, 35, 30, 25]

# Method 1: Vertical Bar Graph
plt.figure(figsize=(8, 6))
plt.bar(categories, values, color='skyblue')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Vertical Bar Graph')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Method 2: Horizontal Bar Graph
plt.figure(figsize=(8, 6))
plt.barh(categories, values, color='lightgreen')
plt.xlabel('Values')
plt.ylabel('Categories')
plt.title('Horizontal Bar Graph')
plt.grid(True)
plt.tight_layout()
plt.show()
