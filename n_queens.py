n = 10
result = []
outputNumber = 1


def solve_n_queens():  
    columnIndices = []
    search(columnIndices)  
    return result

def search(columnIndices):
    if n == len(columnIndices):
        result.append(tuple(columnIndices))
        return
    if len(result) == outputNumber:
        return 
    for columnIndex in range (n):       
        if isValid(columnIndices, columnIndex):               
            columnIndices.append(columnIndex)
            search(columnIndices)
            columnIndices.remove(columnIndex)
        

def isValid(columnIndices, columnIndex):
    rowIndex =len(columnIndices)
    for row,column in enumerate(columnIndices):
        if column == columnIndex:
            return False
    
        if row + column == rowIndex + columnIndex:
            return False
    
        if column - row == columnIndex - rowIndex:
            return False    
    return True
        

def print_result(result):
    solve_n_queens()
    for each in result:
        for row,column in enumerate(each):
           print("(",row,",",column,")",sep = "",end = " ")         
        print()


print_result(result)