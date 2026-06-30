class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        
        count = sum(1 for c in s[:k] if c in vowels)
        max_count = count

        for i in range(1, len(s) - k + 1):
            count += (s[i+k-1] in vowels)  
            count -= (s[i-1] in vowels)  
            max_count = max(max_count, count)
        
        return max_count


        
