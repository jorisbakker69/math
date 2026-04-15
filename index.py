import numpy as np

# Simple dataset (you can change these numbers)
data = np.array([1.0, 2.0, 3.0, 4.0, 5.0])

# Very small number to change one value in the data
epsilon = 1e-4

def mean(x):
    return np.mean(x)

def variance(x):
    # Sample variance (common in statistics)
    return np.var(x, ddof=1)

# Calculate mean and variance for the original data
base_mean = mean(data)
base_var = variance(data)

print(f"Base mean: {base_mean:.6f}")
print(f"Base variance: {base_var:.6f}")

# Here we check: how much do mean and variance change
# if we slightly change each data point?
mean_sensitivity = []
var_sensitivity = []

for i in range(len(data)):
    # Copy the data so we don't change the original array
    perturbed = data.copy()

    # Add a small value to one element
    perturbed[i] += epsilon

    # Recalculate mean and variance
    new_mean = mean(perturbed)
    new_var = variance(perturbed)

    # Approximate "derivative":
    # change in result / change in input
    d_mean = (new_mean - base_mean) / epsilon
    d_var = (new_var - base_var) / epsilon

    mean_sensitivity.append(d_mean)
    var_sensitivity.append(d_var)

mean_sensitivity = np.array(mean_sensitivity)
var_sensitivity = np.array(var_sensitivity)

print("\nApprox. change of mean when we change each x_i (d mean / d x_i):")
print(mean_sensitivity)

print("\nApprox. change of variance when we change each x_i (d variance / d x_i):")
print(var_sensitivity)

# For the mean, we can also write the exact formula:
# if there are n points, each x_i has the same effect: 1/n
n = len(data)
analytic_d_mean = np.ones(n) / n

print("\nExact change of mean (1/n for each x_i):")
print(analytic_d_mean)

print("\nDifference: numeric - exact (should be very small):")
print(mean_sensitivity - analytic_d_mean)
