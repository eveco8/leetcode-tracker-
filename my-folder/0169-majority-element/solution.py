class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # freq = {}
        # for num in nums:
        #     if freq.get(num) is None:
        #         freq[num] = 1
        #     else:
        #         freq[num] += 1

        # maxNum = max(freq, key=freq.get)
        # print(freq)
        # return maxNum

        nums.sort()
        n = len(nums)
        return nums[n//2]

