# Compute the sum of 1/n^2 from n=1 to 100000
total_sum = sum(1 / (n ** 2) for n in range(1, 100001))

# Compute the value of pi^2 / 6
pi = 3.141592
pi_squared_div_6 = (pi ** 2) / 6

# Print the results
print(f"Sum of 1/n^2 from n=1 to 100000 is {total_sum}")
print(f"Value of pi^2 / 6 is  {pi_squared_div_6}")

# Compare the two values
difference = abs(total_sum - pi_squared_div_6)
print(f"Difference between the two values is{difference}")
