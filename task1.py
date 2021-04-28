def difference(arr, n):
 
    # Initialize sums of diagonals
    d1 = 0
    d2 = 0
 
    for i in range(0, n):
     
        for j in range(0, n):
         
            # finding sum of primary diagonal
            if (i == j):
                d1 += arr[i][j]
 
            # finding sum of secondary diagonal
            if (i == n - j - 1):
                d2 += arr[i][j]
         
    # Absolute difference of the sums

    return abs(d1 - d2);
 
# Driver Code
n = 3
 
arr = [[2, 3, 5], [6 , 7, 9],[1, 5, 3]]
 
print(difference(arr, n))

###another solution with ask User to write Matrix
##
##matrix_first_diagonal = 0
##matrix_second_diagonal = 0
##
### To ask user for size of matrix
##rows = cols = int(
##    input("Enter the size of your matrix (note that the matrix is square matrix!)"))
##
##
### 2 loops to take data of matrix from user 
##arr = [[int(input("")) for i in range(cols)]
##       for j in range(rows)]
##print(arr)
##
###  2 for loop to show the data and get diagonals value
##for x in range(len(arr)):
##    for y in range(len(arr)):
##        print(arr[x][y], end=" ")
##        if x == y:
##            matrix_first_diagonal += arr[x][y]
##        if x+y == len(arr):
##            matrix_second_diagonal += arr[x][y]
##    print()
##
## print the value 2 diagonals and absolute result  
##print(f'{matrix_first_diagonal} - {matrix_second_diagonal} =  {abs(matrix_first_diagonal - matrix_second_diagonal)}')
##
