
def splicematrix(matrix,column,row=0):
    newmatrix = []
    for rownum in range(len(matrix)):
        currentrow = []
        if rownum != row:
            for columnnum in range(len(matrix)):
                if columnnum != column:
                    currentrow.append(matrix[rownum][columnnum])
                    # print(rownum,columnnum)
                    # print(currentrow)
            newmatrix.append(currentrow)
    return newmatrix
def determinant2x2(matrix):
    return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

def adjudicate(matrix):
    size = len(matrix)
    newmatrix = [[i for i in row] for row in matrix]
    for rowi in range(size):
        for coli in range(size):
            if rowi != coli:
                newmatrix[coli].pop(rowi)
                newmatrix[coli].insert(rowi,matrix[rowi][coli])
                # print(newmatrix,matrix,matrix[rowi][coli],rowi,coli)
    return newmatrix

def multMatrix(num,matrix):
    newmatrix = [[i*num for i in row] for row in matrix]
    return newmatrix

def matrixofMinors(matrix):
    size = len(matrix)
    newmatrix = [[] for i in range(size)]
    for rowi in range(size):
        for coli in range(size):
            if (coli+rowi)%2 == 1:
                newmatrix[rowi].append(-largedeterminant(splicematrix(matrix,coli,rowi)))
            else:
                newmatrix[rowi].append(largedeterminant(splicematrix(matrix,coli,rowi)))
    return newmatrix

# def splicematrix(matrix,row,col):
#     size = len(matrix)
#     newmatrix = []
#     for rowi in range(size):
#         currentrow = []
#         if rowi != row:
#             for coli in range(size):
#                 if coli != col:
#                     currentrow.append(matrix[rowi][coli])
#             newmatrix.append(currentrow)
#     return newmatrix

def largedeterminant(matrix,column=0):
    if len(matrix) == 2:
        # print(matrix)
        return determinant2x2(matrix)
    if column == len(matrix)-1:
        return (-1)**column * matrix[0][column]*largedeterminant(splicematrix(matrix,column))
    return (-1)**column * matrix[0][column]*largedeterminant(splicematrix(matrix,column))+largedeterminant(matrix,column+1)

def inversematrix(matrix):
    determinant = largedeterminant(matrix)
    return multMatrix(1/determinant,adjudicate(matrixofMinors(matrix)))


# print(splicematrix([[1,2,3],[1,2,3],[1,2,3]],2))
# print(largedeterminant([[1,0,0],[0,1,0],[0,0,1]]))
# print(splicematrix([[1,2,3],[4,5,6],[7,8,9]],1,1))
# print(matrixofMinors([[3,0,2],[2,0,-2],[0,1,1]]))
# print(multMatrix(2,[[1,1],[2,2]]))
# print(determinant2x2([[1,2],[3,4]]))
# print(splicematrix([[5,6,9],[7,100,2],[3,5,23]],0))
# print(adjudicate([[1,2,3],[4,5,6],[7,8,9]]))
print(inversematrix([[2,3,5,7],[11,13,17,19],[23,29,31,37],[41,43,47,53]]))