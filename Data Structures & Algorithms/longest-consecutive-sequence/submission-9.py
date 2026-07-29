class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        for i in nums:
            if i - 1 not in nums:
                c = 1
                while i + c in nums:
                    c += 1
                if c >= longest:
                    longest = c
        
        return longest 

                    