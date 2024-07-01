# Initialize the count variable
count = 0

# Loop through numbers from 1 to 100
for n in range(1, 101):
    # Check if the number is divisible by 3 and not divisible by 2
    if n % 3 == 0 and n % 2 != 0:
        # Print the number
        print(n)
        # Increment the count
        count += 1

# Print the count of numbers
print('The number is', count)
