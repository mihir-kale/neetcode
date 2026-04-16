class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        track = defaultdict(list)

        for i in strs:
            univ = ''.join(sorted(i))
            track[univ].append(i) 
        
        return list(track.values())
