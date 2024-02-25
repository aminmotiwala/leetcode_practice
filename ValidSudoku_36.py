from collections import defaultdict


class ValidSudokuSolution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        columnsDict = defaultdict(set)
        rowsDict = defaultdict(set)
        subSquares = defaultdict(set) #key will be column number which is num//3 so it will 0 , 0, 0, 1, 1 , 1

        for rowNum in range(9):
            for colNum in range(9):
                if board[rowNum][colNum] == ".":
                    continue
                val = board[rowNum][colNum]
                squareRowIndex = rowNum // 3
                sququareColIndex = colNum // 3
                subSquareKey = str(squareRowIndex) + "-"+str(sququareColIndex)
                if val in columnsDict[colNum] or val in rowsDict[rowNum] or val in subSquares[subSquareKey]:
                    return False
                else:
                    columnsDict[colNum].add(val)
                    rowsDict[rowNum].add(val)
                    subSquares[subSquareKey].add(val)

        return True