class Solution(object):
    def twoSum(self, nums, target):
        my_dist = {}

        for i, num in enumerate(nums):
            required = target - num
            if required in my_dist:
                return[my_dist[required],i]
            my_dist[num] = i
        return []