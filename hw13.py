"""
    Max Shi
    HW 13
    12/3/18
    I pledge my honor that I have abided by the Stevens Honor System
"""

class Board:
    def __init__(self, width = 7, height = 6):
        self.__gameBoard = []
        self.__width = width
        self.__height = height
        for col in range(width):
            self.__gameBoard += [[]]
            #print(self.__gameBoard)
            for row in range(height):
                self.__gameBoard[col] += " "

    def __str__(self):
        s = ""
        for row in range(self.__height):
            s+="|"
            for col in range(self.__width):
                s+=self.__gameBoard[col][row]
                s+="|"
            s+="\n"
        s+="-"*(self.__width*2+1)+"\n"
        for col in range(self.__width):
            s+=" "+str(col)
        return s+"\n"

    def allowsMove(self, col):
        return self.__gameBoard[col][0] == " "
    
    def addMove(self, col, ox):
        if self.allowsMove(col):
            topindex = 0
            while(topindex<self.__height and self.__gameBoard[col][topindex]==" "):
                topindex+=1
            self.__gameBoard[col][topindex-1] = ox
            return True
        else: return False
    
    def setBoard( self, moveString ):
        """ takes in a string of columns and places
        alternating checkers in those columns,
        starting with 'X'
        For example, call b.setBoard('012345')
        to see 'X's and 'O's alternate on the
        bottom row, or b.setBoard('000000') to
        see them alternate in the left column.
        moveString must be a string of integers
        """
        nextCh = 'X'   # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.__width:
                self.addMove(col, nextCh)
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'
            
    def delMove(self, col):
        for column in self.__gameBoard:
            for entry in column:
                if entry != " ":
                    entry = " "
                    break

    def winsFor(self, ox):
        maxRow = self.__height-3
        maxCol = self.__width-3
        for col in range(self.__width):
            for row in range(self.__height):
                if col<maxCol:
                    #check horiz
                    if(self.__gameBoard[col][row] == ox):
                        curCol = col+1
                        counter = 1
                        while counter<4 and self.__gameBoard[curCol][row] == ox:
                            curCol += 1
                            counter += 1
                        if counter == 4:
                            return True
                if row<maxRow:
                    #check vert
                    if(self.__gameBoard[col][row] == ox):
                        curRow = row + 1
                        counter = 1
                        while counter<4 and self.__gameBoard[col][curRow] == ox:
                            curRow += 1
                            counter += 1
                        if counter == 4:
                            return True
                if row<maxRow and col<maxCol:
                    #check SE diag
                    if(self.__gameBoard[col][row] == ox):
                        curRow = row + 1
                        curCol = col + 1
                        counter = 1
                        while counter<4 and self.__gameBoard[curCol][curRow] == ox:
                            curRow+=1
                            curCol+=1
                            counter+=1
                        if counter == 4:
                            return True
                if row>2 and col<maxCol:
                    #check NE diag
                    if self.__gameBoard[col][row] == ox:
                        curRow = row-1
                        curCol = col+1
                        counter = 1
                        while counter<4 and self.__gameBoard[curCol][curRow] == ox:
                            curRow -= 1
                            curCol += 1
                            counter += 1
                        if counter == 4:
                             return True
        return False
    
    def hostGame(self):
        gameDone = False
        turn = "X"
        while(not gameDone):
            xInput = -1
            while (0>xInput or xInput>self.__width) and self.allowsMove(xInput):
                try:
                    xInput = int(input("Input "+turn+"'s move: "))
                except ValueError:
                    xInput = -1
            self.addMove(xInput, turn)
            print(self)
            if self.winsFor(turn):
                print(turn+" wins!")
                gameDone = True
            elif turn=="X": turn = "O"
            else: turn = "X"




b = Board()
b.setBoard("1212121")
print(b)
a = Board()
a.setBoard("12234334454")
print(a)
c = Board()
c.setBoard("11223344")
print(c)
d = Board()
d.setBoard("43321221161")
print(d)