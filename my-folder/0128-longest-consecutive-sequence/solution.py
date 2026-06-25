class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()
        print(nums)

        curr_length = 1
        prev_length = 1

        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i] + 1:
                curr_length += 1
            elif nums[i] == nums[i + 1]:
                continue
            elif nums[i + 1] != nums[i] + 1:
                prev_length = max(prev_length, curr_length)
                curr_length = 1

        
        return max(prev_length, curr_length)



