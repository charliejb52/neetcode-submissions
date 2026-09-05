class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []
        removed = set()

        for i, char in enumerate(s):

            stack.append([char, i])


            if len(stack) >= k:

                last_k = list((list(zip(*list(stack)[len(stack)-k:]))[0]))

                if last_k == [char] * k:

                    for j in range(k):

                        curr = stack.pop()
                        print
                        removed.add(curr[1])

        
        ret = ""

        for i, char in enumerate(s):
            if i not in removed:
                ret += char

        return ret

    
                

        