# Initialize the sum variable
S = 0

# Loop through numbers from 1 to 100
for n in range(1, 101):
    # Check if the number is even
    if n % 2 == 0:
        # Add the even number to the sum
        S += n

# Print the result
print(S)
