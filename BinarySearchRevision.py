class SolutionBinarySearch(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid+1

        return -1

    def searchRecursive(self, nums, target):

        if len(nums) == 0:
            return -1

        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.searchRecursive(nums[:mid-1], target)
        elif nums[mid] < target:
            return self.searchRecursive(nums[mid+1:], target)
