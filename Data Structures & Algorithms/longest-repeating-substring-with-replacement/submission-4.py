class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # find the most common character 

        res = 0
        count = {}
        maxf = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]]) # is this the max char?

            while (r - l + 1) - maxf > k: #can we form single char substring
                count[s[l]] -= 1
                l += 1 # move inward from left until k = replacements 

            res = max(res, r - l + 1)
        
        return res 

