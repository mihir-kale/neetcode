class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        comp = set(nums)
        res = 0

        for i in comp:
            if i - 1 not in comp:
                length = 1
                while i + length in comp:
                    length += 1

                res = max(res, length)
        
        return res

        

            