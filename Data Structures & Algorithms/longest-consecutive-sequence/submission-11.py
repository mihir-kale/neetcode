class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums.sort() # go sequentially
        comp = set(nums)

        res = 0

        for i in nums:
            if i - 1 not in comp:
                length = 1
                it = 1
                while i + it in comp:
                    it += 1
                    length += 1
            res = max(res, length)
        
        return res

        

            