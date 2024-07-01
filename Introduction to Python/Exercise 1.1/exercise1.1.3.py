#add up all even numbers between 1 and 100
# Initialize the sum variable
total_sum = 0

# Loop through numbers from 1 to 100
for number in range(1, 101):
    # Check if the number is even
    if number % 2 == 0:
        # Add the even number to the total sum
        total_sum += number

# Print the result
print("The sum of all even numbers between 1 and 100 is:", total_sum)
