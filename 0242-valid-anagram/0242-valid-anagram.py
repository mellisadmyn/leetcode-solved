class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # cek apakah panjang kedua string sama
        if len(s) != len(t):
            return False
        
        # hitung frekuensi setiap karakter dalam string s
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # cek frekuensi setiap karakter dalam string t apakah sama dnegan s
        for char in t:
            if char in char_count:
                char_count[char] -= 1
            else:
                return False
        
        # periksa apakah semua frekuensi karakter menjadi nol
        return all(count == 0 for count in char_count.values())