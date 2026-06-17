class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if freq.get(num) is None:
                freq[num] = 1
            else:
                freq[num] += 1

        minNum = min(freq, key=freq.get)
        print(freq)
        return minNum
