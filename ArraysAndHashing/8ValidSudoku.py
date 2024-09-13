#Notes: can't believe this worked immediately. Solution is O(n^2), only one pass through the board is needed.
#Multiple passes wouldn't change asymptotic runtime but would be lame.

from math import floor

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSeenList = [set() for i in range(9)]
        colSeenList = [set() for i in range(9)]
        boxSeenList = [[set() for i in range(3)] for i in range(3)]
        for i in range(9): #row
            for j in range(9): #col
                num = board[i][j]
                if num != ".":
                    rowSeen = rowSeenList[i]
                    colSeen = colSeenList[j]
                    boxSeen = boxSeenList[floor(i/3)][floor(j/3)]
                    if num in rowSeen or num in colSeen or num in boxSeen:
                        return False
                    rowSeen.add(num)
                    colSeen.add(num)
                    boxSeen.add(num)
        return True
        