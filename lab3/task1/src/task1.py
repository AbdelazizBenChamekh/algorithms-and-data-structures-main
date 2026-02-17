def task7():
    with open('input.txt', 'r') as f:
        n = int(f.readline())
        m = list(map(float, f.readline().split()))
        residents = []
        for i in range(n):
            residents.append([m[i], i + 1])

    for j in range(1, n):
        key = residents[j]
        i = j - 1
        while i >= 0 and residents[i][0] > key[0]:
            residents[i + 1] = residents[i]
            i -= 1
        residents[i + 1] = key

    result = [residents[0][1], residents[n // 2][1], residents[-1][1]]
    
    with open('output.txt', 'w') as f2:
        f2.write(f"{result[0]} {result[1]} {result[2]}")