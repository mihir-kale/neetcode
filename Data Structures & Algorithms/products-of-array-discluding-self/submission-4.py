class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # PAES = prefix * suffix
        ret = len(nums) * [0] # we will prod the two here
        pref = len(nums) * [0]
        suff = len(nums) * [0]

        pref[0] = 1 # no prefix for zeroeth - 1
        suff[-1] = 1 # no suffix for last - 1

        # set the pref value for all i
        for i in range(1, len(nums)):
            pref[i] = nums[i - 1] * pref[i - 1]
        # pref = [1, pref for nums[1], ...]

        # set the suff values for all i
        for i in range(len(nums) - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        
        # combine 
        for i in range(len(nums)):
            ret[i] = pref[i] * suff[i]
        
        return ret

            