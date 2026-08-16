class Solution(object):
    def runningSum(self, nums):
        result = []
        running_sum = 0
        for i in range(len(nums)):
            running_sum += nums[i]
            result.append(running_sum)
        return result