class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # function untuk mengecek suatu karakter itu alphanumeric
        def is_alphanumeric(char):
            return ('a' <= char <= 'z' or 'A' <= char <= 'Z' or '0' <= char <= '9')

        # dua pointers
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not is_alphanumeric(s[left]):
                left += 1

            while left < right and not is_alphanumeric(s[right]):
                right -= 1

            # jika semua compare characters dan ignore case
            if left < right and s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1
            
        return True