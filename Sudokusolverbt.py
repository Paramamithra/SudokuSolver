def getinput():
    board=[]
    for i in range(1,10,1):
        row=input('Enter entries of row number '+str(i) +" :  ")
        board.append(row)
    return board

def printboard(board):
    print("-"*23)
    for row in board:
        print("| ",end="")
        for i in range(0,9,1):
            print(row[i]+" ",end="")
            if i==2 or i==5 or i==8:
                print("|",end="")
        print()
        if board.index(row)==2 or board.index(row)==5 or board.index(row)==8:
            print("-"*23)

def markboard(board):
    refboard=[]
    for row in board:
        refrow=""
        for element in row:
            if element.isnumeric():
                refrow=refrow+"1"
            else:
                refrow=refrow+"0"
        refboard.append(refrow)
    return refboard

def getinterboardrow(row,column):
    interrow=int(row/3)
    intercolumn=int(column/3)
    interboard=createinterboard(board)
    return interboard[interrow*3+intercolumn]

def fillelement(row,column,start):
    for x in range(int(start)+1,10,1):
        if str(x) in board[row]:
            continue
        else:
            elecol=''
            for rows in board:
                elecol=elecol+rows[column]
            if str(x) in elecol:
                continue
            else:
                interboardrow=getinterboardrow(row,column)
                if str(x) in interboardrow:
                    continue
                else:
                    board[row]=board[row][:column]+str(x)+board[row][column+1:]
                    return True
    if board[row].isnumeric():
        return True
    return False

def backtractcoord(board,refboard,i,j):
    for k in range(i,-1,-1):
        for l in range(j,-1,-1):
            if refboard[k][l]=='0':
                start=board[k][l]
                board[k]=board[k][:l]+'-'+board[k][l+1:]
                return k,l,start
        j=8

def backtrack(board,refboard,i,j,start):
    for row in range(0,9,1):
        if row<i:continue
        for column in range(0,9,1):
            if column<j: continue
            if not board[row][column].isnumeric():
                check=fillelement(row,column,start)
                start=0
                if not check:
                    k,l,start=backtractcoord(board,refboard,row,column-1)
                    backtrack(board,refboard,k,l,start)
        j=0
    i=0

def createinterboard(board):
    interboard=[]
    for x in range(0,9,3):
        for y in range(0,9,3):
            interboard.append(board[x][y:y+3]+board[x+1][y:y+3]+board[x+2][y:y+3])
    return interboard

print('Created by ParamaSys For any details contact reply.paramasys@gmail.com')
board=getinput()
print('Entered Sudoku Board is as follows:')
printboard(board)
refboard=markboard(board)
backtrack(board,refboard,0,0,0)
print('Solved Board is as Follows:')
printboard(board)
k=input('Press Enter to exit')
