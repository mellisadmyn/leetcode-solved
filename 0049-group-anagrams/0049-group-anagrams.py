class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}
        
        for s in strs:
            # sorting karakter dalam string untuk mendapatkan kunci
            sorted_key = ''.join(sorted(s))
            
            # tambah empty list jika sorted_key belum ada
            if sorted_key not in anagram_groups:
                anagram_groups[sorted_key] = []
            
            # append original string ke hashmap
            anagram_groups[sorted_key].append(s)
        
        return list(anagram_groups.values())