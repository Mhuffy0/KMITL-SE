n = float(input("Enter the number to find the square root of: "))

guess = n / 2

for _ in range(5):
    temp = n / guess
    guess = (guess + temp) / 2

approximation_5_times = guess
print(f"Approximation after 5 iterations: {approximation_5_times:.3f}")

# Reset
guess = n / 2

for _ in range(6):
    temp = n / guess
    guess = (guess + temp) / 2

approximation_6_times = guess
print(f"Approximation after 6 iterations: {approximation_6_times:.3f}")

# Reset
guess = n / 2

for _ in range(7):
    temp = n / guess
    guess = (guess + temp) / 2

approximation_7_times = guess
print(f"Approximation after 7 iterations: {approximation_7_times:.3f}")
