class Solution:

  def nextGreaterElement(self, nums1, nums2):
    next_greater = {}
    stack = []

    for num in nums2:
      while stack and num > stack[-1]:
        next_greater[stack.pop()] = num
      stack.append(num)

    return [next_greater.get(x, -1) for x in nums1]