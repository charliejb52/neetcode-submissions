class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        tot = sum(nums)

        def dfs(curr, i):

            if (curr == tot - curr):
                return True

            if i >= len(nums):
                return False

            
            return (dfs(curr + nums[i], i+1)) or (dfs(curr, i+1))

        return dfs(0, 0)

        