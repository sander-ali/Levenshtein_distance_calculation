import sys
import time

Dcost = 2
Icost = 1
Scost = 1


def main():
    string1 = "DIGITAL"
    string2 = "VIRTUAL"
    t =  time.clock()
    print (u"Levenshtein Distance: {}\nText: {}\n\nCost Deletion Cost: {}\nCost Insertion Cost: {}\nCost Substitution Cost: {}\n".format(string1, string2, Dcost, Icost, Scost))
    print (u"Distance Edit: {}".format(levenshtein_distance(string1, string2)))
    print (u"Calculation Time: {} seconds".format(time.clock() - t)) 

    
    
def levenshtein_distance(string1, string2):
    '''This function returns the editing distance of Levenshtein between two
    strings given a certain deletion, insertion, and substitution cost.'''
    m = len(string1)
    n = len(string2)
    
    # Editing distance matrix
    E = [[0 for x in range (m + 1)] for x in range (n+1)]
    
    # Initializing first column
    for i in range(n + 1):
        E[i][0] = i * Dcost
      
    # Initializing first row  
    for j in range (m + 1):
        E[0][j] = j * Icost
        
    '''Each row is traversed by filling each box with the editing distance
    of the prefix to and from string1 and to j of the string2; this value is
    minimum between the editing distance between string1[0:i-1] and string2[0:j]
    plus the deletion cost, the editing distance between string1[0:i] and
    string2[0:j-1] plus insertion cost and editing distance between string1[0:i-1]
    and string2 [0:j-1] plus substitution cost.'''
    for i in range(1, (n + 1)):
        for j in range(1, (m + 1)):
            E[i][j] = min(E[i-1][j] + Dcost, E[i][j-1] + Icost, E[i-1][j-1] + diff_val(string1, string2, j, i))           
            
    showMatrix(E, n+1, m+1)  
    
    return E[n][m]


def diff_val(string1, string2, i, j):
    '''The function returns the difference value (0 in case of equality and 
    the value of substitution in case of inequality) resulting from comparing
    the same character of string1 and the true condition of string2'''
    if string1[i-1] == string2[j-1]:
        return 0
    return Scost


def showMatrix(matrix, rowCount, columnCount):   
    print ("Array")
    for row in range(rowCount):
        for column in range(columnCount):
            space = ""
            if int(matrix[row][column]) <= 10:
                space = " "
            print (str(matrix[row][column]) + space),
        print ("\n") 
        


if __name__ == "__main__":
    main(*sys.argv[1:])