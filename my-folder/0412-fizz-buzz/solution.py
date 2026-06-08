class Solution(object):
    def fizzBuzz(self, n):
        results = []
        for num in range(1, n + 1):
            if num % 15 == 0:
                results.append('FizzBuzz')
            elif num % 3 == 0:
                results.append('Fizz')
            elif num % 5 == 0:
                results.append('Buzz')
            else:
                results.append(str(num))
        return results



        """
        :type n: int
        :rtype: List[str]
        """
        
