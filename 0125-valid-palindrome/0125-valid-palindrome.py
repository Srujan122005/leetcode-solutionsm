class Solution(object):
    def isPalindrome(self, s):
       cl = "".join(ch.lower() for ch in s if ch.isalnum())
       left = 0
       right = len(cl)-1
       while left<right:
        if cl[left] != cl[right]:
            return False
        left+=1
        right-=1
       return True