#!/usr/bin/python3

from matplotlib import pyplot as plt

# Simple plot using Matplotlib

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Simple Plot')
plt.show()
