class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dictionary untuk menyimpan indeks dari setiap elemen
        num_indices = {}
        
        for i, num in enumerate(nums):
            # hitung komplement yang diperlukan untuk mencapai target
            complement = target - num

            # memeriksa apakah komplement sudah ada di dalam kamus
            if complement in num_indices:
                # mengembalikan indeks dari dua angka yang diinginkan
                return [num_indices[complement], i]

            # menambahkan ke dalam kamus
            num_indices[num] = i
            
        return []