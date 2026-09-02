class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ret = target[0]

        for i in range(1,len(target)):
            last = target[i-1]
            if target[i] > last:
                ret += (target[i] - last)

        return ret
        