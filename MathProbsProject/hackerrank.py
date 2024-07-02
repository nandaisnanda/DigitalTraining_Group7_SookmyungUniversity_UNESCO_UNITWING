def solve(arr, queries):
    results = []
    for query in queries:
        x, y = query
        # Adjust for 1-based indexing
        x -= 1
        y -= 1
        odd = True
        for i in range(x, y + 1):
            if arr[i] % 2 == 0:
                odd = False
                break
        if odd:
            results.append("Odd")
        else:
            results.append("Even")
    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = solve(arr, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
