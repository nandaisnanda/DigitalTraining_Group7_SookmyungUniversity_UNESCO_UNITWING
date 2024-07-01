# Initialize the sum variable
S = 0

# Loop through numbers from 1 to 100000
for n in range(1, 100001):
    # Add the term 1/n^2 to the sum
    S += 1 / (n ** 2)

# Print the result of the sum
print(S)

# Print the value of (3.141592^2) / 6
print(3.141592 ** 2 / 6)
