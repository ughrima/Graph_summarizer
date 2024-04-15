import matplotlib.pyplot as plt

# Sample data for plotting
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 15, 30]
labels = ['E', 'F', 'G', 'H', 'I']


# Bar graph
# plt.figure(figsize=(8, 6))
# plt.bar(x, y)
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Bar Graph')
# plt.xticks(x, labels)
# plt.show()

# Sample data for line graph
p = [1, 2, 3, 4, 5]
q = [2, 4, 6, 8, 10]

# Plotting the line graph
plt.plot(p, q)

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Graph')

# Display the plot
plt.show()
