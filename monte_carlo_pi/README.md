# Monte Carlo Estimation of pi

This project uses the Monte Carlo method to estimate the value of pi by simulating random points inside a square and checking how many fall inside a circle of unit radius.

# What is Monte Carlo Estimation?

Monte Carlo methods use randomness and statistical sampling to estimate mathematical results. In this case, we approximate pi using random points inside a square:

1. A unit circle of radius 1 fits inside a square of side length 2.
2. Area of the circle is pi(r)(r) = pi.
3. Area of the square is (2)(2) = 4.
4. The ratio of the area of the circle to the square is pi/4.
5. By randomly sampling points and checking whether they fall inside the circle, we can estimate pi as follows:

$$\pi \approx 4 \times \frac{\text{Points inside circle}}{\text{Total points}}$$

# How It Works

1. Generate `N` random points inside a square with sides from -1 to 1.
2. Check whether each point lies inside the unit circle (i.e. $x^2 + y^2 \leq 1$).
3. Count how many points fall inside.
4. Estimate pi using:

```python
pi_estimate = 4 * (inside_circle / total_points)

# Convergence Plot

Additionally, for any given value of N, a convergence plot can be generated. With each newly generated sample pi is freshly estimated, until N sample points are collected. This shows that the pi estimation progressively improves as the number of sample points considered increases.
