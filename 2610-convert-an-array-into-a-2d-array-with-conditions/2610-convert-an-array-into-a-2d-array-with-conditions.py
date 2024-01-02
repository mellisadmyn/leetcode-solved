class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # array freq untuk menyimpan frekuensi setiap elemen dalam array nums
        freq = [0] * (len(nums) + 1)
        
        # array 2D ans untuk menyimpan hasil akhir
        ans = []

        for num in nums:
            # jika frekuensi elemen saat ini >= jumlah baris saat ini di ans
            if freq[num] >= len(ans):
                # tambah sebuah baris baru ke ans
                ans.append([])
            
            # menyisipkan elemen ke dalam baris freq[num]
            ans[freq[num]].append(num)
            
            # tambah frekuensi elemen
            freq[num] += 1

        return ans