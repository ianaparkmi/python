def transpose(matrix):
    transposed = []
    for col in range(len(matrix[0])):  
        new_row = []
        for row in range(len(matrix)):
            new_row.append(matrix[row][col])
        transposed.append(new_row)  
    return transposed

rows = int(input('Enter the number of rows: '))  
matrix = []
print("Enter the matrix line by line (numbers separated by spaces):")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

print('Original matrix:')
for row in matrix:
    print(row)

result = transpose(matrix)
print('Transposed matrix:')
for row in result:
    print(row)