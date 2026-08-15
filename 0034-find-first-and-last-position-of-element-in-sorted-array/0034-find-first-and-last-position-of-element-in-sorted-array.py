class Solution(object):
    def searchRange(self, nums, target):
        left = 0
        right = len(nums) -1
        answer = -1
        while left <= right :
            mid = (left + right)//2
            if nums[mid] == target :
                answer = mid 
                right = mid-1
                
            elif nums[mid]< target:
                left = mid+1
            else :
                right = mid -1
        left = 0
        right = len(nums) - 1
        answer_last = -1
        while left <= right :
            mid = (left + right)//2
            if nums[mid] == target :
                answer_last = mid 
                left = mid+1
            elif nums[mid]< target:
                left = mid+1
            else :
                right = mid -1
        return [answer ,answer_last]
        