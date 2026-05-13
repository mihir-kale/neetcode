class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
    # if a car reaches the destination before or at the same time as a car ahead, 
    # it must be part of the same fleet as that car,

        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse = True)
        # pair is now sorted in desceding order by position


        stack = [] # store the time remaining 
        for p, s in pair: 
            stack.append((target - p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]: # is the closer car reaching before the next closest one
                stack.pop() # reduce fleet count 
        return len(stack)