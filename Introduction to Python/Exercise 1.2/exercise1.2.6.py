# Initial principal amount
P = 100

# Annual interest rate
r = 0.07

# Loop through 10 years
for n in range(10):
    # Update the principal amount with interest
    P = P * (1 + r)

# Print the final amount
print('The amount is', P)
