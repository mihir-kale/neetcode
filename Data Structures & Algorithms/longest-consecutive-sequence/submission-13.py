class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums.sort() # go sequentially
        comp = set(nums)

        res = 0

        for i in nums:
            if i - 1 not in comp:
                length = 1
                while i + length in comp:
                    length += 1

            res = max(res, length)
        
        return res

        

            