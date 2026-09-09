class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        def valid(nums, limit):
            if max(nums) - min(nums) <= limit:
                return True
            else:
                return False

        max_len = 1

        for i in range(len(nums)):
            curr_max, curr_min = nums[i], nums[i]

            j = i+1
            still_going = True
            while j < len(nums) and still_going:
                curr_max = max(curr_max, nums[j])
                curr_min = min(curr_min, nums[j])

                if curr_max - curr_min > limit:
                    still_going = False
                elif j - i + 1 > max_len:
                    max_len = j - i + 1
                    print(nums[i:j+1])

                j += 1

                

        return max_len


        