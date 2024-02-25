class SortingAlgos(object):
    def selectionSort(self, nums):

        for outer in range(len(nums)):
            # suppose min is outer
            min_index = outer
            for inner in range(outer+1, len(nums)):
                if nums[inner] < nums[min_index]:
                    min_index = inner

            #swap min with outer
            temp = nums[outer]
            nums[outer] = nums[min_index]
            nums[min_index] = temp


        return nums