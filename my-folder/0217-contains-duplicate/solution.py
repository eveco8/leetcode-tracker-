class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        obj = {}

        for num in nums:
            if num in obj:
                return True
            obj[num] = 1
        return False

            


        
