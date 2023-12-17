from TopKFrequent_347 import SolutionTopK
from ProductArrayExceptSelf_238 import SolutionProductArray

def topK():
    topKSolution = SolutionTopK()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(topKSolution.topKFrequentOptimized(nums, k))

def productArray():
    productArraySolution = SolutionProductArray()
    nums = [1,2,3,4]
    print(productArraySolution.productExceptSelfOptimized(nums))

if __name__ == '__main__':
    productArray() # call the method you want to run.


