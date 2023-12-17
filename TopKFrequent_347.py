class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        result = []
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        add = 0
        max = -100000
        maxVal = 0
        while add < k:
            for key, v in freq.items():
                if v >= max:
                    maxVal = key
                    max = v
            result.append(maxVal)
            del freq[maxVal]
            add += 1
            max = -100000
            maxVal = 0

        return result

    def topKFrequentOptimized(self, nums, k):
        #youtube: https://www.youtube.com/watch?v=YPTqKIgVk-k
        count = {}

        #lets get array of size of nums so that on each index(count) we put the number
        #input [1,1,1,1,1,1]
        #example freq[sixtimes] = [1]
        freq = [[] for i in range(len(nums) + 1)]

        result = []

        for num in nums:
            #getting counts
            count[num] = count.get(num, 0) + 1

        #now we put this in our 2d Array
        for key, value in count.items():
            freq[value].append(key)

        # here want to run inverse loop
        for i in range(len(freq)-1, 0 , -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result