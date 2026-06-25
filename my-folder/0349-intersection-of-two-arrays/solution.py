class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # result = []
        # for num in nums1: 
        #     if num in nums2:
        #         result.append(num)
        # print(result) 
        # result_set = list(set(result))  
        # return result_set
        
        return list(set(nums1) & set(nums2))
        
