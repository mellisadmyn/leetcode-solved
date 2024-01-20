- Tidak ada elemen unik baru yang ditemukan.
​
6. **Iterasi Kelima (i=5):**
- `nums[5] = 2` tidak sama dengan `nums[unique_pointer] = 1`
- Increment `unique_pointer` menjadi 2.
- Set `nums[2]` (indeks `unique_pointer`) ke 2, sehingga array sejauh ini menjadi `[0,1,2,1,1,2,2,3,3,4]`.
​
7. **Iterasi Keenam (i=6):**
- `nums[6] = 2` sama dengan `nums[unique_pointer] = 2`
- Tidak ada elemen unik baru yang ditemukan.
​
8. **Iterasi Ketujuh (i=7):**
- `nums[7] = 3` tidak sama dengan `nums[unique_pointer] = 2 `
- Increment `unique_pointer` menjadi 3.
- Set `nums[3]` (indeks `unique_pointer`) ke 3, sehingga array sejauh ini menjadi `[0,1,2,3,1,2,2,3,3,4]`.
​
9. **Iterasi Kedelapan (i=8):**
- `nums[8] = 3` sama dengan `nums[unique_pointer] = 3`
- Tidak ada elemen unik baru yang ditemukan.
​
10. **Iterasi Kesembilan (i=9):**
- `nums[9] = 4` tidak sama dengan `nums[unique_pointer] = 3`
- Increment `unique_pointer` menjadi 4.
- Set `nums[4]` (indeks `unique_pointer`) ke 4, sehingga array sejauh ini menjadi `[0,1,2,3,4,2,2,3,3,4]`.
​
11. **Hasil Akhir:**
- `unique_pointer` sekarang adalah 4.
- Panjang array yang unik adalah `unique_pointer + 1`, yaitu 5