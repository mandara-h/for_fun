import random
import matplotlib.pyplot as plt

N = int(input("Enter the number of random points you would like to generate: "))
inside_circle = 0
x_inside = [] 
y_inside = []
x_outside = []
y_outside = []

for i in range(N):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if (x**2 + y**2) <= 1:
        inside_circle += 1
        x_inside.append(x)
        y_inside.append(y)
    else:
        x_outside.append(x)
        y_outside.append(y)

pi_estimate = 4* (inside_circle / N)
print(f"The estimated value of pi is: {pi_estimate}")

plt.figure(figsize=(6,6))
plt.scatter(x_inside, y_inside, color='blue', s=1, label='Inside Circle')
plt.scatter(x_outside, y_outside, color='red', s=1, label='Outside Circle')
plt.title(f"Estimating pi using Monte Carlo ({N})\nEstimated pi value = {pi_estimate:.5f}")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.axis('square')
plt.savefig(f'plot_{str(N)}')
plt.show()
