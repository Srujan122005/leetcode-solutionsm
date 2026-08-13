class Solution(object):
    def minSubArrayLen(self, target, nums):
        right = 0
        left = 0
        current_sum = 0
        min_lenghth = float('inf')
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                cwl = right-left+1
                min_lenghth = min(min_lenghth , cwl)
                current_sum -= nums[left]
                left+=1
        if min_lenghth == float("inf"):
            return 0
        return min_lenghth