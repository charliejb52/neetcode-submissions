class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = {}
        n = len(nums)

        def dfs(i, tot) -> int:

            if (i, tot) in dp:
                return dp[(i, tot)]

            if i == n:
                if tot == target:
                    dp[(i, tot)] = 1
                else:
                    dp[(i, tot)] = 0
                return dp[(i, tot)]

            dp[(i, tot)] = dfs(i + 1, tot + nums[i]) + dfs(i + 1, tot - nums[i])
            return dp[(i, tot)]

        
        return dfs(0, 0)

            

        

