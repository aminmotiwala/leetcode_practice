class SolutionProductArray(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0 for i in range(len(nums))]
        for outerIndex in range(len(nums)):
            total = 1
            for innerIndex in range(len(nums)):
                if outerIndex == innerIndex:
                    continue

                total = total * nums[innerIndex]

            result[outerIndex] = total

        return result

    def productExceptSelfOptimized(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #youtube: https://www.youtube.com/watch?v=bNvIQI2wAjk

        # for input nums = [1,2,3,4]
        # lets calculate prefix product, this will be product uptil now including current
        # outcome [1,2,6,24]
        # lets calculate postfix product, this will be product uptil now including current in reverse order
        # outcome [24,24,12,4]
        # now for result just multiple before value from prefix and after value from postfix
        # outcome [24, 12, 8 , 6]

        result = [1 for i in range(len(nums))]
        prefix = [1 for i in range(len(nums))]
        postfix = [1 for i in range(len(nums))]

        #calculating prefix
        for i in range(len(nums)):
            if i == 0:
                prefix[i] = nums[0]
            else:
                prefix[i] = nums[i] * prefix[i-1]

        #calculating postfix

        for i in range(len(nums) - 1, -1 , -1):
            if i == len(nums) -1:
                postfix[i] = nums[i]
            else:
                postfix[i] = nums[i] * postfix[i+1]

        for i in range(len(nums)):
            if i == 0:
                result[i] = postfix[i+1]
            elif i == len(nums) - 1:
                result[i] = prefix[i-1]
            else:
                result[i] = prefix[i-1] * postfix[i+1]

        return result