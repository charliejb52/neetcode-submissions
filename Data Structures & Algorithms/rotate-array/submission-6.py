class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if k >= len(nums):
            k = k % len(nums)

        k = len(nums)-k

        first_half = nums[0:k]
        second_half = nums[k:]

        nums[:] = second_half + first_half

        
        