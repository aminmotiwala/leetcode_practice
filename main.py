from TopKFrequent_347 import SolutionTopK
from ProductArrayExceptSelf_238 import SolutionProductArray
from BinarySearchRevision import SolutionBinarySearch

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

if __name__ == '__main__':
    performBinarySearch() # call the method you want to run.


