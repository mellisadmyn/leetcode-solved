### Iterasi 1: String "eat"
1. **Sorting Karakter**:
- String "eat" diurutkan menjadi "aet".
2. **Cek Kunci Ada atau Belum**:
- Kunci "aet" belum ada dalam `anagram_groups`.
3. **Tambahkan Kunci dan List Kosong**:
- Tambahkan kunci "aet" ke dalam `anagram_groups` dengan nilai berupa list kosong.
```anagram_groups = {"aet": []}```
4. **Append String ke Kelompok yang Sesuai**:
- Tambahkan string "eat" ke dalam list yang terkait dengan kunci "aet".
```anagram_groups = {"aet": ["eat"]} ```
​
### Iterasi 2: String "tea"
1. **Sorting Karakter**:
- String "tea" diurutkan menjadi "aet".
2. **Cek Kunci Ada atau Belum**:
- Kunci "aet" sudah ada dalam `anagram_groups`.
3. **Append String ke Kelompok yang Sesuai**:
- Tambahkan string "tea" ke dalam list yang terkait dengan kunci "aet".
```anagram_groups = {"aet": ["eat", "tea"]}```
​
### Iterasi 3: String "tan"
1. **Sorting Karakter**:
- String "tan" diurutkan menjadi "ant".
2. **Cek Kunci Ada atau Belum**:
- Kunci "ant" belum ada dalam `anagram_groups`.
3. **Tambahkan Kunci dan List Kosong**:
- Tambahkan kunci "ant" ke dalam `anagram_groups` dengan nilai berupa list kosong.
```anagram_groups = {"aet": ["eat", "tea"], "ant": []}```
4. **Append String ke Kelompok yang Sesuai**:
- Tambahkan string "tan" ke dalam list yang terkait dengan kunci "ant".
```anagram_groups = {"aet": ["eat", "tea"], "ant": ["tan"]}```
​
Dst ...