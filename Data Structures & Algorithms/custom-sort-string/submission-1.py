class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        ret = ""

        for char in order:

            while char in s:

                ret += char

                i = s.find(char)
                s = s[0:i] + s[i+1:]
        
        return ret + s