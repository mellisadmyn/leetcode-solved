1. **Cek suatu karakter apakah sudah ada di dalam dictionary**
   - Pada setiap iterasi, kita cek apakah karakter tersebut sudah ada dalam dictionary `char_count` atau belum.
   - char_count.get(char, 0)` kita akan mengecek pada dictionary char_count` kita akan mencari apakah kata kunci `char` ada di dictionary tersebut, jika ada akan return nilai frekuensi saat ini yang telah dihitung untuk char tersebut dan akan ditambah 1, atau return 0 + 1 jika char tersebut belum ada.

Contoh `s = "anagram"`:

- Iterasi 1: Karakter 'a'
  - Dictionary saat ini: `{'a': 1}`
- Iterasi 2: Karakter 'n'
  - Dictionary saat ini: `{'a': 1, 'n': 1}`
- Iterasi 3: Karakter 'a'
  - Dictionary saat ini: `{'a': 2, 'n': 1}`
- Iterasi 4: Karakter 'g'
  - Dictionary saat ini: `{'a': 2, 'n': 1, 'g': 1}`
- Iterasi 5: Karakter 'r'
  - Dictionary saat ini: `{'a': 2, 'n': 1, 'g': 1, 'r': 1}`
- Iterasi 6: Karakter 'a'
  - Dictionary saat ini: `{'a': 3, 'n': 1, 'g': 1, 'r': 1}`
- Iterasi 7: Karakter 'm'
  - Dictionary saat ini: `{'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}`

Setelah semua iterasi selesai, dictionary `char_count` akan berisi frekuensi setiap karakter dalam string `s`. Dalam contoh ini, hasilnya adalah `{'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}`.

1. **Cek karakter tersebut apakah sama dengan string sebelumnya**
   - Pada setiap iterasi, kita cek apakah karakter tersebut ada dalam dictionary `char_count` yang telah diisi sebelumnya dengan frekuensi karakter dalam string s.
   - Jika karakter tersebut ada dalam dictionary `char_count`, kita akan kurangi frekuensinya dengan 1.

Contoh `t = "nagaram"`:

- Iterasi 1: Karakter 'n'
  - Dictionary saat ini: `{'a': 3, 'n': 0, 'g': 1, 'r': 1, 'm': 1}`.
- Iterasi 2: Karakter 'a'
  - Dictionary saat ini: `{'a': 2, 'n': 0, 'g': 1, 'r': 1, 'm': 1}`.
- Iterasi 3: Karakter 'g'
  - Dictionary saat ini: `{'a': 2, 'n': 0, 'g': 0, 'r': 1, 'm': 1}`.
- Iterasi 4: Karakter 'a'
  - Dictionary saat ini: `{'a': 1, 'n': 0, 'g': 0, 'r': 1, 'm': 1}`
- Iterasi 5: Karakter 'r'
  - Dictionary saat ini: `{'a': 1, 'n': 0, 'g': 0, 'r': 0, 'm': 1}`
- Iterasi 6: Karakter 'a'
  - Dictionary saat ini: `{'a': 0, 'n': 0, 'g': 0, 'r': 0, 'm': 1}`
- Iterasi 7: Karakter 'm'
  - Dictionary saat ini: `{'a': 0, 'n': 0, 'g': 0, 'r': 0, 'm': 0}`

Setelah iterasi selesai, kita melihat bahwa semua frekuensi karakter dalam `char_count` sudah menjadi 0, yang berarti bahwa `t` adalah anagram dari `s`. Jadi, algoritma ini akan return `True`.
