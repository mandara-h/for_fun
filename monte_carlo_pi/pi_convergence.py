import random
import matplotlib.pyplot as plt

N = int(input("Enter the number of random points you want to generate: "))
estimates = []
inside_circle = 0

for i in range(1, N+1):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if (x**2 + y**2 <= 1):
        inside_circle += 1
    estimates.append(4* (inside_circle/i))

plt.plot(estimates)
plt.axhline(y=3.14159, color='r', linestyle='--', label='Actual pi')
plt.title("Convergence of Pi Estimate")
plt.xlabel('Number of Points')
plt.ylabel('Estimated Pi')
plt.legend()
plt.grid(True)
plt.savefig(f'convergence_{str(N)}')
plt.show()
