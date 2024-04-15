# To plot the graphs 

import matplotlib.pyplot as plt

# Bar graph
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 15, 30]
labels = ['E', 'F', 'G', 'H', 'I']

plt.figure(figsize=(8, 6))
plt.bar(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Bar Graph')
plt.xticks(x, labels)
plt.show()

# line graph
p = [1, 2, 3, 4, 5]
q = [2, 4, 6, 8, 10]

plt.plot(p, q)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Graph')

plt.show()
