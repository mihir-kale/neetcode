class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # two pointers meeting in the middle 
        l = 0
        r = len(numbers) - 1

        # sorted list 
        while l < r:
            cur = numbers[l] + numbers[r]

            if cur > target:
                r -= 1
            elif cur < target:
                l += 1
            else:
                return [l + 1, r + 1]
            
        return []