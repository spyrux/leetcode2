from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = defaultdict(int)
        if len(s) >= len(t):
            for i in range(len(s)):
                counts[s[i]]+=1
            for i in range(len(t)):
                counts[t[i]]-=1
                if counts[t[i]]==0:
                    counts.pop(t[i])
        else:
            for i in range(len(t)):
                counts[t[i]]+=1
            for i in range(len(s)):
                counts[s[i]]-=1
                if counts[s[i]]==0:
                    counts.pop(s[i]) 

        print(counts)

        

        return not len(counts)>0