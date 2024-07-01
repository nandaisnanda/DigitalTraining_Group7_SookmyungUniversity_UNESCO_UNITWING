# Initialize a list to store the valid triples
valid_triples = []

# Loop through possible values of a, b, and c
for a in range(1, 11):
    for b in range(1, a + 1):
        for c in range(1, b + 1):
            if a + b + c == 10:
                valid_triples.append((a, b, c))

# Print the valid triples
print("Valid triples (a, b, c) such that a + b + c = 10 and a >= b >= c > 0:")
for triple in valid_triples:
    print(triple)

# Print the count of valid triples
print("Total number of valid triples:", len(valid_triples))
