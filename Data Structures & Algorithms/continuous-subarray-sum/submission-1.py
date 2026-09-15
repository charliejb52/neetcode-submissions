class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        for start in range(len(nums)-1):

            sum = nums[start]

            for i in range(start+1, len(nums)):

                sum += nums[i]
                if sum % k == 0:
                    return True

        return False


        