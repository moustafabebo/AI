matrix_first_diagonal = 0
matrix_second_diagonal = 0

# To ask user for size of matrix
rows = cols = int(
    input("Enter the size of your matrix (note that the matrix is square matrix!)"))


# 2 loops to take data of matrix from user 
arr = [[int(input("")) for i in range(cols)]
       for j in range(rows)]
print(arr)

#  2 for loop to show the data and get diagonals value
for x in range(len(arr)):
    for y in range(len(arr)):
        print(arr[x][y], end=" ")
        if x == y:
            matrix_first_diagonal += arr[x][y]
        if x+y == len(arr):
            matrix_second_diagonal += arr[x][y]
    print()

# print the value 2 diagonals and absolute result  
print(f'{matrix_first_diagonal} - {matrix_second_diagonal} =  {abs(matrix_first_diagonal - matrix_second_diagonal)}')
