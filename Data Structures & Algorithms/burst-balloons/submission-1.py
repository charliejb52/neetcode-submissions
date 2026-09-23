class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        def pop(new_nums, i):

            left = 1
            right = 1

            if i-1 >= 0:
                left = new_nums[i-1]
            if i+1 < len(new_nums):
                right = new_nums[i+1]

            return left*new_nums[i]*right

        maxs = {}
        
        def dfs(new_nums):

            if new_nums == []:
                return 0
            
            if tuple(new_nums) in maxs:
                return maxs[tuple(new_nums)]

            
            emp_max = 0

            for i in range(len(new_nums)):

                value_popped = pop(new_nums, i)
                after_popping = new_nums[0:i] + new_nums[i+1:]
                curr = value_popped + dfs(after_popping)
                if curr > emp_max:
                    emp_max = curr

            maxs[tuple(new_nums)] = emp_max
            return emp_max

        
        return dfs(nums)
        