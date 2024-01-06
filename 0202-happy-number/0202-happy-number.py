class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            
            while n > 0:
                last_digit = n % 10
                n = n // 10
                total_sum += last_digit ** 2
            return total_sum
        
        seen_numbers = set()
        while n != 1 and n not in seen_numbers:
            seen_numbers.add(n)
            n = get_next(n)

        return n == 1