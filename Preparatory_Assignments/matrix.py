# Q6: Matrix Multiplication
A = [[1, 2], [3, 4]]
B = [[2, 0], [1, 2]]

# Result matrix with zeros
result = [[0, 0], [0, 0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

print("Matrix Multiplication Result:")
for row in result:
    print(row)
