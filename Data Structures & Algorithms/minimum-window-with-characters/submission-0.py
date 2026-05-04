class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        l = 0
        r = l + len(t)

        count = {}
        window = {}

        # count the needed chars
        for c in t:
            count[c] = 1 + count.get(c, 0)

        have = 0
        need = len(count)

        res = [-1, -1]
        resLen = float("infinity")

        # window set up
        l = 0
        for r in range(len(s)):
            c = s[r]

            window[c] = 1 + window.get(c, 0)

            # is this char in both strings at the same freq?
            if c in count and window[c] == count[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1
                
                l += 1
            
        l, r = res
        if resLen != float("infinity"):
            return s[l:r+1]
        else:
            return ""
