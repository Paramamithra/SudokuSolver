def getinput(): #Gets input from the user row wise
    board=[]
    for i in range(1,10,1):
        row=input('Enter entries of row number '+str(i) +" :  ")
        board.append(row)
    return board

def printboard(board): #Prints the sudoku board
    print("-"*23) # Starting Line (Horizontal Line)
    for row in board:
        print("| ",end="") # Starting line (Vericle Line)
        for i in range(0,9,1):
            print(row[i]+" ",end="")
            if i==2 or i==5 or i==8:
                print("|",end="") #Internal 3x3 grid lines (horizontal)
        print()
        if board.index(row)==2 or board.index(row)==5 or board.index(row)==8:
            print("-"*23) # Ending Line (Horizontal Line)

def markboard(board): # Marking intial board with filled and unfilled elements for backtracking
    refboard=[]
    for row in board:
        refrow="" #initialising string
        for element in row:
            if element.isnumeric(): #Checking initial element is filled or not
                refrow=refrow+"1" #if filled mark as '1' in reference board
            else:
                refrow=refrow+"0" #if unfilled mark as '0' in reference board
        refboard.append(refrow) #append row
    return refboard

def getinterboardrow(row,column): #Get 3x3 grid as a single string
    interrow=int(row/3)
    intercolumn=int(column/3)
    interboard=createinterboard(board)
    return interboard[interrow*3+intercolumn] #return 3x3 grid as a single string

def fillelement(row,column,start): #enter valid entry in row x column 
    for x in range(int(start)+1,10,1): #check each number from start
        if str(x) in board[row]: #check number repeats in the row
            continue #if yes go to next number (increment x by 1)
        else: #else check number repeats in column
            elecol='' #initialising 
            for rows in board:
                elecol=elecol+rows[column] #getting a column in single string
            if str(x) in elecol: #check if number repeats in a column
                continue # if yes go to next number (increment x by 1)
            else: #check if number repeats in 3x3 grid
                interboardrow=getinterboardrow(row,column) #getting 3x3 grid in a single string 
                if str(x) in interboardrow: #check if number repeats in 3x3 grid
                    continue # if yes go to next number (increment x by 1)
                else: #enter the number in row x column
                    board[row]=board[row][:column]+str(x)+board[row][column+1:] 
                    return True #return true stating successful entry
    if board[row].isnumeric(): #if the entry is number return true stating successful entry
        return True
    return False #if x exceeds 9 and entry is not number then return false stating unsuccessful entry

def backtractcoord(board,refboard,i,j): #get location of previous filled element but was initailly unfilled refrence from (refboard)
    for k in range(i,-1,-1): #go back by one row
        for l in range(j,-1,-1): #go back by one column
            if refboard[k][l]=='0': #checking in refboard that initially it was unfilled
                start=board[k][l] #get value of number to start for filling element
                board[k]=board[k][:l]+'-'+board[k][l+1:] #replacing number with '-'
                return k,l,start #return position and starting number for filling element
        j=8 #start from last column in a new row

def backtrack(board,refboard,i,j,start): #iterating through all elements 
    for row in range(0,9,1): #iterating through each row
        if row<i:continue #for row index equal or greater than last fill
        for column in range(0,9,1): #iterating through each column
            if column<j: continue #for column index equal or greater than last fill
            if not board[row][column].isnumeric(): #check if the element is not filled
                check=fillelement(row,column,start) #fill and get bool as success or unsccuessful in return
                start=0 #start from 0 for next filling
                if not check: #if unsuccesful
                    k,l,start=backtractcoord(board,refboard,row,column-1) #get location of previous filled element but was initailly unfilled refrence from (refboard)
                    backtrack(board,refboard,k,l,start) #backtrack
        j=0 #initialise last fill as 0
    i=0 #initialise last fill as 0

def createinterboard(board): #create array in which each element is 3x3 grid elements
    interboard=[]
    for x in range(0,9,3): 
        for y in range(0,9,3):
            interboard.append(board[x][y:y+3]+board[x+1][y:y+3]+board[x+2][y:y+3])
    return interboard

board=getinput()
print('Entered Sudoku Board is as follows:')
printboard(board)
refboard=markboard(board)
backtrack(board,refboard,0,0,0)
print('Solved Board is as Follows:')
printboard(board)
k=input('Press Enter to exit')
