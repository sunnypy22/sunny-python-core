
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.figure(figsize=(8, 5))
plt.plot(x, y, 'b-', linewidth=2, label='sin(x)')
plt.title("Simple Line Plot")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.grid(True)
plt.legend()
plt.show()

