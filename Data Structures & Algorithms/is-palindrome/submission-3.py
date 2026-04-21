class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        d = ''
        for i in s:
            if i.isalnum():
                d += i.lower()

        l = 0
        r = len(d) - 1

        while l < r:
            if d[l] != d[r]:
                return False
            r -= 1
            l += 1
        
        return True 


        