# Initialize the count variable
count = 0

# Loop through possible values of a
for a in range(1, 11):
    # Loop through possible values of b
    for b in range(1, a + 1):
        # Loop through possible values of c
        for c in range(1, b + 1):
            # Check if the sum of a, b, and c is 10
            if a + b + c == 10:
                # Print the triple (c, b, a)
                print(c, b, a)
                # Increment the count
                count += 1

# Print the total count of triples
print('The number is', count)
