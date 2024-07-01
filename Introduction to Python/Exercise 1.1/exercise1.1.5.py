# Initialize a list to store the integers
divisible_by_3_not_2 = []

# Loop through numbers from 1 to 100
for number in range(1, 101):
    # Check if the number is divisible by 3 but not divisible by 2
    if number % 3 == 0 and number % 2 != 0:
        # Add the number to the list
        divisible_by_3_not_2.append(number)

# Print the integers
print("Integers between 1 and 100 that are divisible by 3 but not divisible by 2:")
print(divisible_by_3_not_2)

# Print the count of such integers
print("Total number of such integers:", len(divisible_by_3_not_2))
