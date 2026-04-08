class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list) # provides default keys 

        for i in strs:
            comp = ''.join(sorted(i))
            groups[comp].append(i) # initial instance relies on default
            
        return list(groups.values()) # join up all the values, exclude comps

