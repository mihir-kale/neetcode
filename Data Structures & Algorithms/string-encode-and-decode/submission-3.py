class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ''
        for i in strs:
            length = str(len(i))
            ret = ret + str(length) + "#" + i
        
        return ret 

    def decode(self, s: str) -> List[str]:

        ret = []
        a = 0
    
        while a < len(s):
            b = a 
            while s[b] != '#':
                b += 1
            
            length = int(s[a:b])
            a = b + 1
            b = a + length  
            ret.append(s[a:b])
            a = b
        
        return ret


            

        

