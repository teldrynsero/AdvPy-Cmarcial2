n = input("")

x = n.split(" ")

#x[0] is number of shopping lists

#x[1] is number of items on the lists

#columns
n = x[0]
n = int(n)

#rows
m = x[1]
m = int(m)

#Matrix = [[0]*n for _ in range(n)]

w, h = m, n
Matrix = [[0 for x in range(w)] for y in range(h)] 
counter = 0

# prints common element in all
# rows of matrix
def printCommonElements(mat):
    print("I am in the function")
 
    mp = dict()
 
    # initialize 1st row elements
    # with value 1
    for j in range(m):
        mp[mat[0][j]] = 1
 
    # traverse the matrix
    for i in range(1, n):
        for j in range(m):
             
            # If element is present in the
            # map and is not duplicated in
            # current row.
            if (mat[i][j] in mp.keys() and
                             mp[mat[i][j]] == i):
                                  
            # we increment count of the
            # element in map by 1
                mp[mat[i][j]] = i + 1
 
                # If this is last row
                if i == n - 1:
                    print(mat[i][j], end = " ")

while n != 0:
    #print(n)
    lists = input("")
    list = lists.split(" ")
    theCount = 0
    for x in list:
        #print(theCount)
        Matrix[counter][theCount] = list[theCount]
        theCount += 1
        #print(x)
    #Matrix[counter][0] = list
    counter += 1
    n -= 1
    #print(thing)

printCommonElements(Matrix)

print(Matrix)

#print(n)