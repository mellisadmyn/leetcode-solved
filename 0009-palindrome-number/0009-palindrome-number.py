class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Special cases:
        # 1. Angka negatif bukan palindrom
        # 2. Angka yang berakhiran 0 (kecuali 0 itu sendiri) bukan palindrom
        
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_num = 0
        original_x = x

        while x > 0:
            last_digit = x % 10
            x = x // 10
            reversed_num = reversed_num * 10 + last_digit

        # memeriksa apakah angka yang dibalikkan sama dengan angka aslinya
        return reversed_num == original_x
