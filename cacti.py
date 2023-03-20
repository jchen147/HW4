def cacti_number(array):
    rows = len(array)
    columns = len(array[0])

    plantable = 0

    for i in range(rows):
        for j in range(columns):
            if array[i][j] == 0:
                adjacent = False
                if i < rows-1 and array[i+1][j] == 1:
                    adjacent = True
                if j < columns-1 and array[i][j+1] == 1:
                    adjacent = True
                if i > 0 and array[i-1][j] == 1:
                    adjacent = True
                if j > 0 and array[i][j-1] == 1:
                    adjacent = True
                    
                if adjacent == False:
                    array[i][j] = 1
                    plantable += 1
    
    return plantable
