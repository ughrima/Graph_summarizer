import matplotlib.pyplot as plt

# Sample data for plotting
x = [1, 2, 3, 4, 5]
y = [10, 15, 20, 25, 30]
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
