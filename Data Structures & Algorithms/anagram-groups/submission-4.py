class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

       # create a hashmap with the key being the alphabetical joined

       res = defaultdict(list)
       # defaultdict allows additions without initializations 

       for i in strs:
            skey = ''.join(sorted(i)) 
            res[skey].append(i)
       return list(res.values())
