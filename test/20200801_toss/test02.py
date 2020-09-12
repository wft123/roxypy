def check_len(matrix):
    n = len(matrix)
    m = len(matrix[0])
    result = 0

    for i in range(0, n):
        for j in range(0, m):
            if matrix[i][j] == 1:
                if i-1 >= 0 and matrix[i-1][j] == 0:
                    result += 1
                if i+1 < n and matrix[i+1][j] == 0:
                    result += 1
                if j-1 >= 0 and matrix[i][j-1] == 0:
                    result += 1
                if j+1 < m and matrix[i][j+1] == 0:
                    result += 1

    print(result)


data = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
check_len(data)
