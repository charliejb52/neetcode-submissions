class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:


        longest = strs[0]

        for word in strs[1:]:

            if word == "":
                return ""

            for j, char in enumerate(longest):

                if j > (len(word) - 1) or char != word[j]:
                    longest = longest[0:j]
                    break

        return longest

        