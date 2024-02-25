from TopKFrequent_347 import SolutionTopK
from ProductArrayExceptSelf_238 import SolutionProductArray
from BinarySearchRevision import SolutionBinarySearch
from SortingRevision import SortingAlgos
from ValidSudoku_36 import ValidSudokuSolution

def topK():
    topKSolution = SolutionTopK()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(topKSolution.topKFrequentOptimized(nums, k))

def productArray():
    productArraySolution = SolutionProductArray()
    nums = [1,2,3,4]
    print(productArraySolution.productExceptSelfOptimized(nums))

def performBinarySearch():
    nums = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target = 23
    binarySearch = SolutionBinarySearch()
    print(binarySearch.search(nums,23))
    print(binarySearch.searchRecursive(nums,23))

def performSelectionSort():
    nums = [64, 25, 12, 22, 11]
    sortingAlogs = SortingAlgos()
    print(sortingAlogs.selectionSort(nums))

def checkSudokuBoard():
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    validSudoku = ValidSudokuSolution()
    print(validSudoku.isValidSudoku(board))

if __name__ == '__main__':
    checkSudokuBoard() # call the method you want to run.


