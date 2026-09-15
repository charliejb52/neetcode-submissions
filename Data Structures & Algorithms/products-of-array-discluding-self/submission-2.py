class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if len(nums) < 2:
            return nums

        going_up = [0] * len(nums)
        coming_down = [0] * len(nums)

        gu = 1
        cd = 1

        for i in range(len(nums)):
            gu *= nums[i]
            going_up[i] = gu

            cd *= nums[len(nums)-1-i]
            coming_down[len(nums)-1-i] = cd


        ret = [0] * len(nums)
        ret[0] = coming_down[1]
        ret[-1] = going_up[-2]

        for i in range(1, len(nums)-1):
            ret[i] = going_up[i-1] * coming_down[i+1]

        return ret

        