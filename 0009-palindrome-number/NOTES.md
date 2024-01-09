**Inisialisasi Awal**
- `x = 121`: Ini adalah angka asli yang akan diperiksa apakah palindrom atau tidak.
- `reversed_num = 0`: Variabel ini digunakan untuk menyimpan angka yang akan dihasilkan setelah digit angka aslinya dibalik.
- `original_x = 121`: Ini adalah salinan dari angka asli untuk dibandingkan nantinya.
​
**Pengecekan Kasus Khusus**
Kita periksa dua kasus khusus terlebih dahulu:
1. `x` bukan angka negatif.
2. `x` bukan berakhiran 0 (kecuali jika `x` sendiri adalah 0).
​
Dalam kasus angka 121, kita tidak masuk ke dalam salah satu kasus khusus ini, karena 121 bukan angka negatif dan bukan berakhiran 0, maka lnjut ke kondisi selanjutnya.
​
**Pembalikan Digit Angka**
Kita menggunakan loop untuk membalikkan digit angka:
1. **Iterasi 1:**
- `last_digit = 1`: Ini adalah digit terakhir dari angka `x`.
- `x = 12`: Kita hapus digit terakhir dari `x`.
- `reversed_num = 0 * 10 + 1 = 1`: Kita tambahkan `last_digit` ke `reversed_num` setelah mengalikan dengan 10.
2. **Iterasi 2:**
- `last_digit = 2`: Digit terakhir dari angka `x`.
- `x = 1`: Hapus digit terakhir dari `x`.
- `reversed_num = 1 * 10 + 2 = 12`: Tambahkan `last_digit` ke `reversed_num` setelah mengalikan dengan 10.
3. **Iterasi 3:**
- `last_digit = 1`: Digit terakhir dari angka `x`.
- `x = 0`: Hapus digit terakhir dari `x`.
- `reversed_num = 12 * 10 + 1 = 121`: Tambahkan `last_digit` ke `reversed_num` setelah mengalikan dengan 10.
​
**Pengecekan Palindrom**
Terakhir, kita memeriksa apakah `reversed_num` (121) sama dengan `original_x` (121). Dalam kasus angka 121, keduanya sama, sehingga fungsi mengembalikan `True`.