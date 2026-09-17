class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ret = []

        curr_max = max(nums[0:k])
        ret.append(curr_max)

        for start in range(1, len(nums)-k+1):
            if nums[start+(k-1)] > curr_max:
                curr_max = nums[start+(k-1)]
            elif nums[start-1] == curr_max:
                curr_max = max(nums[start:start+k])
            
            ret.append(curr_max)


        return ret


        