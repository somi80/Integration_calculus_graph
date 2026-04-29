print("Function :\nf(x)=x^2")  # f(x) = x^2

a = int(input("Enter limits a: "))
b = int(input("Enter limits b: "))
n = int(input("Enter subinterval: "))

h = (b - a) / n

# List to store x and y values
x = [a + i * h for i in range(n + 1)]
y = [xi**2 for xi in x]  # Compute y values for f(x) = x^2

def Trapfun(y, h):
    total = y[0] + y[-1]  # First and last terms
    total += 2 * sum(y[1:-1])  # Sum of intermediate terms

    result = (h / 2) * total
    print("Solution of function is:", result)

# Call the function with computed y values
Trapfun(y, h)

import matplotlib.pyplot as plt
import numpy as np

# Define the x values
x = np.linspace(a, b,50)

# Define the y values for the quadratic function
y = x**2

# Plot the quadratic function
plt.plot(x, y)

# Add title and labels
plt.title("Quadratic Function: y = x^2")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Add grid
plt.grid(True)

# Display the graph
plt.show()